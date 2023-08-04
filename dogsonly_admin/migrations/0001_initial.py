# Generated by Django 3.2.9 on 2022-03-13 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_email', models.EmailField(max_length=254, unique=True)),
                ('contact_sub', models.CharField(max_length=100)),
                ('contact_desc', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
        migrations.CreateModel(
            name='offers',
            fields=[
                ('offer_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('discount_amt', models.CharField(max_length=150)),
                ('offer_desc', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'offers',
            },
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=13)),
                ('order_date', models.DateField()),
                ('order_status', models.CharField(max_length=20)),
                ('total_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=300)),
                ('contact', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('user_date', models.DateField(null=True)),
                ('role_id', models.IntegerField()),
                ('otp', models.CharField(max_length=10, null=True)),
                ('otp_used', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('subcategory_id', models.AutoField(primary_key=True, serialize=False)),
                ('subcategory_name', models.CharField(max_length=20)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.category')),
            ],
            options={
                'db_table': 'subcategory',
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_name', models.CharField(max_length=20)),
                ('service_desc', models.CharField(max_length=300)),
                ('service_duration', models.IntegerField()),
                ('service_price', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.user')),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.FloatField()),
                ('product_desc', models.CharField(max_length=300)),
                ('product_image', models.CharField(max_length=200)),
                ('product_quantity', models.IntegerField()),
                ('offer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.offers')),
                ('subcategory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.subcategory')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_amount', models.IntegerField()),
                ('payment_status', models.CharField(max_length=20)),
                ('payment_date', models.DateField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.order')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='orderdetails',
            fields=[
                ('order_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_quantity', models.IntegerField()),
                ('product_price', models.FloatField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.product')),
            ],
            options={
                'db_table': 'order_detail',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.user'),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback_date', models.DateField()),
                ('feedback_desc', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.user')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('cart_date', models.DateField()),
                ('cart_qty', models.IntegerField()),
                ('total_amt', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogsonly_admin.user')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
