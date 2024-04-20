from django.urls import path
from . import views

urlpatterns = [
    path('', views.libro_list, name='libro_list'),
    path('libro/<int:pk>/', views.libro_detail, name='libro_detail'),
    path('libro/create/', views.libro_create, name='libro_create'),
    path('libro/<int:pk>/update/', views.libro_update, name='libro_update'),
    path('libro/<int:pk>/delete/', views.libro_delete, name='libro_delete'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.user_profile, name='user_profile'),
]