# Generated by Django 5.1.6 on 2025-02-22 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noapp', '0003_comment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Noname', max_length=100)),
                ('text', models.CharField(max_length=300)),
                ('mail', models.CharField(max_length=50)),
            ],
        ),
    ]
