from django.conf.urls import url
from UsersApp import views

urlpatterns=[
    url(r'^users/$',views.UserApi),
    url(r'^users/([0-9]+)$',views.UserApi),
    url(r'^companies/$',views.CompanyApi),
    url(r'^companies/([0-9]+)$',views.CompanyApi),
    url(r'^roles/$',views.RoleApi),
    url(r'^roles/([0-9]+)$',views.RoleApi)
]