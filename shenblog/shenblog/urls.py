"""shenblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from web import views

admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    url(r'^category/(\d+)/$',views.category,name="category"),
    #url(r'^category/2/',views.category_2),
    #url(r'^category/3/',views.category_3),
    url(r'^article/(\d+)/$',views.article_detail,name='article_detail'),
    url(r'^article/new/$',views.new_article,name='new_article'),
    url(r'^account/logout',views.account_logout,name='logout'),
    url(r'^account/login/',views.acc_login,name='login'),

    ]
