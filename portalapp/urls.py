from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # logout → login ki
    path('', views.home_view, name='home'),             # home
    path('results/', views.result_view, name='result'), # results page
]
