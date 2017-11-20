from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

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
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        treasure = form.save(commit = False)
        treasure.user = request.user
        treasure.save()
    return HttpResponseRedirect('/')

def profile(request, username):
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(request, "profile.html",
                  {"username" : username,
                  "treasures" : treasures})


