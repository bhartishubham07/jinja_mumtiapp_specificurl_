from django.shortcuts import render

# Create your views here.

def Dhoni(request):
    D = {'name' : 'M.S. DHONI', 'age' : 39}
    return render(request, 'Dhoni.html', context=D)