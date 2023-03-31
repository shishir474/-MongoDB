import pymongo
from pprint import pprint

# Create a MongoClient object.
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the database using the database name.
mydb = client["mydb"]
moviesCollection = mydb['movies']
usersCollection = mydb['users']
sessionsCollection = mydb['sessions']
commentsCollection = mydb['comments']
theatresCollection = mydb['theatres']





