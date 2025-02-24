# Generated by Django 5.0.6 on 2025-02-21 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vintage_watch_app', '0002_seller_data_alter_product_payment_method_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='sign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('email_add', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='watch_type',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], default='men', max_length=10),
        ),
        migrations.AlterField(
            model_name='seller_data',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='seller_data',
            name='payment_type',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('PayPal', 'PayPal'), ('Gpay', 'Gpay')], default='Credit Card', max_length=50),
        ),
        migrations.AlterField(
            model_name='seller_data',
            name='return_policy',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=50),
        ),
        migrations.AlterField(
            model_name='seller_data',
            name='watch_type',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], default='Men', max_length=50),
        ),
    ]
