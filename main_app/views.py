from django.shortcuts import render
from .models import Treasure

# Create your views here.
def index(request):
    # Here we need to get all of Treasure's objects
    treasures = Treasure.objects.all()
    context = {
            'treasures' : treasures,
            }
    return render(request, 'index.html', context)


def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure' : treasure})

