from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from accounts.models import Profile


class MyUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", required=True, widget=forms.PasswordInput, strip=False)
    email = forms.EmailField(label='Почтовый адресс', required=True)
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name and not last_name:
            raise ValidationError('Заполните хотя бы одно поле first_name или last_name!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            Profile.objects.create(user=user)
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']




class UserChangeForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label='Новый пароль', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label='Старый пароль', strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm  = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password !=password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        print(self.instance)
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Старый пароль неправильный!')
        return old_password

    def save(self, commit = True):
        user = self.instance
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['password', 'password_confirm', 'old_password']