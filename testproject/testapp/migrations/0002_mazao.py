# Generated by Django 4.1.1 on 2022-09-24 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mazao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jinalamazao', models.CharField(max_length=50)),
                ('jinalawilaya', models.ManyToManyField(to='testapp.wilaya')),
            ],
        ),
    ]