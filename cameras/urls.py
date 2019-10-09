from django.urls import path
from . import views

app_name = 'cameras'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:camera_id>/preview.jpg', views.preview, name="preview"),
    path('<str:camera_id>/images/', views.images, name="images"),
]