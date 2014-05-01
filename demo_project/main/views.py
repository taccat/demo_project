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
    context = {}

    # Check whether this request includes a query string to translate.
    query_string = request.GET.get('query', None)
    if query_string:
        query_string = query_string.upper()
        reverse_complement = ''
        for base in query_string:
            reverse_complement += BASE_PAIRING[base]
        context['query_string'] = query_string
        context['reverse_complement'] = reverse_complement

    return render(request, 'home.html', context)
