from django.shortcuts import render,redirect,HttpResponse,reverse

import json

# Create your views here.

def tryjson(request):

    hint={"info":None,"who":None,"flag":"False"}

    if request.method=="GET":

        return render(request,'propose.html')

    wenwa = {"name":None,"age":None}

    name = request.POST.get("name",None)

    age = request.POST.get("age",None)

    hint["flag"] = "True"

    hint["info"] = "元首~"+name+"已经来了"

    hint["who"] = name

    print("hint===========>",hint)

    data = json.dumps(hint)

    return HttpResponse(data)

    # return render(request, 'propose.html',locals())