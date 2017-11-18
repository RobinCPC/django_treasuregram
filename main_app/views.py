from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm

# Create your views here.
def index(request):
    # Here we need to get all of Treasure's objects
    treasures = Treasure.objects.all()
    form = TreasureForm()
    context = {
            'treasures' : treasures,
            'form' : form,
            }
    return render(request, 'index.html', context)


def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'detail.html', {'treasure' : treasure})


def post_treasure(request):
    form = TreasureForm(request.POST)
    if form.is_valid():
        form.save(commit= True)
    return HttpResponseRedirect('/')

