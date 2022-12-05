from django.urls import path

from . import views

urlpatterns = [
    path('', views.greetings, name='greetings'),
    path('shop/', views.list_item, name='list_item'),
    path('<int:id>/shop/', views.detail_item, name='detail_item'),
]