# Generated by Django 3.1.6 on 2021-02-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0013_auto_20210216_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialaccountslinks',
            name='linkdin',
        ),
        migrations.AddField(
            model_name='socialaccountslinks',
            name='linkedin',
            field=models.URLField(default='https://linkedin.com/in/?*Defautl*', verbose_name='Linkedin'),
        ),
    ]
