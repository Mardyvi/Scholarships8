# Generated by Django 4.1 on 2022-08-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrebeca', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'becas',
            },
        ),
    ]
