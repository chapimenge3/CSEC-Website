# Generated by Django 3.1.6 on 2021-02-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0007_auto_20210214_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='division',
            field=models.CharField(blank=True, choices=[('cpd', 'Competitive Programming'), ('development', 'Development'), ('capacity', 'Capacity Building'), ('unassigned', 'Unassigned')], default='unassigned', max_length=20, null=True),
        ),
    ]
