import pymongo
import random
from imgs import images

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydb"]

col = mydb["profile"]

def create_room(room_name, number_of_players, number_of_rounds):
    code = random.randint(1111,9999)
    rounds = []
    for i in range(number_of_rounds):
        a = i+1
        round = {
            "round": a,
            "imgSrc": random.choice(images)
        }
        rounds.append(round)

    query = {"roomName": room_name,
             "code": code,
             "numberOfPlayers": number_of_players,
             "numberOfRounds": number_of_rounds,
             "rounds": rounds
             }
    col.insert_one(query)
    response = {
        "nazwa pokoju": room_name,
        "kod dostępu": code,
    }
    return response

def get_rooms():
    project = {"$project":
                   {
                       "_id": 0,
                       "roomName": 1
                   }}
    sort_by_room_name={"$sort": {"roomName":1}}

    question = [project, sort_by_room_name]

    response = []
    rooms = col.aggregate(question)
    for room in rooms:
        response.append(room)
    return response

def find_room(name, code):
    query = {
        "roomName": name,
        "code": code
    }
    projection = {
        "_id": 0,
        "roomName": 1,
        "rounds": 1
    }
    room = col.find_one(query, projection)
    return room