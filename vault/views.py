from django.shortcuts import render
from .models import PDFDocument

def index(request):
    pdfs = PDFDocument.objects.prefetch_related('tags').all()
    return render(request, 'vault/index.html', {
        'pdfs': pdfs,
    })

def about(request):
    contributors = [
        "JuventusFans112 (Dummy Test)",
        "naufalkebab (Full-Stack Developer & Security)",
        "( Need UI/UX )",

    ]
    description = "Typovault, a community-driven website, serves as a central repository for the scattered documents and knowledge surrounding typology. Is built with Django for its robust backend capabilities, scalability, and extensive library ecosystem, ensuring a reliable and feature-rich platform for this central repository of typographic knowledge."
    changelogs = [

    {"version": "1.3 Beta", "changes": "UI adjustments and performance improvements."},
    {"version": "1.2 Beta", "changes": "fixed several critical UI bugs, Enhanced security measures "},
    {"version": "1.1 Alpha", "changes": "Implemented a more intuitive navigation system."},
    {"version": "1.0 Alpha", "changes": "Implemented user role management."}


    ]
    return render(request, 'vault/about.html', {
        'contributors': contributors,
        'description': description,
        'changelogs': changelogs,
    })

def contact(request):
    contact_info = {
        'name': 'Naufal Kebab',
        'email': 'naufalarpharazon@gmail.com',
        'phone': '+62 831 5064 5824',
        'linkedin': 'https://www.facebook.com/arpharazons',
        'quora': 'https://id.quora.com/profile/Naufal-285',
        'facebook': 'https://www.facebook.com/arpharazons',
    }
    return render(request, 'vault/contact.html', {
        'contact_info': contact_info,
    })
