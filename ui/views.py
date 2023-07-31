from django.http import JsonResponse
from django.shortcuts import render


def index(request):
	return render(request, "frontend/index.html")


def say(request):
	return JsonResponse({'This':'HEllo axios!!!!'},safe=False)
