from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('upload/', views.upload_image, name='upload_image'),
    path('table/', views.table_view, name='table_view'),
]
