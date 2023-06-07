from django.db import models


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    est_disponible = models.BooleanField(default=True)


class Commande(models.Model):
    nom_client = models.CharField(max_length=100)
    email_client = models.EmailField()
    date_commande = models.DateTimeField(auto_now_add=True)


class ElementCommande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)


from django.db import models

# Create your models here.
