# Generated by Django 3.1.6 on 2021-02-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0009_auto_20210216_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='+251911111111', max_length=50, verbose_name='Phone'),
        ),
    ]
