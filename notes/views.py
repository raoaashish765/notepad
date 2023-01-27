from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    if request.method=="GET":
        sfield=request.GET.get('srch', False)
        print(sfield)
        if sfield!=False:
            return redirect('note/'+sfield)
    return render(request, 'notes/index.html')

def note(request, nid):
    if request.method=="POST":
        cpass=request.POST['passw']
        chkdta=Allnotes.objects.get(link=nid)
        basepsw=chkdta.pass1
        print(cpass)
        print(basepsw)
        if cpass==basepsw:
            #show user text(s)
            usert=Txtall.objects.get(link=nid)
            shw=True
            return render(request, 'notes/note.html', {'show':shw, 'dta':usert, 'nid':nid})
        return render(request, 'notes/index.html')
    if Allnotes.objects.filter(link=nid):
        pres=True
    else:
        pres=False
    return render(request, 'notes/note.html', {'pres':pres, 'nid':nid})

def create(request):
    if request.method=="POST":
        id=request.POST['id']
        spass1=request.POST['pass1']
        spass2=request.POST['pass2']
        print(id)
        print(spass1)
        print(spass2)
        stdata=Allnotes.objects.create(link=id, pass1=spass1)
        stdata.save()
        txts=Txtall.objects.create(link=id)
        txts.save()
        return redirect('note/'+id)
    else:
        return redirect('home')

def updt(request):
    if request.method=="POST":
        id=request.POST['id2']
        stxt=request.POST['txtar']
        print(id)
        print(stxt)
        stdata=Txtall.objects.get(link=id)
        stdata.usrtxt=stxt
        stdata.save()
        return redirect('note/'+id)
    else:
        return redirect('home')