from config import moviesCollection
from pprint import pprint


def printRes(res):
    for i in res:
        pprint(i)


class Movies():
    def top_ten_movies_with_highest_imdb(self):
        res = moviesCollection.find({"imdb.rating": {"$ne":""}},{"title":1,"imdb":1}).sort("imdb.rating",-1).limit(10)
        printRes(res)


    def top_ten_movies_with_highest_imdb_in_given_year(self,year):
        res = moviesCollection.find({"imdb.rating": {"$ne":""}, "year":year},{"title":1,"imdb":1}).sort("imdb.rating",-1).limit(10)
        printRes(res)


    def top_ten_movies_with_highest_IMDB_rating_with_number_of_votes_greaterthan_1000(self):
        res = moviesCollection.find({"imdb.votes": {"$gt":1000}}, {"title":1, "imdb":1}).sort("imdb.rating",-1).limit(10)
        printRes(res)


    def movies_with_highest_tomato_ratings(self,pattern):
        res = moviesCollection.find({"title": {"$regex": pattern}}, {"title":1, "tomatoes.viewer":1}).sort("tomatoes.viewer.rating",-1).limit(10)
        printRes(res)

    
    def top_ten_directors_who_created_max_movies(self): 
        # unwind operator Deconstructs an array field from the input documents to output a document for each element.
        res = moviesCollection.aggregate(
            [
                {"$unwind":"$directors"},
                {"$group": {"_id":"$directors", "movieCount": {"$sum":1}} }, 
                {"$sort": {"movieCount": -1}}, 
                {"$project": {"Director": "$_id", "movieCount":1, "_id":0} },
                {"$limit":10}
            ]
        )
        printRes(res)


    def top_ten_directors_who_created_max_movies_in_specific_year(self,year): 
        res = moviesCollection.aggregate(
            [   {"$match": {"year": year}},
                {"$unwind":"$directors"},
                {"$group": {"_id":"$directors", "movieCount": {"$sum":1}} }, 
                {"$sort": {"movieCount": -1}}, 
                {"$project": {"Director": "$_id", "movieCount":1, "_id":0} },
                {"$limit":10}
            ]
        )
        printRes(res)

    
    def top_ten_directors_who_created_max_no_of_movies_for_given_genre(self,genre):
        res = moviesCollection.aggregate([
            {"$unwind":"$directors"}, 
            {"$unwind":"$genres"}, 
            {"$match": {"genres":genre}}, 
            {"$group": {"_id":"$directors", "movieCount":{"$sum":1}} }, 
            {"$sort": {"movieCount": -1}},
            {"$limit": 10}
        ])
        printRes(res)


    def top_ten_actors_who_starred_in_max_movies(self):
        res = moviesCollection.aggregate([
            {"$unwind":"$cast"}, 
            {"$group": {"_id":"$cast", "movieCount":{"$sum": 1}} }, 
            {"$project": {"Name":"$_id", "movieCount":1, "_id":0}},
            {"$sort": {"movieCount":-1}},
            {"$limit":10}
        ])
        printRes(res)
    

    def top_ten_actors_who_starred_in_max_movies_in_given_year(self,year):
        res = moviesCollection.aggregate([
            {"$unwind":"$cast"}, 
            {"$match": {"year": year}},
            {"$group": {"_id":"$cast", "movieCount":{"$sum": 1}} }, 
            {"$project": {"Name":"$_id", "movieCount":1, "_id":0}},
            {"$sort": {"movieCount":-1}},
            {"$limit":10}
        ])
        printRes(res)


    def top_ten_actors_who_starred_in_max_movies_in_given_genre(self,genre):
        res = moviesCollection.aggregate([
            {"$match": {"genres":genre}},
            {"$unwind":"$cast"}, 
            {"$group": {"_id":"$cast", "movieCount":{"$sum": 1}} }, 
            {"$project": {"Name":"$_id", "movieCount":1, "_id":0}},
            {"$sort": {"movieCount":-1}},
            {"$limit":10}
        ])
        printRes(res)


    def top_ten_movies_for_each_genre_with_highest_imdb_rating(self):
        genres = moviesCollection.aggregate([{"$unwind":"$genres"}, {"$group":{"_id":"$genres"}}])
        for i in genres:
            genre = i['_id']
            res = moviesCollection.aggregate(
                [   
                    {"$match": {"genres":genre, "imdb.rating": {"$ne":""} }},
                    {"$sort": {"imdb.rating":-1}}, 
                    {"$limit":4}
                ])
            print(genre)
            printRes(res)
            print('------------------------------------------')


def main():
    obj = Movies()

    print("""
            Enter Choice:
            1. Top 10 movies with highest imdb
            2. Top 10 movies with highest imdb in a given year
            3. Top 10 movies with highest imdb ratings and number of votes greater than 1000
            4. Top 10 movies with highest tomato ratings
            5. Top 10 directors who created max movies
            6. Top 10 directors who created max movies in a given year
            7. Top 10 directors who created max movies for a given genre
            8. Top 10 actors who starred in max movies
            9. Top 10 actors who starred in max movies in a given year
            10.Top 10 actors who starred in max movies in a given genre
            11.Top 10 movies in each genre with highest imdb ratings
            """)
    
    ch=int(input())
    if ch == 1:
        obj.top_ten_movies_with_highest_imdb()
    elif ch==2:
        year = input("Enter the year for which you want to see month wise comment count: \n")
        try:
            valid_year = int(year)
            obj.top_ten_movies_with_highest_imdb_in_given_year(valid_year)
        except ValueError:
            print("please enter a valid year. Only numerical value is allowed")
    elif ch==3:
        obj.top_ten_movies_with_highest_IMDB_rating_with_number_of_votes_greaterthan_1000()
    elif ch==4:
        # REGEX for movie names starting with D
        pattern='^D'
        obj.movies_with_highest_tomato_ratings(pattern)
    elif ch==5:
        obj.top_ten_directors_who_created_max_movies()
    elif ch==6:
        year = input("Enter the year: \n")
        try:
            valid_year = int(year)
            obj.top_ten_directors_who_created_max_movies_in_specific_year(valid_year)
        except ValueError:
            print("please enter a valid year. Only numerical value is allowed")
    elif ch==7:
        obj.top_ten_directors_who_created_max_no_of_movies_for_given_genre("Short")
    elif ch==8:
        obj.top_ten_actors_who_starred_in_max_movies()
    elif ch==9:
        year = input("Enter the year: \n")
        try:
            valid_year = int(year)
            obj.top_ten_actors_who_starred_in_max_movies_in_given_year(valid_year)
        except ValueError:
            print("please enter a valid year. Only numerical value is allowed")
    elif ch==10:
        obj.top_ten_actors_who_starred_in_max_movies_in_given_genre("Action")
    elif ch==11:
        obj.top_ten_movies_for_each_genre_with_highest_imdb_rating()
    else:
        print("Wrong choice")
        


if(__name__=="__main__"):
    main()