# Generated by Django 4.1.7 on 2023-05-02 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("magasin", "0037_produit_stock"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContenuPanier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantite", models.PositiveIntegerField(default=1)),
                (
                    "panier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contenu",
                        to="magasin.panier",
                    ),
                ),
                (
                    "produit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="magasin.produit",
                    ),
                ),
            ],
        ),
    ]
