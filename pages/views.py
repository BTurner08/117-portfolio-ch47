from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

def about_view(request):
    return render(request, 'pages/about.html')

def contact_views(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print("POST...")
        
        if form.is_valid():
            name = form. cleaned_data["name"]
            email_from = form. cleaned_data["email"]
            message = form.cleaned_data["message"]

            send_mail(
                "Email from " + name, message, email_from, ["airblake2016@gmail.com"]
            )
        else:
            print("Invalid Form")

        print("POST ... ")
    else:
        print("GET...")
        form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})