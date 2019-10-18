from django.shortcuts import render
from datetime import datetime
from . import muj_modul

hodina=datetime.now().strftime("%H")
den_vtydnu=datetime.now().isoweekday()

def index(request):
    vysledek=muj_modul.otevreno(den_vtydnu,hodina)
    vysledek1=muj_modul.otevreno_den(den_vtydnu)
    return render(request, "moviebook/index.html", dict(vysledek=vysledek,vysledek1=vysledek1))