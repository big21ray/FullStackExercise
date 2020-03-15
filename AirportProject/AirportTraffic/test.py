# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from .models import Airport
# from .serializers import *
# from django.shortcuts import render
# from django.http import JsonResponse

from django.core import serializers
import json
with open("fixtures/AirportTraffic.json") as json_file:
            data = json.load(json_file)
            obj_generator = serializers.deserialize("json",data)
            print(obj_generator)