from django.shortcuts import render

html_base = """
<h1>Mi web personal</h1>
<ul>
  <li><a href="">Inicio</a></li>
  <li><a href="about-me">Acerca de mi</a></li>
  <li><a href="portfolio">Portafolio</a></li>
  <li><a href="contact">Contacto</a></li>
</ul>
"""

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")