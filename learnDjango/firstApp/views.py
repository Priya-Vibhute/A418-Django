from django.shortcuts import render,HttpResponse
#  A   A()
# Create your views here.

# Function based View

def about(request):
   return HttpResponse("")

def home(request):
   return HttpResponse("Home page")

def courses(request):
   return render(request,"courses.html",{})

def students(request):
   context={"id":"",
            "name":"Nisha",
            "subjects":["Maths","Science","English"]
            }
   return render(request,"students.html",context)
