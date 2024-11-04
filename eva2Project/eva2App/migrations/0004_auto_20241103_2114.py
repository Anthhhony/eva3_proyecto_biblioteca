# Generated by Django 3.2 on 2024-11-04 00:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eva2App', '0003_auto_20241103_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator('El correo ingresado no es válido, compruebe el ejemplo: correoejemplo@gmail.com')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message='No puede tener una edad con más de 3 dígitos.', regex='^\\d{1,3}$')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='Inserte un rut válido (ejemplo: xx.xxx.xxx-x)', regex='^\\d{1,2}\\.\\d{3}\\.\\d{3}-[0-9Kk]$')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message='Favor ingresar un número de teléfono adecuado (ejemplo: +56912345678)', regex='^\\d{9,10}$')]),
        ),
        migrations.AlterField(
            model_name='libro',
            name='n_paginas',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(49)]),
        ),
        migrations.AlterField(
            model_name='libro',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='libro',
            name='stock',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]