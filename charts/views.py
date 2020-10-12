from django.contrib import auth
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from trackers.models import PainSymptom
from django.conf import settings
from sqlalchemy import create_engine
from datetime import datetime


class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts/chart.html', {'title': 'Mon Graphique'})


class ChartData(LoginRequiredMixin, UserPassesTestMixin, APIView):
    authentication_classes = []
    permission_classes = []

    def connect(self):
        """Connect Python to the MySQL database with: 'name variable' """

        username = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']
        host = settings.DATABASES['default']['HOST']
        port = settings.DATABASES['default']['PORT']

        engine = create_engine(
            f'mysql+pymysql://{username}:{password}@{host}/\
{database_name}?host={host}?port={port}',
            echo=False, encoding='utf8', pool_recycle=60000,
            pool_pre_ping=True)

        return engine

    def get(self, request, format=None):
        pain_qs = PainSymptom.objects.all()
        user = auth.get_user(request)
        engine = self.connect()

        all_pain_df = pd.read_sql('trackers_painsymptom', engine)
        user_pain_df = all_pain_df[(all_pain_df.user_id == user.id)]

        df = pd.DataFrame()

        df['year'] = pd.DatetimeIndex(user_pain_df['date_day']).year
        df['month'] = pd.DatetimeIndex(user_pain_df['date_day']).month
        df['day'] = pd.DatetimeIndex(user_pain_df['date_day']).day
        print(df)
        print(df.dtypes)

        print(user_pain_df['date_day'])
        tmp_timestamp = user_pain_df['date_day'].values.tolist()
        print(tmp_timestamp)
        timestamp = [n // 1000000 for n in tmp_timestamp]
        # Format : 1602028800000 ms
        print(timestamp)

        data = {
            'timestamp': timestamp,
            'intensity_y': user_pain_df['intensity'].values.tolist(),
        }

        return Response(data)

    def test_func(self):
        if self.request.user:
            return True
        return False
