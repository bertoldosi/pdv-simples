from django.contrib import admin
from django.urls import path
from caixa.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Pdv.as_view()),
]
