from django.urls import path, include
from CustomerApp import views
from django.urls import include, re_path



urlpatterns = [
    #url path for the account
    re_path(r'^account/$',views.AccountAPI),
    re_path(r'^account/([0-9]+)$',views.AccountAPI),

    #url path for the client
    re_path(r'^client/$',views.ClientAPI),
    re_path(r'^client/([0-9]+)$',views.ClientAPI),
]
