# Generated by Django 4.0.6 on 2022-09-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_category_subcategory_subcategoryinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
