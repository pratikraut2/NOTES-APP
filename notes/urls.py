
from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.login_view, name='login'),   # root → login page
    path('home/', views.home, name='home'),    # home page after login
    path('add/', views.add, name='add'),
    path('edit/<int:note_id>', views.edit, name='edit'),
    path('delete/<int:note_id>/', views.delete, name='delete'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
