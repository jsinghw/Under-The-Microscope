from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view)
]
