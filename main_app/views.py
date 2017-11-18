from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
            'treasures' : treasures,
            }
    return render(request, 'index.html', context)


class Treasure(object):
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url


treasures = [
        Treasure("Golden Nugget" , 500.00 , "Gold"   , "Curly's Creek , NM",
                "images/treasuregram-brand-gold-nugget.png"),
        Treasure("Fool's Gold"   , 0      , "Pyrite" , "Fool's Falls  , CO",
                "images/treasuregram-brand-fools-gold.png"),
        Treasure("Coffee Can"    , 25.00  , "Aluminum"    , "Acme   , CA",
                "images/treasuregram-brand-coffee-can.png")
        ]
