from django.shortcuts import render
from .models import Photo

# Create your views here.

def index(request):
    if request.method == 'POST':
        new_photo = Photo(file = request.FILES['img'])
        new_photo.save()

        context = {'new_url':str(new_photo.file.url)}    
        return render(request, 'index.html', context) 
    else:
        return render(request, 'index.html')