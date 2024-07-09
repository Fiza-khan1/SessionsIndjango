from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    cnt=request.session.get('count',0)
    newCount=cnt+1
    request.session['count']=newCount
    return render(request,'home.html',{'count':newCount})

def setsession(request):   
    request.session['Name']='Fiza'
    request.session['age']='22'
    request.session.set_expiry(600)
    return render(request,'setsession.html')


def getsession(request):
    if 'Name' in request.session:
        # request.session.modified=True
        name=request.session.get('Name','guest')
        age=request.session.get('Age','26')
    # keys=request.session.keys()
    # items=request.session.items()
        return render(request, 'getsession.html',{'name':name})
    else:
        return HttpResponse("Your session has expired")



def delSession(request):
    # if 'Name' in request.session:
    #     del request.session['Name']
    request.session.flush()
    # request.session.delete()
    
    return render(request,'delsession.html')
def settestcookie(request):
    request.session.set_test_cookie()
    if request.session.test_cookie_worked():
        return HttpResponse("Cookies worked")
    else:
        return HttpResponse("enable cookies")
    
    request.session.delete_test_cookie()
