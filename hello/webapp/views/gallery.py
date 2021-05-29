from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.http import urlencode
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import Galleryform, GalleryDeleteForm, SimpleSearchForm
from webapp.models import Gallery, Albom
from django.urls import reverse_lazy
from django.db.models import Q


class IndexViewGallery(ListView):
    template_name = 'Galery/index.html'
    model = Gallery
    context_object_name = 'galleries'
# class IndexViewGallery(ListView):
#     model = Gallery
#     template_name = 'Galery/index.html'
#     context_object_name = 'galleries'
#     paginate_by = 3
#     paginate_orphans = 1
#
#
#     def get(self, request, *args, **kwargs):
#         self.form = self.get_search_form()
#         self.search_value = self.get_search_value()
#         return super().get(request, *args, **kwargs)
#
#     def get_context_data(self, *args, object_list = None, **kwargs):
#         context = super().get_context_data(object_list= object_list, **kwargs)
#         context['form'] = self.form
#         if self.search_value:
#             context['query'] = urlencode({'search': self.search_value})
#         return context
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         if self.search_value:
#             query = Q(caption__icontains=self.search_value)
#             queryset = queryset.filter(query)
#         return queryset.order_by('-created_at')
#
#     def get_search_form(self):
#         return SimpleSearchForm(self.request.GET)
#
#     def get_search_value(self):
#         if self.form.is_valid():
#             return self.form.cleaned_data['search']
#         return None




class GalleryMore(DetailView):
    model = Gallery
    template_name = 'Galery/gallery_detail.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        # if user.is_authenticated and user.groups.filter(name='moderator').exists():
        #     kwargs['reviews'] = Review.objects.filter(good__pk=self.get_object().pk)
        # else:
        #     kwargs['reviews'] = Review.objects.filter(moderation=True, good__pk=self.get_object().pk)
        return super().get_context_data(**kwargs)



class GalleryAdd(LoginRequiredMixin, CreateView):
    template_name = 'Galery/galery_add.html'
    model = Gallery
    form_class = Galleryform

    # def get_success_url(self):
    #     return reverse(Gallery, kwargs = {'pk': self.object.pk})

    def form_valid(self, form):
        albom = get_object_or_404(Albom, pk=self.kwargs.get('pk'))
        gallery = form.save(commit=False)
        gallery.albom = albom
        gallery.user = self.request.user
        gallery.save()
        return redirect('see_albom', pk=albom.pk)

class GalleryChange(PermissionRequiredMixin, UpdateView):
    model = Gallery
    template_name = 'Galery/change_galery.html'
    form_class = Galleryform
    context_object_name = 'galleries'
    permission_required = 'webapp.change_gallery'

    def has_permission(self, request):
        return super().has_permission() or self.request.user == self.get_object().user



    def get_success_url(self):
        return reverse('see_gallery', kwargs={'pk': self.object.pk})



class DeleteGallery(PermissionRequiredMixin, DeleteView):
    model = Gallery
    permission_required = 'webapp.delete_gallery'
    template_name = 'Galery/galery_del.html'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().user

    def get_success_url(self):
        return reverse('see_albom', kwargs={'pk': self.object.albom.pk})

