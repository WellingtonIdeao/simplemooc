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
from courses import views

app_name = 'courses'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    #GET /
    path('', views.index, name='index'),
    #re_path(r'(?P<pk>\d+)/$', views.details, name='details'),
    re_path(r'(?P<slug>[\w_-]+)/$', views.details, name='details'),
    re_path(r'(?P<slug>[\w_-]+)/inscricao$', views.enrollment, name='enrollment'),
    re_path(r'(?P<slug>[\w_-]+)/cancelar-inscricao$', views.undo_enrollment,
            name='undo_enrollment'),
    re_path(r'(?P<slug>[\w_-]+)/anuncios$', views.announcements,
            name='announcements'),
    re_path(r'(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)$', views.show_announcement,
            name='show_announcement'),
]