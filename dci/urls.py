from django.urls import path
from dci.views import index

urlpatterns = [

    path('', index)

]