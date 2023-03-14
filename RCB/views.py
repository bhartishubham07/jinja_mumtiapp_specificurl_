from django.shortcuts import render

# Create your views here.

def Virat(request):
    D = {'name' : 'Virat Kohli', 'age' : 32}
    return render(request, 'Virat.html', context=D)