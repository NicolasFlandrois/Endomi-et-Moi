from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts/chart.html', {'title': 'Mon Graphique'})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [120, 130, 140, 150, 160, 170]
        data = {
            'labels': labels,
            'default': default_items
        }

        return Response(data)
