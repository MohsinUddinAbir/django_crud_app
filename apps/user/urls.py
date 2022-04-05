
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import (
   PasswordResetView,
   PasswordResetDoneView,
   PasswordResetConfirmView,
   PasswordResetCompleteView,
	PasswordChangeView,
   PasswordChangeDoneView
)

from . import views

urlpatterns = [ 
   path('signup/', views.signup, name='signup'),
   path('login/', views.log_in, name='login'),
   path('logout/', views.log_out, name='logout'),
   path('profile/<username>/', views.profile, name='profile'),
   path('edit-profile/', views.edit_profile, name='edit_profile'),

   path('password_reset/', PasswordResetView.as_view(
      template_name='user/password_reset.html',
      email_template_name='user/password_reset_email.html',
      subject_template_name='user/password_reset_subject.txt',
      success_url='/password_reset/done/',
      from_email="mohsinuddinabir@hotmail.fr"),
      name='password_reset'
   ),
   path('password_reset/done/', PasswordResetDoneView.as_view(
      template_name='user/password_reset_done.html'),
      name='password_reset_done'
   ),
   path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
      template_name='user/password_reset_confirm.html',
      success_url='/reset/done/'),
      name='password_reset_confirm'
   ),
   path('reset/done/', PasswordResetCompleteView.as_view(
      template_name='user/password_reset_complete.html'),
      name='password_reset_complete'
   ),
	path('password_change/', PasswordChangeView.as_view(
      template_name='user/password_change.html',
      success_url=reverse_lazy('password_change_done')),
      name='password_change'
	),
   path('password_change/done/', PasswordChangeDoneView.as_view(
      template_name='user/password_change_done.html'),
       name='password_change_done'),
]
