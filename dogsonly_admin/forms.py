from django import forms
from dogsonly_admin.models import user, category, subcategory, product, offers, orderdetails, order, feedback, service, payment, contactus, cart


class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = ["name", "gender", "address", "contact", "email", "password", "user_date", "role_id"]

class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = ["category_name"]

class subcategoryform(forms.ModelForm):
    class Meta:
        model = subcategory
        fields = [ "category_id", "subcategory_name"]

class offersform(forms.ModelForm):
    class Meta:
        model = offers
        fields = ["start_date", "end_date", "discount_amt", "offer_desc"]

class productform(forms.ModelForm):
    product_image = forms.FileField()
    class Meta:
        model = product
        fields = ["subcategory_id", "offer_id", "product_name", "product_price", "product_desc", "product_quantity", "product_image"]

class cartform(forms.ModelForm):
    class Meta:
        model = cart
        fields = ["product_id","user_id","cart_date","cart_qty","total_amt"]

class orderform(forms.ModelForm):
    class Meta:
        model = order
        fields = ["user_id", "address", "contact",  "order_date", "order_status", "total_amount"]

class orderdetailsform(forms.ModelForm):
    class Meta:
        model = orderdetails
        fields = ["product_id", "order_id", "order_quantity", "amount"]

class serviceform(forms.ModelForm):
    class Meta:
        model = service
        fields = ["user_id", "service_name", "service_desc", "service_duration", "service_price"]

class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ["user_id", "product_id", "feedback_date", "feedback_desc"]

class paymentform(forms.ModelForm):
            class Meta:
                model = payment
                fields = ["order_id", "payment_amount", "payment_status", "payment_date"]

class contactusform(forms.ModelForm):
    class Meta:
        model = contactus
        fields = ["contact_name", "contact_email", "contact_sub", "contact_desc"]



