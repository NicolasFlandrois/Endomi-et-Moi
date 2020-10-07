from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from rest_framework.views import APIView
from rest_framework.response import Response

# from django.db import connection
# import pandas as pd

from trackers.models import PainSymptom
from django_pandas.io import read_frame


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts/chart.html', {'title': 'Mon Graphique'})


class ChartData(LoginRequiredMixin, UserPassesTestMixin, APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        pain_qs = PainSymptom.objects.filter(
            user=self.request.user).order_by('-date_added')

        pain_df = read_frame(pain_qs)
        print(pain_df)
        labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [120, 130, 140, 150, 160, 170]
        data = {
            'labels': labels,
            'default': default_items
        }

        return Response(data)

    def test_func(self):
        if self.request.user:
            return True
        return False
