from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import AirportModel
from .serializers import *
from django.shortcuts import render
from django.http import JsonResponse

from django.core import serializers


import json

@api_view(['GET', 'POST'])




def original(request):
    if request.method == 'GET':
        try:
            
            with open("AirportTraffic/fixtures/AirportTraffic.json") as json_file:
                data = json.load(json_file)
                resp = JsonResponse(data,safe = False,status = 200)
                # resp['Access-Control-Allow-Origin'] = 'http://localhost:8000'
                return(resp)
        except FileNotFoundError:
            return(Response(status=status.HTTP_404_NOT_FOUND))
    return(Response(status=status.HTTP_404_NOT_FOUND))




# def BooksList(request):
#     books = []
#     # you can change .all() to .filter()
#     # ex: Book.objects.filter(user=request.user.id):
#     for obj in AirportModel.objects.all():
#         books += [{'Primary_Key' : obj['primary_key'],
#         'ReportPeriod': obj['report_period'],
#         'Terminal':obj['terminal'],
#         'Arrival_Departure':obj['Arrival_Departure'],
#         'Domestic_International':obj['Domestic_International'],
#         'Passenger_Count':obj['passenger_count']

#         }]
#         data = {"Instances": books}
#         response = JSONResponse(data, {}, response_mimetype(request))
#         response['Content-Disposition'] = 'inline; filename=files.json'
#         return response




def load_original(request):
    try:
        
        with open("AirportTraffic/fixtures/AirportTraffic.json") as json_file:
            data = json.load(json_file)
            out = []
            m = 0
            for j in data:
                j["report_period"] = j.pop("ReportPeriod")
                j["terminal"] = j.pop("Terminal")
                j["arrival_departure"] = j.pop("Arrival_Departure")
                j["domestic_international"] = j.pop("Domestic_International")
                j["passenger_count"] = j.pop("Passenger_Count")
                j['primary_key'] = m
                m+=1
                j['model'] = "AirportTraffic.Airport"
                p = AirportModel.objects.create_air(j)
                p.save()

                
                        
        books = []
        # you can change .all() to .filter()
        # ex: Book.objects.filter(user=request.user.id):
        for obj in AirportModel.objects.all():
            print(obj.__dict__)
            books += [{
            'Primary_Key' : obj.primary_key,
            'ReportPeriod': obj.report_period,
            'Terminal':obj.terminal,
            'Arrival_Departure':obj.arrival_departure,
            'Domestic_International':obj.domestic_international,
            'Passenger_Count':obj.passenger_count

            }]
            data = {"Instances": books}
        response = JsonResponse(data)
        return(response)
    except FileNotFoundError:
        return(Response(status=status.HTTP_404_NOT_FOUND))
    


# def airports_list(request):


#     """
#  List  Airports, or create a new Airport.
#  """
#     if request.method == 'GET':
#         data = []
#         nextPage = 1
#         previousPage = 1
#         Airports = Airport.objects.all()
#         page = request.GET.get('page', 1)
#         paginator = Paginator(Airports, 100)
#         try:
#             data = paginator.page(page)
#         except PageNotAnInteger:
#             data = paginator.page(1)
#         except EmptyPage:
#             data = paginator.page(paginator.num_pages)

#         serializer = AirportSerializer(data,context={'request': request} ,many=True)
#         if data.has_next():
#             nextPage = data.next_page_number()
#         if data.has_previous():
#             previousPage = data.previous_page_number()

#         return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/Airports/?page=' + str(nextPage), 'prevlink': '/api/Airports/?page=' + str(previousPage)})

#     elif request.method == 'POST':
#         serializer = AirportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def airport_detail(request, pk):
#     """
#  Retrieve, update or delete a Airport by id/pk.
#  """
#     try:
#         Airport = Airport.objects.get(pk=pk)
#     except Airport.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = AirportSerializer(Airport,context={'request': request})
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = AirportSerializer(Airport, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         Airport.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)