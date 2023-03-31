from config import theatresCollection
from pprint import pprint

def printRes(res):
    for i in res:
        pprint(i)


class Theatres():
    def top_ten_cities_with_max_theatres(self):
        res = theatresCollection.aggregate([
           {"$group": {"_id":"$location.address.city", "theatresCount":{"$sum":1}}}, 
           {"$sort": {"theatresCount":-1}},
           {"$limit": 10}
        ])  
        printRes(res)


    def top_ten_theatres_nearby_given_theatre(self):
        res = theatresCollection.aggregate([
            {"$geoNear": {"near":{ "type": "Point", "coordinates": [ -73.99279 , 40.719296 ] }, 
                "distanceField":"dist.calculated", 
                "maxDistance":10000, 
                "includeLocs": "dist.location", 
                "spherical":"true"
            }},
            {"$limit":6}
        ])
        print(res)
        printRes(res)

    

def main():
    obj = Theatres()
    
    obj.top_ten_cities_with_max_theatres()

    obj.top_ten_theatres_nearby_given_theatre()

if(__name__=="__main__"):
    main()
