from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})

def about_me(request):
    print("Rendering about me")
    return render(request, "about_me.html", {})

def contact_me(request):
    print("Rendering contact me")
    return render(request, "contact_me.html", {})
