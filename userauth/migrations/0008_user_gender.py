# Generated by Django 5.1.3 on 2024-12-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0007_alter_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]