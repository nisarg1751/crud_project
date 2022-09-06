from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse
from sub.forms import Reg
from sub.models import User
from django.contrib import messages
# Create your views here.
def add(request):
    stud = User.objects.all()
    if request.method == 'POST':
        fm = Reg(request.POST)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',request.POST)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['password']
            reg = User(name = nm, email = em,password=pm)
            reg.save()
            fm = Reg()
            # messages.add_message(request,messages.SUCCESS,'Your data has been created')
            messages.success(request,'you data is added successfully!!!!!!')
    else:
        fm = Reg()
    return render(request,'addandshow.html',{'form':fm, 'stu':stud})

def update(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Reg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request,messages.SUCCESS,'your data updated successfully')
            messages.success(request,'you data is update successfully!!!!!!')
            # return redirect('successful')
    else:
        pi = User.objects.get(pk=id)
        fm = Reg(instance=pi)
    return render(request,'update.html',{'form':fm})



def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def thankyou(request):
    return render(request,'thankyou.html')

def adddata(request):
    stud = User.objects.all()
    if request.method == 'POST':
        fm = Reg(request.POST)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',request.POST)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['password']
            reg = User(name = nm, email = em,password=pm)
            reg.save()
            fm = Reg()
            # messages.add_message(request,messages.SUCCESS,'Your data has been created')
            messages.success(request,'you data is added successfully!!!!!!')
            return JsonResponse({'status':'Save'})
        else:
            return JsonResponse({'status':'Failed'})
