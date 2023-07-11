# Generated by Django 4.1.5 on 2023-07-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_card_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='İsim Soyisim')),
                ('text', models.TextField(verbose_name='Yorum')),
                ('date_now', models.DateTimeField(auto_now_add=True, verbose_name='Tarih - Saat')),
            ],
        ),
    ]
