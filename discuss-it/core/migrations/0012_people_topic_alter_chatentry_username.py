# Generated by Django 4.1.4 on 2023-01-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_chatentry_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='topic',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='chatentry',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]