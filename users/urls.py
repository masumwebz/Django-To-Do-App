from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='user_list'),
    path('signup', views.signup, name='signup'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutuser, name='logout'),
    #path('update_profile/<int:pk>', views.update, name='update_profile'),



    # path('update_task/<int:pk>/', views.updateTask, name='update'),
    # path('delete/<int:pk>', views.deleteTask, name='delete'),
]