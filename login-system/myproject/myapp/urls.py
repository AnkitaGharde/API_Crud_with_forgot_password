from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
#basic urls

   path('',views.dashbord, name='dashbord'),
   path('signup/',views.signup,name='signup'),
   path('login/',views.login,name='login'),
   path('logout/', views.logout, name='logout'),
   path('django/',views.djangodash, name='djangodash'),

#forgot-pass
   path('resetpass',views.resetpass, name='resetpass'),
   path('otp',views.OTP, name='otp'),
   path('passchange',views.passChange, name='passchange'),

#drf-api
   path('api/', views.apiOverview, name="api-overview"),
   path('user-list/', views.userList, name="task-list"),
   path('user-detail/<str:pk>/', views.userDetail, name="task-detail"),
   path('user-create/', views.userCreate, name="task-create"),
   path('user-update/<str:pk>/', views.userUpdate, name="task-update"),
   path('user-delete/<str:pk>/', views.userDelete, name="task-delete"),



 ]