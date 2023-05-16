from django.contrib import admin
from .models import Customer,Product,Orders,Feedback

# Register your models here.
from .models import*
from .models import Produit
admin.site.register(Produit)
from .models import Categorie
admin.site.register(Categorie)
from .models import Fournisseur
admin.site.register(Fournisseur)
from .models import Commande
admin.site.register(Commande)
from .models import ProduitNC
admin.site.register(ProduitNC)

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Orders, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
# Register your models here.
