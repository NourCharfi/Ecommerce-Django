# Generated by Django 4.1.7 on 2023-03-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("magasin", "0020_alter_produit_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produit",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="magasin/media/"),
        ),
    ]
