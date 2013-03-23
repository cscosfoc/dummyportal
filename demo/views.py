from django.shortcuts import render
from dummy.demo.models import Building, Location
from random import sample

def Index(request):
    r_id = sample(xrange(1, 6), 3)
    b_fil = Building.objects.filter(id__in=r_id)
    context = {
            'b_fil': b_fil,
            }

    return render(request, 'demo/index.html', context)

def Index_Location(request, locationslug):
    locationslug = Location.objects.get(slug=locationslug)
    buildings = locationslug.building_set.all()
    context = { 'buildings': buildings }

    return render(request, 'demo/location.html', context)