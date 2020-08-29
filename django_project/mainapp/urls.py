from django.urls import path
from mainapp.views import IndexListView

app_name = 'mainapp'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
]
