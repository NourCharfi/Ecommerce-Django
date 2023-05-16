
from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Produit(models.Model):
    catégorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, null=True)
    TYPE_CHOICES=[  ('em','emballé'),
                    ('fr','Frais'),
                    ('cs','Conserve')]
    
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img =models.ImageField(upload_to='media/', null=True, blank=True)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.libellé+","+self.description+","+str(self.prix)+","+self.type

class Categorie(models.Model):
    TYPE_CHOICES=[
    ('APPLE','APPLE'), ('DELL','DELL'),
    ('OPPO','OPPO'), ('SAMSUNG','SAMSUNG')
    ]

    name=models.CharField(max_length=50,default='APPLE',choices=TYPE_CHOICES)
    def __str__(self):
        return self.name
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100,null=True)
    adresse=models.TextField(null=True)
    email=models.EmailField(null=True)
    telephone=models.CharField(max_length=8,null=True)
    logo =models.ImageField(upload_to='media/', null=True, blank=True)
    def __str__(self):
        return (self.nom+','+self.adresse+','+self.email+','+self.telephone)
class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    nom_client = models.CharField(max_length=100,default="")
    adresse_livraison = models.CharField(max_length=200,default="")
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField(Produit, related_name='produits')

    def __str__(self):
        return str(self.dateCde) + ' - ' + str(self.totalCde)

    def get_produits_info(self):
    
        return [(p.libellé, p.prix,p.qte) for p in self.produits.all()]



class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    
    def __str__(self):
        return "objet ProduitNC:%s"%(self.Duree_garantie)
    



from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    catégorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, null=True)
    TYPE_CHOICES=[  ('em','emballé'),
                    ('fr','Frais'),
                    ('cs','Conserve')]
    name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='product_image/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    def __str__(self):
        return self.name


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
