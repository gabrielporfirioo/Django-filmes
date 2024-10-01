from django.urls import path, include
from . import views

urlpatterns = [
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.movie_list, name='movie_list'),
    path('add/', views.add_movie, name='add_movie'),
    path('signup/', views.signup, name='signup'),
    path('delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    
    

    
]
