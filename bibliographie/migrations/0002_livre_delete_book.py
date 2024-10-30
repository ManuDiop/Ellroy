# Generated by Django 5.1.2 on 2024-10-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliographie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('date_publication', models.DateField()),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('couverture', models.ImageField(blank=True, null=True, upload_to='couvertures/')),
                ('synopsis', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]