# Generated by Django 4.1 on 2023-12-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallmon', '0005_alter_falltype_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fallhistory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='falltype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]