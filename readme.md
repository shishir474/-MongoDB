To access MongoDB database, python needs a MongoDB driver. Here I have used PyMongo.
Use pip to install pymongo
To create a database in MongoDB, we first need to create a mongoClient object & then specify the connection url with the correct ip address and the name of the database you want to create
After creating database, create collections for movies, users, comments, theatres and sessions and import the data into these collections using mongoImport tool


# COMMENTS COLLECTION

Q.1 In this problem, we have to find top 10 users who made the maximum number of comments.Performed aggregate operation on comments collection where I have grouped the comments on the basis of the user's name and also maintained the comments count using sum function and then sort the result on basis of commentsCount and use limit 10 to get the top 10 users who made max number of comments.

Q.2 In this problem, we have to find top 10 movies with maximum comments. Performed aggregate operation on comments collection where I have grouped the comments on the basis of the movie_Id and also maintained the comments count using sum function and then sort the result on basis of commentsCount and use limit 10 to get the aggregate_result. Created a list lst which contains the movie_name and corresponding comment count. Iterate over this aggregate_result and populate the list. Created a pandas dataframe using this list containing 2 columns movie_name and comment_count

Q.3 In this problem, for a given year we have to find total number of comments created for each month in that year. Performed aggregate operation on comments collection, first used project operation to project the year and month from the given date using month and date operator.Then performed a match operation to match the records for the given year and then performed the grouping on the basis of month and maintained a count which indicates the total number of comments created for that month, sort the result and project the month and its correspoding comment count.


# MOVIES COLLECTION

Q.4 In this problem, we have to find top 10 movies with highest IMDB ratings. Used movies collection for this problem. First we have to discard all those records where IMDB ratings is equal to "" and then sort the records on the basis of imdb ratings in descending order and then used limit 10 tho get top 10 results.

Q.5 In this problem, we have to find top 10 movies with highest IMDB ratings in a given year. Used movies collection for this problem. First we have to discard all those records where IMDB ratings is equal to "" and year doesn't match with the given year. Then sort the records on the basis of imdb ratings in descending order and then used limit 10 tho get top 10 results.

Q.6 In this problem, we have to find top 10 movies with highest IMDB rating with number of votes > 1000. Used movies collection for this problem. First filter out the records where number of votes > 1000 & then sort this filtered data on the basis of IMDB ratings in descending order and use limit 10 to get the top 10 results.

Q.7 In this problem, we have to find top 10 movies with title matching a given pattern sorted by highest tomatoes ratings. Used movies collection for this problem. First filter out the records using the regex operator which is used to check the pattern & then sort this filtered data on the basis of tomatoes viewer rating in descending order and use limit 10 to get the top 10 results.

Q.8 In this problem, we have to find top 10 directors who created the maximum number of movies. Performed aggregate operation on the movies collection where first we need to unwind the directors array using unwind operator. Unwind operator deconstructs an array field from the input documents to output a document for each element. Then perform grouping on the basis of directors name and also maintained corresponding sum which represents the movie_count for that specific director, sort the result on the basis of movieCount and use limit 10 to get the top 10 directors who created max number of movies.

Q.9 In this problem, we have to find top 10 directors who created the maximum number of movies in a given year. Performed aggregate operation on the movies collection where first we need to filter those records whose year matches with the given year & then unwind the directors array using unwind operator. Unwind operator deconstructs an array field from the input documents to output a document for each element. Then perform grouping on the basis of directors name and also maintained corresponding sum which represents the movie_count for that specific director, sort the result on the basis of movieCount and use limit 10 to get the top 10 directors who created max number of movies in a given year.

Q.10 In this problem, we have to find top 10 directors who created the maximum number of movies for a given genre. Performed aggregate operation on the movies collection where we need to unwind the directors and genre array and then match the records with the given genre. Then perform grouping operation on the basis of director name and also maintain a corresponding movieCount using the sum function. Sort the result on basis of this movieCount in descending order and use limit 10 to get the top 10 directors

Q.11 In this problem, we have to find top 10 actors who starred in the maximum number of movies.Performed aggregate operation on the movies collection where first we need to unwind the cast array using unwind operator. Then group the records on basis of cast and also maintained corresponding movieCount which indicates num of movies in which that actor starred. Sort the result on basis of this movieCount in descending order and use limit 10 to get the top 10 actors who starred in max movies.

Q.12 In this problem, we have to find top 10 actors who starred in the maximum number of movies in a given year. Performed aggregate operation on the movies collection where first we need to filter the records whose year matches with the given year. Then unwind the cast array using unwind operator. Then group the records on basis of cast and also maintained corresponding movieCount which indicates num of movies in which that actor starred. Sort the result on basis of this movieCount in descending order and use limit 10 to get the top 10 actors who starred in max movies in given year.

Q.13 In this problem, we have to find top 10 actors who starred in the maximum number of movies in a given genre. Performed aggregate operation on the movies collection where first we need to match the given genre with the genres of the movie documents & then once we have the filtered result, unwind the cast array, perform grouping on basis of cast and maintain corresponding movieCount which indicates the movie count for that particular cast in the given genre. Sort the result on basis of this movieCount in descending order and use limit 10 to get the top 10 actors who starred in max movies in given genre.

Q.14 In this problem, we have to find top 10 movies for each genre with the highest IMDB rating. First we need to get all the genres. For this performed aggregate operation on movies collection, unwind the genre and then perform grouping on basis of genre. Loop over the genres extracted in the first part and for each genre perform aggregate operation where we first match the genre and also ensure that imdb rating is not empty.Then sort the result on basis of IMDB ratings in descending order and use limit 4 to get the top 4 movies in that particular genre. 

# THEATRES COLLECTION

Q.15 In this problem, we have to find Top 10 cities with the maximum number of theatres. Performed aggregate operation on the theatres collection where we need to group the records on basis of location.address.city and also need to maintain corresponding theatres count indicating number of theatres in that city. Sort the result on basis of theatresCount in descending order & use limit 10 to get the top 10 cities with max number of theatres

Q.16 In this problem, we have to find top 10 theatres nearby given coordinates. Here we need to create index on the location field. Geonear operator requires indexing on our geolocation object. Performed aggregate operation on the theatres collection. Used geonear operator which outputs documents in order of nearest to farthest from a specified point. In geonear we have to specify the coordinates and the location type. Finally used limit 10 to get the top 10 nearest theatres from the given coordinates






 




