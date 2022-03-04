from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import csv
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'home.html')

def addrecruiters(request):
    if request.POST:
        name = request.POST.get('nameof')
        profile = request.POST.get('profile')
        package = request.POST.get('package')
        dream = request.POST.get('dreamstate')
        data = [name, profile, package, dream]
        print(name, profile, package, dream)
        with open('recruiters.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)  
            f.close()
    return render(request, 'addrecruiters.html')

def recruiters(request):
    with open('recruiters.csv', encoding="utf8") as f:
        csv_reader = csv.reader(f)
        list = []
        for line in csv_reader:
            if line != ['Name', 'Profile', 'Package', 'DreamState']:
                list.append(line)           
    return render(request, 'recruiters.html', {'data': list})

def studentprofile(request):
    if request.GET:
        roll = request.GET.get('id')
        enroll = request.GET.get('rollid')
        with open('studentData.csv', encoding="utf8") as f:
            csv_reader = csv.reader(f)
            list = []
            for line in csv_reader:
                if roll is not None and line[0] == roll:
                    list.append(line)
            return render(request, 'details.html', {'data': list}) 
    if request.POST:
        name = request.POST.get('searchname')
        with open('studentData.csv', encoding="utf8") as f:
            csv_reader = csv.reader(f)
            list = []
            for line in csv_reader:
                if name is not None and line[2].find(name.upper()) != -1 and line[2] != "NAME":
                    list.append(line)
            return render(request, 'profile.html', {'data': list})              
    return render(request, 'studentprofile.html')

def profile(request):
    return render(request, 'profile.html')

def studentlist(request):
    return render(request, 'studentlist.html')

def editrecruiters(request):
    list = []
    with open('recruiters.csv', encoding="utf8") as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            if line != ['Name', 'Profile', 'Package', 'DreamState']:
                list.append(line) 
    if request.POST:
        name = request.POST.get('nameCompany')
        profile = request.POST.get('profile')
        package = request.POST.get('package')
        dream = request.POST.get('dreamstate')
        data = [name, profile, package, dream]
        listremove = []  
        with open('recruiters.csv', 'r', encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != name:
                    print(row)
                    listremove.append(row)
        with open('recruiters.csv', 'w', encoding="utf8", newline='') as f:
            writer = csv.writer(f)
            for line in listremove:
                writer.writerow(line)      
        with open('recruiters.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)  
            f.close()
    return render(request, 'editrecruiters.html', {'data': list})