from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from account.forms import Accountform
from account.models import Account,Transaction


# Create your views here.


def home(request):
    return render(request,'home.html')


def register(request):                                           #here context dictionary type used to send data from view to html
    if (request.method == "POST"):  # after submission this condition works
        ##normal field
        u = request.POST["u"]  # for normal data request.POST for taking value
        p = request.POST["p"]
        cp = request.POST["cp"]
        e = request.POST["e"]
        fn = request.POST["fn"]
        ln = request.POST["ln"]
        if(cp==p):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln)
            u.save()
            return redirect('account:home')
        else:
            return HttpResponse("passwords are not same")
    return render(request, 'register.html')


def user_login(request):
    if (request.method == "POST"):
        u = request.POST["u"]
        p = request.POST["p"]
        user=authenticate(username=u,password=p)
        if(user):
            login(request,user)
            return redirect('account:home')
        else:
            return HttpResponse("invalid credentials")

    return render(request,'login.html')


def user_logout(request):
    logout(request)               #here logout(rquest) is builtin func so need to import and just add this
    # return user_login(request)
    return redirect('account:home')




def viewtransaction(request):
    u=request.user
    t = Transaction.objects.filter(user=u)
    return render(request, "viewtransaction.html", {"t": t})


def create(request):
    if (request.method == "POST"):  # after submission this condition works
        u = request.user

        ##normal field
        t = request.POST["an"]  # for normal data request.POST for taking value
        a = request.POST["hn"]
        p = request.POST["at"]


        cv = request.POST["b"]  # for file field  request.FILES for taking value

        a = Account.objects.create(account_number=t, account_holder_name=a, account_type=p, balance=cv,user=u)

        a.save()
        return home(request)
    return render(request, 'create.html')


def update(request):
    u=request.user
    a=Account.objects.filter(user=u)
    return render(request, 'update2.html',{'a':a})

def edit(request,n):
    a=Account.objects.get(pk=n)    #first we fetch that particular field with id ( arguement passed from view.html
    if (request.method == "POST"):  # after submission this condition works
        form = Accountform(request.POST,instance=a)
                      #here request.post is for normal field and .FILE is for media content    #instance=b is that id with field datas
        if form.is_valid():  # checks the validity of form, its a django in built func
                form.save()     #saves or insert the values entered in form field to their apropriate table field coz the form already created based on table
                return home(request)

    form = Accountform(instance=a)                 #need to create an empty form here to display in add1.html
                #here instance =b is given in empty form to fill the data in form field when form loads then edit process up

    return render(request, 'update.html',{'form':form})



def delete(request,n):
    a=Account.objects.get(id=n)    #for delete first we fetch that particular field with id ( arguement passed from view.html)
    a.delete()               #then .delete()
    return home(request)   #optional can direct to another page after deleting or any process


