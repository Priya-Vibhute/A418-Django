from django.shortcuts import render,HttpResponse
from django.views import View
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
   print("********************************")
   print(request.method)
   print("********************************")
   context={"id":"",
            "name":"Nisha",
            "subjects":["Maths","Science","English"]
            }
   return render(request,"students.html",context)

def book(request):
   print(request.GET.get("bookname"))
   print(request.GET.get("price"))

   context={"bookName":request.GET.get("bookname"),
            "price":request.GET.get("price")}
   
   return render(request,"book.html",context)

# request.GET
# request.POST

def employee(request):
   if request.method=='GET':
      return render(request,"employee.html")
   if request.method=='POST':
      employeeName=request.POST.get("employeeName")
      return render(request,"employee.html",{"empname": employeeName})
   


class MyView(View):

   def get(self,request):
      return render(request,"my_view.h tml")
   
   def post(self,request):
      return render(request,"success.html")
   
def learnFilters(request):
   return render(request,"template_filters.html",{"data":"Django"})
