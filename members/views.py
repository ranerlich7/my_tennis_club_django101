from django.shortcuts import render
from members.models import Member

def members(request):
  mymembers = Member.objects.all()
  context = {
    'mymembers': mymembers,
    'name': 'RAN'
  }
  return render(request, "all_members.html", context)

def courts(request):
  return render(request, "my_courts.html")

def details(request, id):
  mymember = Member.objects.get(id=id)
  context = {
    'mymember': mymember,
  }
  return render(request, "details.html", context)
