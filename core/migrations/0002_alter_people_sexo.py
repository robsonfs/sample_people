# Generated by Django 3.2.7 on 2021-09-29 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='sexo',
            field=models.CharField(
                choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=10),
        ),
    ]
