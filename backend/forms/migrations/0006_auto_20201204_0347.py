# Generated by Django 3.1.3 on 2020-12-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_myuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
