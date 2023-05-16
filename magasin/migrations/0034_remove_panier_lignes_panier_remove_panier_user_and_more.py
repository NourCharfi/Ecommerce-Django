# Generated by Django 4.1.7 on 2023-05-02 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("magasin", "0033_remove_lignepanier_panier_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="panier", name="lignes_panier",),
        migrations.RemoveField(model_name="panier", name="user",),
        migrations.AddField(
            model_name="panier",
            name="client",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="panier",
            name="produits",
            field=models.ManyToManyField(blank=True, to="magasin.produit"),
        ),
        migrations.AddField(
            model_name="panier",
            name="total",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.DeleteModel(name="LignePanier",),
    ]
