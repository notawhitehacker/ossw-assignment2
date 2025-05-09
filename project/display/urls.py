
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='proj_list'),
    path('<str:name>/', views.display_proj, name='proj_detail')
]