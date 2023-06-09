# Generated by Django 4.1.7 on 2023-05-01 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("magasin", "0031_commande_adresse_livraison_commande_nom_client_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="LignePanier",
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
                ("quantite", models.IntegerField(default=1)),
                ("prix_unitaire", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Panier",
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
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "total",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "produits",
                    models.ManyToManyField(
                        through="magasin.LignePanier", to="magasin.produit"
                    ),
                ),
                (
                    "utilisateur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="lignepanier",
            name="panier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="magasin.panier"
            ),
        ),
        migrations.AddField(
            model_name="lignepanier",
            name="produit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="magasin.produit"
            ),
        ),
    ]
