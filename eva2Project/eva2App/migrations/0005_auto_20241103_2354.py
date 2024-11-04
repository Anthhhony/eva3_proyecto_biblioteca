# Generated by Django 3.2 on 2024-11-04 02:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eva2App', '0004_auto_20241103_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='correo',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator('El correo ingresado no es válido, compruebe el ejemplo: correoejemplo@gmail.com')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message='Ingrese un número de teléfono adecuado (ejemplo: +56912345678)', regex='^\\d{9,10}$')]),
        ),
    ]
