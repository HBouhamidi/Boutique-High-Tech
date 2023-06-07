from django.shortcuts import render, get_object_or_404
from .models import Produit, Commande, ElementCommande



def post_list(request):
    produits = Produit.objects.order_by('prix')
    return render(request, 'blog/post_list.html', {'produits': produits})
def post_detail(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    return render(request, 'blog/post_detail.html', {'produit': produit})

