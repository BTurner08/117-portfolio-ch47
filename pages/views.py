from django.shortcuts import render
from .forms import ContactForm

def about_view(request):
    return render(request, 'pages/about.html')

def contact_views(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print("POST...")
    else:
        print("GET...")
    form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})