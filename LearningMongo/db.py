import pymongo
from bson.objectid import ObjectId

from ProjectLearning.typechecker import strict_types

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["PythonLearning"]

def addCustomer(**customer):
    mycol = mydb["customers"]
    x = mycol.insert_one(customer)
    return x

@strict_types
def updateCustomer(id: ObjectId, **customer):
    mycol = mydb["customers"]
    x = mycol.update_one({'_id': id}, { "$set": customer })
    return x

def getDB():
    return mydb