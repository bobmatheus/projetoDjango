# Generated by Django 5.2.4 on 2025-07-12 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor_1h', models.DecimalField(decimal_places=2, max_digits=6)),
                ('valor_1h30', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
