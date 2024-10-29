# Generated by Django 5.1.2 on 2024-10-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('date_publication', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
