"""user profile urls
"""
from django.urls import path

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index')
]