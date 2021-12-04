from pymongo import MongoClient

client =  MongoClient('localhost', 27017) # mongodb python 접속
db = client.dbsparta # dbsparta 이름의 데이터베이스 생성 ( get or create)

# adding users collection document
# db.users.insert_one({'name': '덤블도어', 'age': 116})

all_users = list(db.users.find())
users = list(db.users.find({'age': 116}))
for user in users:
    print(user)
dumbledore = db.users.find_one({'age': 116})
print(dumbledore)