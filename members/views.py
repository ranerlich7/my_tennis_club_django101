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
