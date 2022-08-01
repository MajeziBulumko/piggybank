from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CustomerApp.models import AccountType, ClientInfo
from CustomerApp.serializer import AccountSerializer,ClientSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def AccountAPI(request, id = 0):
    if request.method=='GET':
        account = AccountType.objects.all()
        account_serializer = AccountSerializer(account, many=True)
        return JsonResponse(account_serializer.data, safe=False)

    elif request.method=='POST':
        account_data=JSONParser().parse(request)
        account_serializer = AccountSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method=='PUT':
        account_data = JSONParser().parse(request)
        account =AccountType.objects.get(AccountId=account_data['AccountId'])
        account_serializer=AccountSerializer(account,data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        account = AccountType.objects.get(AccountId=id)
        account.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def ClientAPI(request, id = 0):
    if request.method=='GET':
        client = ClientInfo.objects.all()
        client_serializer = ClientSerializer(client, many=True)
        return JsonResponse(client_serializer.data, safe=False)

    elif request.method == 'POST':
        client_data = JSONParser().parse(request)
        client_serializer = ClientSerializer(data = client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

    elif request.method == 'PUT':
        client_data = JSONParser().parse(request)
        client = ClientInfo.objects.get(clientId = client_data['clientId'])
        client_serializer = ClientSerializer(client,data= client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Updated Successfully!!" , safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        client = ClientInfo.objects.get(clientId=id)
        client.delete()
        return JsonResponse("Deleted Succeffully!!", safe =False)


# Create your views here.
