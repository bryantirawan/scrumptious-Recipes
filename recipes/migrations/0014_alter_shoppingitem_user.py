# Generated by Django 4.0.3 on 2022-04-28 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0013_alter_shoppingitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
