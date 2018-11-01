"""openbook_org URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from openbook_org_common.views import Health
from openbook_org_contact.views import Contact, WaitlistSubscribeView

urlpatterns = [
    path('health/', Health.as_view(), name='health'),
    path('contact/', Contact.as_view(), name='contact'),
    path('waitlist/subscribe/', WaitlistSubscribeView.as_view(), name='waitlist_subscribe')
]
