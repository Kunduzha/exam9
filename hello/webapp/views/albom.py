from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponse
from django.utils.http import urlencode
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from webapp.forms import AlbomForms, SimpleSearchForm
from webapp.models import Albom, Gallery
from django.urls import reverse_lazy
from django.db.models import Q

from webapp.views.gallery import ChoiceForGallery


class IndexViewAlbom(ListView):
    model = Albom
    template_name = 'Albom/index.html'
    context_object_name = 'alboms'
    paginate_by = 3
    paginate_orphans = 1


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, object_list = None, **kwargs):
        context = super().get_context_data(object_list= object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})

        choices_alboms = []
        gallery_choice = []
        if self.request.user.is_authenticated:
            choices = ChoiceForAlbom.objects.filter(user=self.request.user)
            choices_gallery = ChoiceForGallery.objects.filter(user = self.request.user)
            for choice in choices:
                choices_alboms.append(choice.albom.pk)
            for choice_gallery in choices_gallery:
                gallery_choice.append(choice_gallery.gallery.pk)

        context['choices_alboms'] = choices_alboms
        context['choices_gallery'] = gallery_choice
        return context
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)  | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset.order_by('name')

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None




class AlbomMore(DetailView):
    model = Albom
    template_name = 'Albom/albom_more.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        if user.is_authenticated and user.groups.filter(name='moderator').exists():
            kwargs['galleries'] = Gallery.objects.filter(gallery__pk=self.get_object().pk)

        return super().get_context_data(**kwargs)



class AlbomAdd(LoginRequiredMixin, CreateView):
    template_name = 'Albom/add_albom.html'
    model = Albom
    form_class = AlbomForms

    def get_success_url(self):
        return reverse('see_albom', kwargs = {'pk': self.object.pk})


class AlbomChange(LoginRequiredMixin, UpdateView):
    model = Albom
    template_name = 'Albom/update_albom.html'
    form_class = AlbomForms
    context_object_name = 'alboms'

    def get_success_url(self):
        return reverse('see_albom', kwargs={'pk': self.object.pk})




class AlbomDelete(LoginRequiredMixin, DeleteView):
    template_name = 'Albom/albom_delete.html'
    model = Albom
    context_object_name = 'alboms'
    success_url = reverse_lazy('main_page')



class ChoiceForAlbom(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        albom = get_object_or_404(Albom, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            ChoiceForAlbom.objects.get(albom=albom, user=user)
            return HttpResponseForbidden("error")
        except ChoiceForAlbom.DoesNotExist:
            ChoiceForAlbom.objects.create(albom=albom, user=user)
        return HttpResponse(albom.choice_albom)




class UnChoiceForAlbom(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        albom = get_object_or_404(Albom, pk=self.kwargs.get('pk'))
        user = request.user
        try:
            choice = ChoiceForAlbom.objects.get(albom=albom, user=user)
            choice.delete()
            return HttpResponse(albom.choice_albom)
        except ChoiceForAlbom.DoesNotExist:
            return HttpResponseForbidden("error")
