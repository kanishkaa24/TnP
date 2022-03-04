from django.shortcuts import render
import csv

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
        with open('studentData.csv', 'r', encoding="utf8") as f:
            csv_reader = csv.reader(f)
            list = []
            for line in csv_reader:
                if enroll is not None and line[0] == enroll:
                    list.append(line)
                    return render(request, 'editdetails.html', {'data': list}) 
        with open('studentData.csv', 'r', encoding="utf8") as f:
            csv_reader = csv.reader(f)
            list = []
            for line in csv_reader:
                if roll is not None and line[0] == roll:
                    list.append(line)
                    return render(request, 'details.html', {'data': list})
    if request.POST:
        name = request.POST.get('searchname')
        editname = request.POST.get('editprofile')
        enrollmentNum = request.POST.get('enrollnum')
        email = request.POST.get('email')
        branch = request.POST.get('branch')
        contact = request.POST.get('contact')
        alternate = request.POST.get('alternate')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        address = request.POST.get('address')
        xp = request.POST.get('XthP')
        xc = request.POST.get('XthC')
        xb = request.POST.get('XthB')
        xy = request.POST.get('XthY')
        xiip = request.POST.get('XIIthP')
        xiib = request.POST.get('XIIthB')
        xiiy = request.POST.get('XIIthY')
        cet = request.POST.get('CET')
        dpp = request.POST.get('DPP')
        yod = request.POST.get('YOD')
        sem1 = request.POST.get('sem1')
        sem2 = request.POST.get('sem2')
        sem3 = request.POST.get('sem3')
        sem4 = request.POST.get('sem4')
        sem5 = request.POST.get('sem5')
        semt5 = request.POST.get('semt5')
        sem6 = request.POST.get('sem6')
        semt6 = request.POST.get('semt6')
        sem7 = request.POST.get('sem7')
        semt7 = request.POST.get('semt7')
        pb = request.POST.get('pbacklog')
        cb = request.POST.get('cbacklog')
        eligible = request.POST.get('eligible')
        gap = request.POST.get('gap')
        placed1 = request.POST.get('placed1')
        placed2 = request.POST.get('placed2')
        placed3 = request.POST.get('placed3')
        placed4 = request.POST.get('placed4')
        remarks = request.POST.get('remarks')
        if name is not None and editname is None:
            with open('studentData.csv', encoding="utf8") as f:
                csv_reader = csv.reader(f)
                list = []
                for line in csv_reader:
                    if name is not None and line[2].find(name.upper()) != -1 and line[2] != "NAME":
                        list.append(line)
                return render(request, 'profile.html', {'data': list}) 
        if editname is not None:
            data = [enrollmentNum, branch, editname, remarks, gender, dob, address, category, contact, alternate, email, xp, xc, xb, xy, xiip, xiib, xiiy, cet, dpp, yod, sem1, sem2, sem3, sem4, sem5, semt5, sem6, semt6, sem7, semt7, pb, cb, eligible, gap, placed1, placed2, placed3, placed4]
            listremove = []  
            with open('studentData.csv', 'r', encoding="utf8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[2] != editname:
                        listremove.append(row)
            with open('studentData.csv', 'w', encoding="utf8", newline='') as f:
                writer = csv.writer(f)
                for line in listremove:
                    writer.writerow(line)      
            with open('studentData.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)  
                f.close()
            with open('studentData.csv', encoding="utf8") as f:
                csv_reader = csv.reader(f)
                list = []
                for line in csv_reader:
                    if editname is not None and line[2].find(editname.upper()) != -1 and line[2] != "NAME":
                        list.append(line)
                        return render(request, 'profile.html', {'data': list})             
    return render(request, 'studentprofile.html')

def profile(request):
    return render(request, 'profile.html')

def studentlist(request):
    return render(request, 'studentlist.html')

def editdetails(request):
    return render(request, 'editdetails.html')

def details(request):
    return render(request, 'details.html')

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