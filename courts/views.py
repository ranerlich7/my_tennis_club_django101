from django.shortcuts import render

from courts.models import Courts


def courts(request):
    courts = Courts.objects.all()
    context = {
        'courts': courts,
    }
    return render(request, "all_courts.html", context)
