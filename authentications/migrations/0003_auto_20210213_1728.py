# Generated by Django 2.2.17 on 2021-02-13 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0002_auto_20210213_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
