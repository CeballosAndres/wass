import datetime as dt
from accounts.models import Agenda, CatalogoDia


def resetAvailability():
    today = CatalogoDia.objects.get(nombre=dt.date.today().weekday())
    agendas = Agenda.objects.filter(dia=today)
    for agenda in agendas:
        agenda.disponible = True
        agenda.save()
