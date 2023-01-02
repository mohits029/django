from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return( render(request, 'index.html') )

def submit(request):
    textarea= request.GET.get('text', 'nothing')
    removepunch= request.GET.get('removepunch', 'off')
    uppercase= request.GET.get('uppercase', 'off')
    

    punctution= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    sortedpunc= ""
    up=""
    if(removepunch== "on"):
        for char in textarea:
            if(char not in punctution):
                sortedpunc= sortedpunc+char

    if(uppercase=="on"):
        up= sortedpunc.upper()

    val= {
        'removepunch': sortedpunc,
        'upper': up
    }

    return (render(request, 'submit.html', val))