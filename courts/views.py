from django.shortcuts import get_object_or_404, redirect, render

from courts.models import Court
from members.models import Member

def courts(request):
  courts = Court.objects.all()
  context = {
    'courts': courts,
  }
  return render(request, "all_courts.html", context)



def reserve(request, id):
    if request.method == 'POST':
        court = get_object_or_404(Court, id=id)
        
        # Extract member names from the POST request
        member1 = request.POST.get('member1')
        member2 = request.POST.get('member2')
        print(f"reserving for members:{member1}, {member2}")
        # Update court information
        court.is_occupied = True
        # catch this court by member1 and member2
        
        member1_obj = Member.objects.get(id=member1)
        member2_obj = Member.objects.get(id=member2)

        member1_obj.court = court
        member2_obj.court = court
        member1_obj.save()
        member2_obj.save()
        court.save()        

    return redirect('/courts/')
    

