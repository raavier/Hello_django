from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request,n1,n2):
    soma1 = n1+n2
    return HttpResponse('<h1> A soma de {} com {} é igual a {}</h1>'.format(n1,n2,soma1))

def sub(request,n1,n2):
    sub1 = n1-n2
    return HttpResponse('<h1> A sub de {} com {} é igual a {}</h1>'.format(n1,n2,sub1))

def mult(request,n1,n2):
    mult1 = n1*n2
    return HttpResponse('<h1> A mult de {} com {} é igual a {}</h1>'.format(n1,n2,mult1))

def div(request,n1,n2):
    div1 = n1/n2
    return HttpResponse('<h1> A div de {} com {} é igual a {}</h1>'.format(n1,n2,div1))