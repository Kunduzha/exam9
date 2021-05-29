from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import DetailView, UpdateView

from accounts.forms import MyUserCreationForm, UserChangeForm, ProfileChangeForm, PasswordChangeForm



def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('main_page')
    else:
        form = MyUserCreationForm()
    return render(request, 'registration/user_create.html', context={'form': form})


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        # projects = self.get_object().projects.all()
        # paginator = Paginator(projects, self.paginate_related_by, orphans=self.paginate_related_orphans)
        # page_number = self.request.GET.get('page', 1)
        # page = paginator.get_page(page_number)
        # kwargs['page_obj'] = page
        # kwargs['projects'] = page.object_list
        # kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class UserChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_profile_form()
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = self.get_profile_form()
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        response = super().form_valid(form)
        profile_form.save()
        return response

    def form_invalid(self, form, profile_form):
        context = self.get_context_data(form=form, profile_form=profile_form)

    def get_object(self, queryset=None):
        return self.request.user

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == 'POST':
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES

        return ProfileChangeForm(**form_kwargs)

    def get_success_url(self):
        return reverse('account:detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'user_password_change.html'

    def get_success_url(self):
        return reverse('account:detail', kwargs={'pk': self.request.user.pk})
