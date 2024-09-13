from django.shortcuts import redirect, render
from members.models import Court, Member

def members(request):
  mymembers = Member.objects.all()
  context = {
    'mymembers': mymembers,
    'name': 'RAN'
  }
  return render(request, "all_members.html", context)


def details(request, id):
  mymember = Member.objects.get(id=id)
  context = {
    'mymember': mymember,
  }
  return render(request, "details.html", context)


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
