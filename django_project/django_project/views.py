from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse('<b>welcome dear<b>')
def aboutdetails(request,detailid):
    return HttpResponse(detailid)