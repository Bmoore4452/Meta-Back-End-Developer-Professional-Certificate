from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<html><body><h1>This is my first demo in Django</h1></body></html>"
    )


def add(request):
    path = request.path
    method = request.method
    content = """ 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
""".format(
        path, method
    )
    return HttpResponse(content)


def header(request):
    path = request.path
    scheme = request.scheme
    methond = request.method
    address = request.META["REMOTE_ADDR"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path_info = request.path_info

    response = HttpResponse()
    response.headers["Age"] = 20

    msg = f"""<br>
    <br>Path : {path}
    <br>Address : {address}
    <br>Scheme : {scheme}
    <br>Method : {methond}
    <br>User Agent : {user_agent}
    <br>Path Info : {path_info}
    <br>Response Headers : {response.headers}
    
    """
    return HttpResponse(msg, content_type="text/html", charset="utf-8")


def pathview(request):
    name = request.GET.get("name")
    id = request.GET.get("id")
    return HttpResponse(f"Name : {name} <br> USERID : {id}")


def showform(request):
    return render(request, "form.html")


def getform(request):
    if request.method == "POST":
        id = request.POST["id"]
        name = request.POST["name"]
    return HttpResponse("Name:{} UserID:{}".format(name, id))


def menuitems(request, dish):
    items = {
        "hotdog": "I love hotdogs",
        "pizza": "I love pizza",
        "purger": "I love burgers",
    }

    description = items[dish]

    return HttpResponse(f"<h1>{dish}</h1><p>{description}</p>")
