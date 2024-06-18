# Create your views here.


from django.shortcuts import render, redirect
from .models import Admission, Contact
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        if request.method == "POST":
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            mobile_number = request.POST.get('mobile_number', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            print(name, email, mobile_number)
            contact = Contact(
                name=name,
                email=email,
                mobile_number=mobile_number,
                subject=subject,
                message=message
            )
            try:
                contact.save()
                return render(request, 'contact.html', {'success_message': 'Thank you for contacting us!'})
            except Exception as e:
                print(f"Error saving contact data: {e}")
                return render(request, 'contact.html', {'error_message': 'An error occurred. Please try again later.'})
    return render(request, 'contact.html')


def courses(request):
    return render(request, 'courses.html')


def login(request):
    return render(request, 'login.html')


from django.core.files.storage import FileSystemStorage


def admission(request):
    if request.method == 'POST':
        print(request.FILES)
        name = request.POST.get('Name', '')
        email = request.POST.get('Email', '')
        number = request.POST.get('Number', '')
        dob = request.POST.get('DOB', '')
        aadhaar = request.POST.get('Aadhaar', '')
        gender = request.POST.get('Gender', '')
        education = request.POST.get('Education', '')
        doc_10th = request.FILES.get('doc_10th', None)
        doc_12th = request.FILES.get('doc_12th', None)
        doc_graduate = request.FILES.get('doc_graduate', None)
        doc_postgraduate = request.FILES.get('doc_postgraduate', None)
        course_name = request.POST.get('Course_name', '')
        address = request.POST.get('Address', '')
        state = request.POST.get('State', '')
        district = request.POST.get('District', '')
        pincode = request.POST.get('Pincode', '')
        fs = FileSystemStorage()

        if doc_10th:
            filename_10th = fs.save(doc_10th.name, doc_10th)
            file_url_10th = fs.url(filename_10th)
            print("10th Doc URL:", file_url_10th)

        if doc_12th:
            filename_12th = fs.save(doc_12th.name, doc_12th)
            file_url_12th = fs.url(filename_12th)
            print("12th Doc URL:", file_url_12th)

        if doc_graduate:
            filename_graduate = fs.save(doc_graduate.name, doc_graduate)
            file_url_graduate = fs.url(filename_graduate)
            print("Graduate Doc URL:", file_url_graduate)

        if doc_postgraduate:
            filename_postgraduate = fs.save(doc_postgraduate.name, doc_postgraduate)
            file_url_postgraduate = fs.url(filename_postgraduate)
            print("Postgraduate Doc URL:", file_url_postgraduate)

        print(name, email, number, dob, aadhaar, gender, education, doc_10th, doc_12th, doc_graduate, doc_postgraduate,
              course_name, address, state, district, pincode)

        admission = Admission(
            name=name,
            email=email,
            number=number,
            dob=dob,
            aadhaar=aadhaar,
            gender=gender,
            education=education,
            doc_10th=doc_10th,
            doc_12th=doc_12th,
            doc_graduate=doc_graduate,
            doc_postgraduate=doc_postgraduate,
            course_name=course_name,
            address=address,
            state=state,
            district=district,
            pincode=pincode,
        )
        admission.save()
    return render(request, 'admission.html')


def airportmanagement(request):
    return render(request, 'airportmanagement.html')
