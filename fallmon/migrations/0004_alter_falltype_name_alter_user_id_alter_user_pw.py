# Generated by Django 4.1 on 2023-12-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fallmon', '0003_alter_falltype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='falltype',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='pw',
            field=models.CharField(max_length=255),
        ),
    ]
