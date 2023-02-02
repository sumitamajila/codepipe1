from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import CertificationDetailsForm
from .models import CertificationDetails
# Create your views here.


def welcome(request):
    #return HttpResponse("<h1>welcome to certification module or app</h1>")
     return render(request, 'welcome.html')
def create(request):

    if request.method == 'POST':
        form = CertificationDetailsForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("read")

    form = CertificationDetailsForm()
    # first_name = request.POST.get('first_name', 'arnab')
    # last_name = request.POST.get('last_name', 'joshi')
    return render(request, 'create.html', {'form': form})

def read(request):
  data = CertificationDetails.objects.all()
  #data = CertificationDetails.objects.filter(status=True)
  return render(request, 'read.html', {'records': data})


def update(request, id):
    currentRecord = get_object_or_404(CertificationDetails, pk=id)
    if request.method == 'POST':
        form = CertificationDetailsForm(request.POST, instance=currentRecord)
        if form.is_valid():
            form.save()

            return redirect("read")
    form = CertificationDetailsForm(instance=currentRecord)
    return render(request, 'create.html', {'form': form, 'update': True})

    #return HttpResponse(f"<h1>i am update page, and i am updating {id} record.</h1>")

def delete(request, id):
    currentRecord = get_object_or_404(CertificationDetails, pk=id)
    currentRecord.status = False
    currentRecord.save()
   # CertificationDetails.objects.get(pk=id).delete()
    return redirect("read")




   # return HttpResponse("<h1>i am delete page</h1>")
