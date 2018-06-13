"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from release.views import LoginView,AdminExamineView,ModifyPasswordView,ReleaseListView,RechargeView


urlpatterns = [
#    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^examine/', AdminExamineView.as_view(), name='examine'),
    url(r'^home/', ReleaseListView.as_view(), name='release_list'),
    url(r'^password/', ModifyPasswordView.as_view(), name='modify_password'),
    url(r'^recharge/', RechargeView.as_view(), name='racharge')
]
