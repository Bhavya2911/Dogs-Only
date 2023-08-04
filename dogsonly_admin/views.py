import random
from django.contrib import messages
from django.core.mail import send_mail
from dogsonly_admin.models import category, user, subcategory, offers, product, orderdetails, order, service, feedback, \
    payment, contactus, cart
from django.shortcuts import render, redirect
import sys
from dogsonly_admin.forms import categoryform, subcategoryform, offersform, productform, orderform, orderdetailsform, \
    serviceform, feedbackform, paymentform, contactusform, userform, cartform
from dogsonly import settings
from dogsonly_admin.functions import handle_uploaded_file
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View


# Create your views here.
# -----------------------------------show table------------------------------------
def user_table(request):
    emp = user.objects.all()
    return render(request, "table_user.html", {'user': emp})


def category_table(request):
    emp = category.objects.all()
    return render(request, "table_category.html", {'category': emp})


def subcategory_table(request):
    emp = subcategory.objects.all()
    return render(request, "table_subcategory.html", {'subcategory': emp})


def offer_table(request):
    emp = offers.objects.all()
    return render(request, "table_offer.html", {'offer': emp})


def product_table(request):
    emp = product.objects.all()
    return render(request, "table_product.html", {'product': emp})


def cart_table(request):
    emp = cart.objects.all()
    return render(request, "table_cart.html", {'cart': emp})


def order_table(request):
    emp = order.objects.all()
    return render(request, "table_order.html", {'order': emp})


def orderdetails_table(request):
    emp = orderdetails.objects.all()
    return render(request, "table_orderdetails.html", {'orderdetails': emp})


def service_table(request):
    emp = service.objects.all()
    return render(request, "table_service.html", {'service': emp})


def feedback_table(request):
    emp = feedback.objects.all()
    return render(request, "table_feedback.html", {'feedback': emp})


def payment_table(request):
    emp = payment.objects.all()
    return render(request, "table_payment.html", {'payment': emp})


def contactus_table(request):
    emp = contactus.objects.all()
    return render(request, "table_contactus.html", {'contactus': emp})


# -----------------------------------show table------------------------------------

# ------------------------------delete fileds -------------------------------------

def delete_category(request, id):
    cat = category.objects.get(category_id=id)
    cat.delete()
    return redirect("/category_table")


def delete_subcategory(request, id):
    subcat = subcategory.objects.get(subcategory_id=id)
    subcat.delete()
    return redirect("/subcategory_table")


def delete_offers(request, id):
    offer = offers.objects.get(offer_id=id)
    offer.delete()
    return redirect("/offers_table")


def delete_product(request, id):
    prod = product.objects.get(product_id=id)
    prod.delete()
    return redirect("/product_table")


def delete_service(request, id):
    ser = service.objects.get(service_id=id)
    ser.delete()
    return redirect("/service_table")


def delete_payment(request, id):
    pay = payment.objects.get(payment_id=id)
    pay.delete()
    return redirect("/payment_table")


def delete_contactus(request, id):
    con = contactus.objects.get(contact_id=id)
    con.delete()
    return redirect("/contactus_table")


def delete_order(request, id):
    ordr = order.objects.get(order_id=id)
    ordr.delete()
    return redirect("/order_table")


def delete_order_details(request, id):
    ordr_det = orderdetails.objects.get(order_detail_id=id)
    ordr_det.delete()
    return redirect("/orderdetails_table")


# ------------------------------delete fileds -------------------------------------

# -------------------------------insert fileds--------------------------------------
def insertcategory(request):
    if request.method == "POST":
        form = categoryform(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/category_table/')
            except:
                print("---------------", sys.exc_info())
    else:
        form = categoryform()

    return render(request, 'insert_category.html', {'form': form})


def insertsubcategory(request):
    category_records = category.objects.all()
    if request.method == "POST":
        form = subcategoryform(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/subcategory_table/')
            except:
                print("---------------", sys.exc_info())
    else:
        form = subcategoryform()

    return render(request, 'insert_subcategory.html', {'form': form, 'category': category_records})


def insert_offer(request):
    if request.method == "POST":
        form = offersform(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/offers_table/')
            except:
                print("---------------", sys.exc_info())
    else:
        form = offersform()

    return render(request, 'insert_offers.html', {'form': form})


def insertproduct(request):
    subcategory_records = subcategory.objects.all()
    offers_records = offers.objects.all()
    if request.method == "POST":
        form = productform(request.POST, request.FILES)
        print("=====", request.POST.get('product_image'))
        print("-------------", form.errors)

        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['product_image'])
                form.save()
                return redirect('/product_table/')
            except:
                print("---------------", sys.exc_info())
    else:
        form = productform()

    return render(request, 'insert_product.html',
                  {'form': form, 'subcategory': subcategory_records, 'offers': offers_records})


def insertorder(request):
    user_records = user.objects.all()
    if request.method == "POST":
        form = orderform(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/order_table/')
            except:
                print("---------------", sys.exc_info())
    else:
        form = orderform()

    return render(request, 'insert_order.html', {'form': form, 'user': user_records})


def insertorderdetails(request):
    product_record = product.objects.all()
    order_records = order.objects.all()
    if request.method == "POST":
        form = orderdetailsform(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/orderdetails_table')
            except:
                print("---------------", sys.exc_info())
    else:
        form = orderdetailsform()

    return render(request, 'insert_order_item.html', {'form': form, 'product': product_record, 'order': order_records})


def insertservice(request):
    user_records = user.objects.all()
    if request.method == "POST":
        form = serviceform(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/service_table/')
            except:
                print("---------------", sys.exc_info())
    else:
        form = serviceform()

    return render(request, 'insert_service.html', {'form': form, 'user': user_records})


def insert_Feedback(request):
    user_records = user.objects.all()
    product_record = product.objects.all()
    if request.method == "POST":
        form = feedbackform(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/feedback_table')
            except:
                print("---------------", sys.exc_info())
    else:
        form = categoryform()

    return render(request, 'insert_feedback.html', {'form': form, 'user': user_records, 'product': product_record})


def insertcontact(request):
    if request.method == "POST":
        form = contactusform(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/contactus_table/')
            except:
                print("---------------", sys.exc_info())
    else:
        form = contactusform()

    return render(request, 'insert_contact.html', {'form': form})


def insertpayment(request):
    ordr_records = order.objects.all()
    if request.method == "POST":
        form = paymentform(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/payment_table/')
            except:
                print("---------------", sys.exc_info())
    else:
        form = paymentform()

    return render(request, 'insert_payment.html', {'form': form, 'order': ordr_records})


# -------------------------------insert fields--------------------------------------

# -------------------------------update fields--------------------------------------

def select_category(request, id):
    cat = category.objects.get(category_id=id)
    return render(request, 'update_category.html', {'category': cat})


def update_Category(request, id):
    cat = category.objects.get(category_id=id)
    form = categoryform(request.POST, instance=cat)
    if form.is_valid():
        form.save()
        return redirect("/category_table")
    return render(request, 'update_category.html', {'category': cat})


def select_subcategory(request, id):
    subcat = subcategory.objects.get(subcategory_id=id)
    subat_records = category.objects.all()
    return render(request, 'update_subcategory.html', {'subcategory': subcat, 'category': subat_records})


def update_subcategory(request, id):
    subcat = subcategory.objects.get(subcategory_id=id)
    subat_records = category.objects.all()
    form = subcategoryform(request.POST, instance=subcat)
    if form.is_valid():
        form.save()
        return redirect("/subcategory_table")
    return render(request, 'update_subcategory.html', {'subcategory': subcat, 'category': subat_records})


def select_offers(request, id):
    ofr = offers.objects.get(offer_id=id)
    return render(request, 'update_offers.html', {'offer': ofr})


def update_offers(request, id):
    ofr = offers.objects.get(offer_id=id)
    form = offersform(request.POST, instance=ofr)
    if form.is_valid():
        form.save()
        return redirect("/offers_table")
    return render(request, 'update_offers.html', {'offer': ofr})


def select_product(request, id):
    pro = product.objects.get(product_id=id)
    subcat_records = subcategory.objects.all()
    ofr_records = offers.objects.all()
    return render(request, 'update_product.html',
                  {'product': pro, 'subcategory': subcat_records, 'offers': ofr_records})


def update_product(request, id):
    pro = product.objects.get(product_id=id)
    subcat_records = subcategory.objects.all()
    ofr_records = offers.objects.all()
    form = productform(request.POST, instance=pro)
    if form.is_valid():
        form.save()
        return redirect("/product_table")
    return render(request, 'update_product.html',
                  {'product': pro, 'subcategory': subcat_records, 'offers': ofr_records})


def select_service(request, id):
    ser = service.objects.get(service_id=id)
    user_records = user.objects.all()
    return render(request, 'update_service.html', {'service': ser, 'user': user_records})


def update_service(request, id):
    ser = service.objects.get(service_id=id)
    user_records = user.objects.all()
    form = serviceform(request.POST, instance=ser)
    if form.is_valid():
        form.save()
        return redirect("/service_table")
    return render(request, 'update_service.html', {'service': ser, 'user': user_records})


# -------------------------------update fields--------------------------------------

# -------------------------------dashboard,profile,chart--------------------------------------
def dashboard(request):
    ordr = order.objects.all()
    u = user.objects.all().count()
    o = order.objects.all().count()
    p = product.objects.all().count()
    f = feedback.objects.all().count()

    return render(request, "dashboard.html", {'order': ordr, 'user': u, 'ordr': o, 'product': p,'feedback':f})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class ProjectChart(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        cursor = connection.cursor()
        cursor.execute(
            '''SELECT product_id_id as id, sum(amount) as amount FROM order_detail i JOIN product p where i.product_id_id = p.product_id GROUP by product_id_id;''')
        qs = cursor.fetchall()

        labels = []
        default_items = []
        for item in qs:
            labels.append(item[0])
            default_items.append(item[1])
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


# -------------------------------dashboard,profile,chart--------------------------------------

# login
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = user.objects.filter(email=email, password=password, role_id=1).count()
        print("--------------", email, "---------", password)
        if val == 1:
            data = user.objects.filter(email=email, password=password, role_id=1)
            for item in data:
                request.session['admin_email'] = item.email
                request.session['admin_password'] = item.password
                request.session['admin_user_id'] = item.user_id
            if request.POST.get("remember"):  # remember :it's a checkbox name.(in html page)
                response = redirect("/dashboard/")
                response.set_cookie('cookie_admin_email', request.POST[
                    "email"])  # cemail is a key     #email : it's a textbox name (in html page)
                response.set_cookie('cookie_admin_password', request.POST[
                    "password"])  # cpass is a key       #password: it's a textbox name(in html page)
                return response
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid user name and password")
            return redirect('/login/')
    else:
        if request.COOKIES.get("cookie_admin_email"):
            return render(request, "login.html",
                          {'c_admin_email': request.COOKIES['cookie_admin_email'],
                           'c_admin_password': request.COOKIES[
                               'cookie_admin_password']})  # cookie1 and cookie2 are keys
        else:
            return render(request, "login.html")
        return render(request, "login.html")


def logout(request):
    # session for logout
    try:
        del request.session['admin_email']
        del request.session['admin_password']
        del request.session['admin_user_id']
        return redirect("/login/")
    except:
        pass
        return redirect("/login/")


# Forget
def forget_password(request):
    return render(request, 'forget_password.html')


# Sending OTP
def sendotp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['email']

    request.session['temail'] = e
    print("-------------", e)

    obj = user.objects.filter(email=e).count()

    if obj == 1:
        val = user.objects.filter(email=e).update(otp=otp1, otp_used=0)

        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'set_password.html')


# Reseting a password
def set_password(request):
    if request.method == "POST":

        T_otp = request.POST['OTP']
        T_pass = request.POST['pass']
        T_cpass = request.POST['rpass']

        if T_pass == T_cpass:
            e = request.session['temail']

            val = user.objects.filter(email=e, otp=T_otp, otp_used=0).count()

            if val == 1:
                user.objects.filter(email=e).update(otp_used=1, password=T_pass)
                return redirect("/login/")
            else:
                messages.error(request, "Invalid OTP")
                return render(request, "set_password.html")

        else:
            messages.error(request, "New password and Confirm password does not match ")
            return render(request, "set_password.html")

    else:
        return redirect("/forget_password")


# Edit Profile
def profile(request):
    a_id = request.session['admin_user_id']
    u = user.objects.get(user_id=a_id)
    register_date = u.user_date
    register = register_date.strftime("%Y-%m-%d")
    print("====", register_date)
    return render(request, "profile.html", {'ca': u, 'register': register})


def update_profile(request):
    a_id = request.session['admin_user_id']
    u = user.objects.get(user_id=a_id)
    form = userform(request.POST, instance=u)
    print("-------------", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/dashboard/")
        except:
            print("---------------", sys.exc_info())
    else:
        pass
    return render(request, "profile.html", {'ca': u})


def accept_order(request, id):
    o = order.objects.get(order_id=id)
    o.order_status = 1
    o.save()

    subject = "Order status"
    message = "Your order is confirmed"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [o.user_id.email, ]
    print("---- receiver ----", recipient_list)
    send_mail(subject, message, email_from, recipient_list)
    return redirect("/order_table/")


def rejected_order(request, id):
    o = order.objects.get(order_id=id)
    o.order_status = 2
    o.save()

    subject = "Order status"
    message = "Your order is rejected due to some technical issue. Please try again later."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [o.user_id.email, ]
    print("---- receiver ----", recipient_list)
    send_mail(subject, message, email_from, recipient_list)
    return redirect("/order_table/")
