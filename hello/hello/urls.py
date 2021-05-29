"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include
from django.conf import settings

from webapp.views import GalleryMore, GalleryAdd, GalleryChange, DeleteGallery, IndexViewGallery, ChoiceGallery, UnChoiceForGallery
from webapp.views import IndexViewAlbom, AlbomMore, AlbomChange, AlbomDelete, AlbomAdd, ChoiceForAlbom, UnChoiceForAlbom
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexViewAlbom.as_view(), name='main_page'),
    # path('more/<int:pk>/', Good_more.as_view(), name='see_good'),
    path('more/<int:pk>/', AlbomMore.as_view(), name='see_albom'),
    path('fotos/<int:pk>/', IndexViewGallery.as_view(), name='see_fotos'),
    path('add/', AlbomAdd.as_view(), name='add_albom'),
    path('edit/<int:pk>/', AlbomChange.as_view(), name='change_albom'),
    path('delete/<int:pk>/', AlbomDelete.as_view(), name='del_albom'),
    path('<int:pk>/add_foto/', GalleryAdd.as_view(), name='adding_foto'),
    path('delete_foto/<int:pk>/', DeleteGallery.as_view(), name='delete_foto'),
    path('update/<int:pk>/', GalleryChange.as_view(), name='update_foto'),
    path('more_foto/<int:pk>/', AlbomMore.as_view(), name='see_foto'),
    path('<int:pk>/choice_gallery', ChoiceGallery.as_view(), name='choice_gallery'),
    path('<int:pk>/unchoice_gallery', UnChoiceForGallery.as_view(), name='unchoice_gallery'),
    path('<int:pk>/choice_albom', ChoiceForAlbom.as_view(), name='choice_albom'),
    path('<int:pk>/unchoice_albom', UnChoiceForAlbom.as_view(), name='unchoice_albom'),
    path('accounts/', include('accounts.urls')),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)