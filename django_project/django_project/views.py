from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse('<b>welcome dear<b>')
def aboutdetails(request,detailid):
    return HttpResponse(detailid)
def homepage(request):
    data={"T" :"sakshi's page"}
    return render(request,"index.html",data)