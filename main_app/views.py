from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
            'treasures' : treasures,
            }
    return render(request, 'index.html', context)


class Treasure(object):
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location


treasures = [
        Treasure("Golden Nugget" , 500.00 , "gold"   , "Curly's Creek , NM"),
        Treasure("Fool's Gold"   , 0      , "pyrite" , "Fool's Falls  , CO"),
        Treasure("Coffee Can"    , 20.00  , "tin"    , "Acme          , CA")
        ]
