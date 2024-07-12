from django.shortcuts import render
# from django.http import JsonResponse

# Create your views here


#.................by passing only key and provide the name of key.................
# def home(request):
#    Name ='Priya Pardeshi'
#    City ='Bhopal'
#    Qualification = 'B.tech'

#    return render(request,'home.html',{'nm':Name,
#                                       'ct':City,
#                                       'qual':Qualification
#                                       })



# ............by passsing key and value in dic formate..............
# def home(request):
#     data={
#         'nm':'Priya Pardeshi',
#         'qual':'B.tech',
#         'ct':'Bhopal'
#     }
#     return render(request,'home.html',{'key':data})




# ..........passing one attribute like nm in all place............
def home(request):
    data={
        'nm':{
            'name':"Priya Pardeshi",
            'qual':"B.Tech",
            'ct':"Bhopal"
        }
    }
    return render(request,'home.html',{'key':data})