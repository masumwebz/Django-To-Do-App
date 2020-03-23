from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='user_list'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    #path('profile/<int:pk>', views.register, name='login'),



    # path('update_task/<int:pk>/', views.updateTask, name='update'),
    # path('delete/<int:pk>', views.deleteTask, name='delete'),
]