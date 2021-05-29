from django import forms
from webapp.models import Gallery, Albom


class Galleryform(forms.ModelForm):
    class Meta:
        model=Gallery
        fields=('image', 'caption', 'user', 'status')


class GalleryDeleteForm(forms.Form):
    caption=forms.CharField(max_length=100, required=True, label='Введите текст подписи  чтобы удалить его')



class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Найти")


class AlbomForms(forms.ModelForm):

    class Meta:
        model=Albom
        fields = ['name', 'description', 'created_at', 'status']


# class PrivateForm(forms.ModelForm):
#
#     class Meta:
#         model=Albom
#         fields = ['text_review', 'rating', 'moderation']