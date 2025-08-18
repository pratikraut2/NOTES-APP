
from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.home, name='home'),
    path('add/',views.add, name='add'),
    path('edit/<int:note_id>',views.edit, name='edit'),
    path('delete/<int:note_id>/', views.delete, name='delete'),   
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
