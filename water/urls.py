"""pintuan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from water import views

urlpatterns = [
    url(r'^wx/$', views.wx, name='wx'),
    url(r'^about/$', views.about, name='about'),
    url(r'^agent/$', views.agent, name='agent'),

    url(r'^buy/$', views.buy, name='buy'),

    url(r'^coordinate/$', views.coordinate, name='coordinate'),

    url(r'^feedback/$', views.feedback, name='feedback'),

    url(r'^privatecenter/$', views.privatecenter, name='privatecenter'),

    url(r'^production/(?P<production_type>.+)/$', views.production, name='production'),
]
