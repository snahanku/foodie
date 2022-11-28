from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
#api_key=LQeKfQgZZC9C9ei04qpYvg==MJYJQ5xl14opYcrD
#API_URL=https://api.api-ninjas.com/v1/nutrition?query=
# Create your views here.
def home(request):
    #template =loader.get_template("home.html")

    context ={
        "message":"hello",
        "data" : [1,2,3,4,5]
    }
    import json
    import requests
    if request.method == 'POST':
        query= request.POST['query']
        api_url= 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request= requests.get(api_url+ query, headers={'X-Api-Key': 'LQeKfQgZZC9C9ei04qpYvg==MJYJQ5xl14opYcrD'})
        api= json.loads( api_request.content)
        try:
             api= json.loads( api_request.content)
             print( api_request.content)
        except Exception as e:
            api ="oops there was  an error "
            print(e)
        return render(request , "home.html",{'api':api})
    else:
        return render(request , "home.html",context)


    