from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm

def gallery_view(request):
    images = Image.objects.all().order_by('-created_at')
    return render(request, 'gallery/gallery.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:gallery')
    else:
        form = ImageForm()
    return render(request, 'gallery/upload.html', {'form': form})

def table_view(request):
    images = Image.objects.all().order_by('id')
    return render(request, 'gallery/table.html', {'images': images})
