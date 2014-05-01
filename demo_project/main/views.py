"""
Views.
"""

from django.shortcuts import render
from django.http import HTTPResponse

BASE_PAIRING = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}


def home(request):
    return HTTPResponse('OHAI')
