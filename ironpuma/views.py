from django.shortcuts import render
# from django import views

def home(request):
	return render(request, 'index.html')