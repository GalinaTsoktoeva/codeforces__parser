from django.urls import path

from task.views import index

urlpatterns = [
    path('', index)
]
