# Generated by Django 4.2.1 on 2023-05-07 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("magasin", "0041_product_atégorie_product_fournisseur_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product", old_name="atégorie", new_name="catégorie",
        ),
    ]
