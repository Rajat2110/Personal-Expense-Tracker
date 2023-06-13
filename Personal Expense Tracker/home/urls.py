from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('handleSignup/',views.handleSignup,name='handleSignup'),
    path('handlelogin/',views.handlelogin,name='handlelogin'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "reset_password.html"),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="home/reset_password_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name ="home/password_reset_form.html"),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetView.as_view(template_name ="home/password_reset_done.html"),name='password_reset_complete'),
    path('handleLogout/',views.handleLogout,name='handleLogout'),
    path('addmoney/',views.addmoney,name='addmoney'),
    path('addmoney_submit/',views.addmoney_submit,name='addmoney_submit'),
    path('expense_delete/<int:id>',views.expense_delete,name='expense_delete'),
    path('profile/',views.profile,name='profile'),
    path('weeklyexpense/',views.weeklyexpense,name='weeklyexpense'),
    path('monthlyexpense/',views.monthlyexpense,name='monthlyexpense'),
    path('expense_week/',views.expense_week, name='expense_week'),
    path('expense_month/',views.expense_month, name='expense_month'),
    path('info_year/',views.info_year, name='info_year'),
    path('yearly/',views.yearly, name = 'yearly'),
    path('history/',views.history,name='history'),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('<int:id>/editprofile/',views.editprofile,name="editprofile"),
    path('<int:id>/profile_update/',views.profile_update,name="profile_update"),
]