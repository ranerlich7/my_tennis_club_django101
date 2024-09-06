from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    template = loader.get_template('members_page.html')
    return HttpResponse(template.render())

def trainers(request):
    return HttpResponse("These are my Trainers")

def courts(request):
    return HttpResponse("These are my Courts")

def main(request):
    return HttpResponse("Welcome to my tennis club!")