"""dogsonly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from dogsonly_admin import views
from django.conf.urls import url
from dogsonly_admin.views import HomeView, ProjectChart


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('category_table/',views.category_table),
    path('user_table/',views.user_table),
    path('subcategory_table/',views.subcategory_table),
    path('offers_table/',views.offer_table),
    path('product_table/',views.product_table),
    path('cart_table/', views.cart_table),
    path('order_table/',views.order_table),
    path('orderdetails_table/', views.orderdetails_table),
    path('service_table/', views.service_table),
    path('feedback_table/', views.feedback_table),
    path('payment_table/', views.payment_table),
    path('contactus_table/', views.contactus_table),

    path('delete_category/<int:id>',views.delete_category),
    path('delete_subcategory/<int:id>', views.delete_subcategory),
    path('delete_offers/<int:id>', views.delete_offers),
    path('delete_product/<int:id>', views.delete_product),
    path('delete_service/<int:id>', views.delete_service),
    path('delete_payment/<int:id>', views.delete_payment),
    path('delete_contactus/<int:id>', views.delete_contactus),
    path('delete_order/<int:id>', views.delete_order),


    path('insert_category/',views.insertcategory),
    path('insert_subcategory/',views.insertsubcategory),
    path('insert_offers/',views.insert_offer),
    path('insert_product/',views.insertproduct),
    path('insert_order/', views.insertorder),
    path('insert_order_details/', views.insertorderdetails),
    path('insert_service/', views.insertservice),
    path('insert_feedback/', views.insert_Feedback),
    path('insert_contact/', views.insertcontact),
    path('insert_payment/', views.insertpayment),


    path('select_category/<int:id>',views.select_category),
    path('update_category/<int:id>',views.update_Category),
    path('select_subcategory/<int:id>', views.select_subcategory),
    path('update_subcategory/<int:id>', views.update_subcategory),
    path('select_offer/<int:id>', views.select_offers),
    path('update_offer/<int:id>', views.update_offers),
    path('select_product/<int:id>', views.select_product),
    path('update_product/<int:id>', views.update_product),
    path('select_service/<int:id>', views.select_service),
    path('update_service/<int:id>', views.update_service),

    path('dashboard/',views.dashboard),
    url(r'charthome', HomeView.as_view(), name='home'),
    url(r'^api/chart/data/$', ProjectChart.as_view(), name="api-data"),

    path('login/',views.login),
    path('logout/',views.logout),
    path('forget_password/',views.forget_password),
    path('send_otp/',views.sendotp),
    path('reset/',views.set_password),
    path('profile/',views.profile),
    path('update_profile/',views.update_profile),
    path('accepted_order/<int:id>', views.accept_order),
    path('rejected_order/<int:id>', views.rejected_order),

    path('client/', include('dogsonly_client.client_urls')),



]
