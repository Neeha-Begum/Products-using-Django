from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msearch(request,pid):
    mobiles=[{'id':1,'brand':'Samsung s23','cost':80000,'config':'8gb 128gb'},
             {'id':2,'brand':'Xiaomi','cost':30000,'config':'6gb 128gb'},
             {'id':3,'brand':'Iphone','cost':136000,'config':'8gb 256gb'},
             {'id':4,'brand':'Oneplus','cost':25000,'config':'4gb 128gb'}]
    result=None
    for item in mobiles:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>Brand name:{result.get('brand')}<br>Cost:{result.get('cost')}<br>Configuration:{result.get('config')}</p>")
    else:
        return HttpResponse("Sorry,No result matched")
def lsearch(request,pid):
    laptops=[{'id':1,'brand':'Dell','cost':'65,000','config':'8gb 1Tb'},
          {'id':2,'brand':'HP','cost':'50,000','config':'8gb 512gb'},
          {'id':3,'brand':'Acer','cost':'35,000','config':'8gb 512gb'},
          {'id':4,'brand':'Macbook','cost':'1,00,000','config':'8gb 1TB'}]
    result=None
    for item in laptops:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>Brand name:{result.get('brand')}<br>Cost:{result.get('cost')}<br>Configuration:{result.get('config')}</p>")
    else:
        return HttpResponse("Sorry,No result matched")
def asearch(request,pid):
    airpods=[{'id':1,'brand':'Noise','cost':2500},
             {'id':1,'brand':'Galaxy buds','cost':18000},
             { 'id':3,'brand':'Boat','cost':1500},
             {'id':4,'brand':'One plus','cost':1000}]
    result=None
    for items in airpods:
        if items.get('id')==pid:
            result=items
            break
    if result is not None:
        return HttpResponse(f"<p>Brand name:{result.get('brand')}<br>Cost:{result.get('cost')}</p>")
    else:
        return HttpResponse("Sorry,No result matched")