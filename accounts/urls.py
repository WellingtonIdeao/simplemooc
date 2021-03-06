"""courses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views as accounts_views
app_name = 'accounts'
# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    #GET /
    path('', accounts_views.dashboard, name='dashboard'),
    path('entrar', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('sair', auth_views.LogoutView.as_view(next_page='website:home'), name='logout'),
    path('cadastra-se', accounts_views.register, name='register'),
    path('nova-senha', accounts_views.password_reset, name='password_reset'),
    re_path(r'confirmar-nova-senha(?P<key>\w+)/$',
            accounts_views.password_reset_confirm,
            name='password_reset_confirm'),
    path('editar', accounts_views.edit, name='edit'),
    path('editar-senha', accounts_views.edit_password, name='edit_password')

]
