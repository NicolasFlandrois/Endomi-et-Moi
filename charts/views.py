from django.shortcuts import render

# Create your views here.

def chart(request):
    return render(request, 'charts/chart.html', {'title': 'Mon Graphique'})
