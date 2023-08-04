from django.contrib import admin
from django.urls import path
from dogsonly_client import client_views

urlpatterns = [
    path('index/', client_views.index),
    path('client_register/', client_views.client_register),
    path('client_login/', client_views.client_login),
    path('client_logout/', client_views.client_logout),
    path('client_lost_password/', client_views.client_lostpassword),
    path('client_otp/', client_views.client_sendotp),
    path('client_reset/', client_views.client_setpassword),
    path('client_profile/', client_views.client_profile),
    path('client_updatepro/', client_views.client_updateprofile),
    path('client_contactus/', client_views.client_contactus),
    path('client_header_menu/', client_views.load_menu),
    path('client_shop/', client_views.client_shop),
    path('client_shopdetails/<int:id>', client_views.client_shopdetails),
    path('client_feedback/', client_views.client_feedback),
    path('show_cart/', client_views.client_cart),
    path('client_cart/<int:id>', client_views.insert_cart),
    path('clear_cart/', client_views.clear_cart),
    path('delete_cart/<int:id>', client_views.delete_cart),
    path('checkout/', client_views.checkout),
    path('place_order/<int:total>', client_views.place_order),
    path('allorders/', client_views.client_allorders),
    path('search_product/', client_views.autosuggest, name='pro_search'),
    path('search2/', client_views.search),
]
