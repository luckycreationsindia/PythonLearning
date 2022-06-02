from django.http import HttpResponse
from django.shortcuts import render
from LearningMongo.db import addCustomer, updateCustomer
from bson.objectid import ObjectId

def create(request):
    x = addCustomer(name='Lucky', email='luckycreationsindia@gmail.com')
    print(x)
    return HttpResponse('Created')

def update(request):
    x = updateCustomer(id = ObjectId(oid='6298ac7e1e95be3422343cd2'), name='Lokesh Jain', email='luckycreationsindia@gmail.com')
    # x = updateCustomer(id = '6298ac7e1e95be3422343cd2', name='Lokesh Jain', email='luckycreationsindia@gmail.com')
    print(x.acknowledged)
    return HttpResponse('Updated')