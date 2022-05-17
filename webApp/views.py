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
        year = request.POST.get('year')
        if year == "2022":
            with open('recruiters2022.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)  
                f.close()
        if year == "2023":
            with open('recruiters2023.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)  
                f.close()
    return render(request, 'addrecruiters.html')

def recruiters(request):
    list2022 = []
    list2023 = []
    with open('recruiters2022.csv', encoding="utf8") as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            if line != ['Name', 'Profile', 'Package', 'DreamState']:
                list2022.append(line) 
    with open('recruiters2023.csv', encoding="utf8") as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            if line != ['Name', 'Profile', 'Package', 'DreamState']:
                list2023.append(line)         
    return render(request, 'recruiters.html', {'data2022': list2022, 'data2023': list2023})

def editrecruiters2022(request):
    list = []
    with open('recruiters2022.csv', encoding="utf8") as f:
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
        with open('recruiters2022.csv', 'r', encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != name:
                    print(row)
                    listremove.append(row)
        with open('recruiters2022.csv', 'w', encoding="utf8", newline='') as f:
            writer = csv.writer(f)
            for line in listremove:
                writer.writerow(line)      
        with open('recruiters2022.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)  
            f.close()
    return render(request, 'editrecruiters2022.html', {'data': list})

def editrecruiters2023(request):
    list = []
    with open('recruiters2023.csv', encoding="utf8") as f:
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
        with open('recruiters2023.csv', 'r', encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != name:
                    print(row)
                    listremove.append(row)
        with open('recruiters2023.csv', 'w', encoding="utf8", newline='') as f:
            writer = csv.writer(f)
            for line in listremove:
                writer.writerow(line)      
        with open('recruiters2023.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)  
            f.close()
    return render(request, 'editrecruiters2023.html', {'data': list})

def studentprofile(request):
    if request.GET:
        roll = request.GET.get('id')
        enroll = request.GET.get('rollid')
        with open('studentData2022.csv', 'r', encoding="utf8") as f:
            csv_reader = csv.reader(f)
            list = []
            for line in csv_reader:
                if enroll is not None and line[0] == enroll:
                    list.append(line)
                    return render(request, 'editdetails.html', {'data': list}) 
        with open('studentData2022.csv', 'r', encoding="utf8") as f:
            csv_reader = csv.reader(f)
            list = []
            for line in csv_reader:
                if roll is not None and line[0] == roll:
                    list.append(line)
                    return render(request, 'details.html', {'data': list})
    if request.POST:
        name = request.POST.get('searchname')
        editname = request.POST.get('editprofile')
        rollNum = request.POST.get('rollNum')
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
        semt4 = request.POST.get('semt4')
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
        blocked = request.POST.get('blocked')
        ppo = request.POST.get('ppo')
        placed1 = request.POST.get('placed1')
        placed2 = request.POST.get('placed2')
        placed3 = request.POST.get('placed3')
        placed4 = request.POST.get('placed4')
        placed5 = request.POST.get('placed5')
        placed6 = request.POST.get('placed6')
        dream1 = request.POST.get('dream1')
        dream2 = request.POST.get('dream2')
        dream3 = request.POST.get('dream3')
        dream4 = request.POST.get('dream4')
        if name is not None and editname is None:
            with open('studentData2022.csv', encoding="utf8") as f:
                csv_reader = csv.reader(f)
                list = []
                for line in csv_reader:
                    if name is not None and line[2].find(name.upper()) != -1 and line[2] != "NAME":
                        list.append(line)
                return render(request, 'profile.html', {'data': list}) 
        if editname is not None:
            data = [rollNum, enrollmentNum, editname, branch, gender, dob, address, category, contact, alternate, email, xp, xc, xb, xy, xiip, xiib, xiiy, cet, dpp, yod, sem1, sem2, sem3, sem4, semt4, sem5, semt5, sem6, semt6, sem7, semt7, pb, cb, eligible, gap, blocked, ppo, placed1, placed2, placed3, placed4, placed5, placed6, dream1, dream2, dream3, dream4]
            listremove = []  
            with open('studentData2022.csv', 'r', encoding="utf8") as f:
                reader = csv.reader(f)
                for row in reader:
                    if row[2] != editname:
                        listremove.append(row)
            with open('studentData2022.csv', 'w', encoding="utf8", newline='') as f:
                writer = csv.writer(f)
                for line in listremove:
                    writer.writerow(line)      
            with open('studentData2022.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(data)  
                f.close()
            with open('studentData2022.csv', encoding="utf8") as f:
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
    if request.POST:
        allfive = request.POST.get('branch')
        cse = request.POST.get('cse')
        it = request.POST.get('it')
        ece = request.POST.get('ece')
        eee = request.POST.get('eee')
        ice = request.POST.get('ice')
        ten = float(request.POST.get('ten'))
        twelve = float(request.POST.get('twelve'))
        diploma = float(request.POST.get('diploma'))
        gap = float(request.POST.get('gap'))
        backlog = float(request.POST.get('backlog'))
        overall = float(request.POST.get('overall'))
        male = request.POST.get('male')
        female = request.POST.get('female')
        all = request.POST.get('both')
        iplaced = request.POST.get('iplaced')
        eplaced = request.POST.get('eplaced')
        ppo = request.POST.get('ppo')
        mplaced = float(request.POST.get('mplaced'))
        dattempt = float(request.POST.get('dattempt'))
        genm = "MALE"
        if not male and not all:
            genm = ""
        genf = "FEMALE"
        if not female and not all:
            genf = ""
        bcseI = ""
        bcseII = ""
        bitI = ""
        bitII = ""
        bice = ""
        beceI = ""
        beceII = ""
        beceIII = ""
        beee = ""
        if allfive:
            bcseI = "Computer Sc. (Section I)"
            bcseII = "Computer Sc. (Section II)"
            bitI = "Information Tech. (Section I)"
            bitII = "Information Tech. (Section II)"
            bice =  "Instrumentation & Control"
            beee = "Electrical & Electronics Engg."
            beceI = "Electronics & Eomm. Engg. (Section I)"
            beceII = "Electronics & Eomm. Engg. (Section II)"
            beceIII = "Electronics & Eomm. Engg. (Section III)"
        if cse:
            bcseI = "Computer Sc. (Section I)"
            bcseII = "Computer Sc. (Section II)"
        if it:
            bitI = "Information Tech. (Section I)"
            bitII = "Information Tech. (Section II)"
        if ice:
            bice =  "Instrumentation & Control"
        if eee:
            beee = "Electrical & Electronics Engg."
        if ece:
            beceI = "Electronics & Eomm. Engg. (Section I)"
            beceII = "Electronics & Eomm. Engg. (Section II)"
            beceIII = "Electronics & Eomm. Engg. (Section III)"
        list = []
        with open('studentData2022.csv', 'r', encoding="utf8") as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                if line[11] == "":
                    line[11] = 0
                if line[15] == "":
                    line[15] = 0
                if line[19] == "":
                    line[19] = 0
                if line[31] == "":
                    line[31] = 0
                if line[32] == "":
                    line[32] = 0
                if line[35] == "":
                    line[35] = 0
                count = 0
                for i in range(38, 44):
                    if line[i] != "":
                        count += 1
                count1 = 0
                for i in range(44, 48):
                    if line[i] != "":
                        count1 += 1
                if (line[3] == bcseI or line[3] == bcseII or line[3] == bitI or line[3] == bitII or line[3] == bice or line[3] == beee or line[3] == beceI or line[3] == beceII or line[3] == beceIII) and (line[4] == genm or line[4] == genf) and (float(line[11]) >= ten) and (float(line[15]) >= twelve or float(line[19]) >= diploma) and (float(line[31]) >= overall) and (float(line[32]) <= backlog) and (float(line[35]) <= gap) and (count <= mplaced) and (count1 <= dattempt):
                    if line[11] == 0:
                        line[11] = ""
                    if line[15] == 0:
                        line[15] = ""
                    if line[19] == 0:
                        line[19] = ""
                    if line[31] == 0:
                        line[31] = ""
                    if line[32] == 0:
                        line[32] = ""
                    if line[35] == 0:
                        line[35] = ""
                    if ppo == "No" or ppo == "no":
                        if line[37] == "":
                            if iplaced != "":
                                include = iplaced.split(",")
                                flag = 0
                                for i in include:
                                    for j in range(37, 44):
                                        if (line[j].lower()).find(i.lower()) != -1:
                                            flag = 1
                                if flag:
                                    if eplaced != "":
                                        exclude = eplaced.split(",")
                                        flag1 = 1
                                        for i in exclude:
                                            for j in range(37, 44):
                                                if (line[j].lower()).find(i.lower()) != -1:
                                                    flag1 = 0
                                        if flag1:
                                            list.append(line)
                                    else:
                                        list.append(line)
                            else:
                                list.append(line)
                    if ppo == "Yes" or ppo == "yes":
                        if line[37] != "":
                            if iplaced != "":
                                include = iplaced.split(",")
                                flag = 0
                                for i in include:
                                    for j in range(37, 44):
                                        if (line[j].lower()).find(i.lower()) != -1:
                                            flag = 1
                                if flag:
                                    if eplaced != "":
                                        exclude = eplaced.split(",")
                                        flag1 = 1
                                        for i in exclude:
                                            for j in range(37, 44):
                                                if (line[j].lower()).find(i.lower()) != -1:
                                                    flag1 = 0
                                        if flag1:
                                            list.append(line)
                                    else:
                                        list.append(line)
                            else:
                                list.append(line)
        with open('studentData2022new.csv', 'w', encoding="utf8", newline='') as f:
                writer = csv.writer(f)
                for line in list:
                        writer.writerow(line)
        return render(request, 'list.html', {'data': list})
    return render(request, 'studentlist.html')

def list(request):
    return render(request, 'list.html') 

def editdetails(request):
    return render(request, 'editdetails.html')

def details(request):
    return render(request, 'details.html')