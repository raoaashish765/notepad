from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('note/<str:nid>/', views.note, name="note"),
    path('create', views.create, name="create"),
    path('updt', views.updt, name="updt"),
]
