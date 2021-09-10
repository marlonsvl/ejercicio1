# Generated by Django 3.1.5 on 2021-09-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ValorCambio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('fecha', models.DateTimeField(verbose_name='fecha')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='valor')),
            ],
        ),
    ]
