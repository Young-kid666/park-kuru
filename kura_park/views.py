from django.shortcuts import render, get_object_or_404

def home_view(request):
    context = {}
    return render(request, 'kura_park/index.html', context)

def park_view(request):
    return render(request, 'kura_park/park.html')

def museum_view(request):
    return render(request, 'kura_park/museum.html')

def temple_view(request):
    return render(request, 'kura_park/temple.html')

def thermal_view(request):
    return render(request, 'kura_park/thermal.html')

def about_view(request):
    return render(request, 'kura_park/about.html')

def map_view(request):
    return render(request, 'kura_park/map.html')

def contacts_view(request):
    return render(request, 'kura_park/contacts.html')

def old_oak_view(request):
    return render(request, 'kura_park/old_oak.html')