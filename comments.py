from config import commentsCollection
from config import moviesCollection
import pandas as pd

class Comment():
    def top10UserWithMaxComment(self):
        agg_res = commentsCollection.aggregate(
            [
                {"$group": {"_id":"$name", "commentCount":{"$sum": 1}}}, 
                {"$sort": {"commentCount": -1}}, {"$limit": 10}
            ]
        )
        for i in agg_res:
            print(i)
    

    def top10MoviesWithMaxComment(self):
        agg_res = commentsCollection.aggregate(
            [
                {"$group":{"_id":"$movie_id", "commentCount":{"$sum": 1}}}, 
                {"$sort": {"commentCount": -1}}, {"$limit": 10}
            ]
        )
        
        lst = list()
        for i in agg_res:
            strId = i['_id']
            commentCount = i['commentCount']
            movie = moviesCollection.find_one({"_id" : strId})
            res = ( movie['title'],commentCount)
            lst.append(res)

        df = pd.DataFrame(lst, columns=['Movie_name', 'CommentCount'])
        df.set_index('Movie_name', inplace=True)
        print(df.head())


    def monthWiseComment(self, year):
        agg_res = commentsCollection.aggregate(
            [
                {"$project": { "year":{"$year":"$date"}, "month":{"$month":"$date"} }}, 
                {"$match": {"year":year}},  
                {"$group": {"_id":"$month", "count": {"$sum": 1} } },  
                {"$sort": {"_id":1}},  
                {"$project": {"month":"$_id", "count":1, "_id":0}}
            ]
        )

        for i in agg_res:
            print(i)


  


def main():
    obj = Comment()

    print("""
            Enter Choice:
            1. Top 10 users with most comments
            2. Top 10 movies with most comments
            3. For a given year, comments made every month
            """)
    ch=int(input())
    if ch == 1:
        obj.top10UserWithMaxComment()
    elif ch==2:
        obj.top10MoviesWithMaxComment()
    elif ch==3:
        year = input("Enter the year for which you want to see month wise comment count: \n")
        try:
            valid_year = int(year)
            obj.monthWiseComment(valid_year)
        except ValueError:
            print("please enter a valid year. Only numerical value is allowed")
    else:
        print("Wrong choice")
        

    

if(__name__=="__main__"):
    main()