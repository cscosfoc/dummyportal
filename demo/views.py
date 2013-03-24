from django.shortcuts import render
from dummy.demo.models import Location

def Index(request):
    locs = Location.objects.all()[:4]
    hall = list()

    for loc in locs:
        hall.append(loc.building_set.all()[:1])

    context = {
            'hall': hall,
            }

    return render(request, 'demo/index.html', context)

def Index_Location(request, locationslug):
    locationslug = Location.objects.get(slug=locationslug)
    buildings = locationslug.building_set.all()
    context = { 'buildings': buildings }

    return render(request, 'demo/location.html', context)