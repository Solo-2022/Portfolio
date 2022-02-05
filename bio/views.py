from django.shortcuts import render

# Create your views here.
def bio_page(request):
    return render(request, 'bio_page.html')