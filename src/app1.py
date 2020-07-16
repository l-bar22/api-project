from flask import Flask,request
from flask_pymongo import flask_pymongo
from bson import json_util
from bson.objectid import ObjectId
app=Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/friendsdb'

mongo=PyMongo(app)

if __name__ =='__main__':
    app.run(debug=True)

@app.route('/users',methods=['POST'])
def create_user():
    name=request.json['name']
    familyname=request.json['familyname']

    if name and familyname:
       id=mongo.db.users.insert(
           {'name':name,'familyname':familyname}
       ) 
        response ={
            'id':str(id),
            'name':name,
            'familyname':familyname
        }
        return response
    else:
        return not_found()

@app.route('/chat',method=['POST'])
def create_chat():
    participant1=request.json['participant1']
    dialogue1=request.json['dialogue1']
    participant2=request.json['participant2']
    dialogue2=request.json['dialogue2']
    if participant1 and dialogue1 and participant2 and dialogue2:
        id=mongo.db.chat.insert({
            'participant1':participant1,
            'dialogue1':dialogue1,
            'participant2':participant2,
            'dialogue2':dialogue2
        })
        response={
            'id':str(id),
            'participant1':participant1,
            'dialogue1':dialogue1,
            'participant2':participant2,
            'dialogue2':dialogue2
        }
        return response
    else:
        return not_found


@app.route('/users',method=['GET'])
def get_users():
    users =mongo.db.users.find()
    response=json_util.dumps(users)
    return response

@app.route('/users/<id>',methods=['GET'])
def get_user(id):
    user=mongo.db.users.find_one('_id':ObjectId(id))
    response =json_util.dumps(user)
    return response
    

@app.errorhandler(404)
def not_found(error=None):
    response=jsonity({
        'message':'Resource Noy Found' + request.url,
        'status':404
    })
    return response