import respond
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from .models import CountryModel
from .serializers import CountrySeriliazers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.contrib import messages #import messages

# Create your views here.
@api_view(['GET'])
def country_fun(request):
    showresult=CountryModel.objects.all()
    # print("#### ",showresult)
    serializerobj=CountrySeriliazers(showresult,many=True)
    # print("%%%% ",serializerobj.data)
    return Response(serializerobj.data)

def showcountry(request):
    try:
        # messages.success(request,'redirecting next page')
        return render(request,'index.html')
    except ValueError as v:
        messages.warning(request, 'please select country',v)
        return HttpResponse(messages.error('select country'))

def index_pass_name(request):
    try:
        country = request.GET['country']
        print('selected country is ', country)
        return render(request,'page2_index.html',{'country':country})
    except MultiValueDictKeyError:
        messages.error(request, 'please select country')
    except ValueError as v:
        messages.warning(request, 'please select country',v)

def webpage1(request):
    return render(request,'page1.html')

def webpage2(request):
    result=request.GET['fruits']
    print('selected fruit is ',result)
    return render(request,'page2.html',{'fruits':result})