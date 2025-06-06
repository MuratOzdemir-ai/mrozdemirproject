from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<int:pk>/', views.project_detail_view, name='project_detail'),
    path('contact/', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
    path('education-and-achievements/', views.education_and_achievements_view, name='education_and_achievements'),
    path('support/', views.support_message_view, name='support_message'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/<int:pk>/', views.blog_detail_view, name='blog_detail'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name='portfolio/logout.html'), name='logout'),
]


