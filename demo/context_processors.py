from dummy.demo.models import Location

def root_locations(request):
    return {'root_locations': Location.objects.all()}