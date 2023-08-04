from django.db import models


# Create your models here.


class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    user_date = models.DateField(null=True)
    role_id = models.IntegerField()
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField(null=True)

    class Meta:
        db_table = "user"


class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)

    class Meta:
        db_table = "category"


class subcategory(models.Model):
    subcategory_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=20)

    class Meta:
        db_table = "subcategory"


class offers(models.Model):
    offer_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    discount_amt = models.CharField(max_length=150)
    offer_desc = models.CharField(max_length=150)

    class Meta:
        db_table = "offers"


class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    subcategory_id = models.ForeignKey(subcategory, on_delete=models.CASCADE)
    offer_id = models.ForeignKey(offers, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField(null=False)
    product_desc = models.CharField(max_length=300)
    product_image = models.CharField(max_length=200)
    product_quantity = models.IntegerField(null=False)

    class Meta:
        db_table = "product"


class cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    cart_date = models.DateField()
    cart_qty = models.IntegerField()
    total_amt = models.IntegerField()

    class Meta:
        db_table = "cart"


class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=13)
    order_date = models.DateField(null=False)
    order_status = models.CharField(max_length=20)
    total_amount = models.IntegerField(null=False)
    payment_status = models.CharField(max_length=20)

    class Meta:
        db_table = "order"


class orderdetails(models.Model):
    order_detail_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    order_quantity = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)

    class Meta:
        db_table = "order_detail"


class service(models.Model):
    service_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=20)
    service_desc = models.CharField(max_length=300)
    service_duration = models.IntegerField()
    service_price = models.FloatField(null=False)

    class Meta:
        db_table = "service"

class feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    feedback_date = models.DateField(null=False)
    feedback_desc = models.CharField(max_length=200)
    rating = models.IntegerField()

    class Meta:
        db_table = "feedback"

class contactus(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=30)
    contact_email = models.EmailField(unique=True)
    contact_sub = models.CharField(max_length=100)
    contact_desc = models.CharField(max_length=300)

    class Meta:
        db_table = "contactus"

class payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    payment_amount = models.IntegerField(null=False)
    payment_status = models.CharField(max_length=20)
    payment_date = models.DateField(null=False)

    class Meta:
        db_table = "payment"