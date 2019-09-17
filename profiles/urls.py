from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.userProfile, name='profile'),
    path('', views.history_list_view, name='history')
]