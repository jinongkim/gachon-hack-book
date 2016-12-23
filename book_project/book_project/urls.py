"""book_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from hack_book import views


urlpatterns = [
#     url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='pages/index.html'), name='Index'),
    url(r'^login$', TemplateView.as_view(template_name='pages/login.html'), name='login'),
    # url(r'^user_check$', views.user_check, name='user_check'),
    # url(r'^login_user$', views.login_user, name='login_user'),
    url(r'^sign_in$', TemplateView.as_view(template_name='pages/sing_in.html'), name='sign_in'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^find_pw$', TemplateView.as_view(template_name='pages/find_pw.html'), name='find_pw'),
    url(r'^market$', TemplateView.as_view(template_name='pages/market_1.html'), name='market'),
    url(r'^report_center$', TemplateView.as_view(template_name='pages/report_center_1.html'), name='report_center'),
    url(r'^hope_book$', TemplateView.as_view(template_name='pages/hope_book_1.html'), name='hope_book'),
    url(r'^gong9$', TemplateView.as_view(template_name='pages/gong9_1.html'), name='gong9'),
    url(r'^major$', TemplateView.as_view(template_name='pages/major_1.html'), name='major'),
    url(r'^detail_book$', TemplateView.as_view(template_name='pages/detail_book_1.html'), name='detail_book'),
    url(r'^mypage_selling$', TemplateView.as_view(template_name='pages/mypage_selling_1.html'), name='mypage_selling'),
    url(r'^mypage_edit$', TemplateView.as_view(template_name='pages/mypage_edit_1.html'), name='mypage_edit'),
]
