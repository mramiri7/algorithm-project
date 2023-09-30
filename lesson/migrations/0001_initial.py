# Generated by Django 4.1 on 2023-08-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('handouts', models.FileField(blank=True, null=True, upload_to='handouts/')),
                ('videos', models.URLField(blank=True)),
            ],
        ),
    ]