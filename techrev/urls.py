from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('review/create/', views.review_create, name='review_create'),
    path('review/<int:rev_id>/', views.review_get, name='review'),
]