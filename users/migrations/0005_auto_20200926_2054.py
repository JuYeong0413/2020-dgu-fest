# Generated by Django 3.0.6 on 2020-09-26 20:54

from django.db import migrations, models
import users.validation


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200926_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(null=True, unique=True, validators=[users.validation.validate_phonenumber], verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1, null=True),
        ),
    ]
