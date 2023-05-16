# Generated by Django 4.1.7 on 2023-05-02 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("magasin", "0035_remove_panier_produits_remove_panier_total_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="panier",
            options={"verbose_name": "Panier", "verbose_name_plural": "Paniers"},
        ),
        migrations.RemoveField(model_name="panier", name="client",),
        migrations.AddField(
            model_name="panier",
            name="utilisateur",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="panier",
            name="produit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="magasin.produit",
            ),
        ),
        migrations.AlterField(
            model_name="panier",
            name="quantite",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
