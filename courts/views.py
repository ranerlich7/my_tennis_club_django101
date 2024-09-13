from django.shortcuts import redirect, render

from courts.models import Court

def courts(request):
  courts = Court.objects.all()
  context = {
    'courts': courts,
  }
  return render(request, "all_courts.html", context)


def reserve(request, id):
  court = Court.objects.get(id=id)
  court.is_occupied = True
  court.save()
  return redirect('/courts/')
