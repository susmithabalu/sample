# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
import csv
from sample.forms import UploadForm
from sample.models import CSV


def home(request):
   
    return render_to_response("home.html")

def upload(request):
    return render_to_response("upload.html")