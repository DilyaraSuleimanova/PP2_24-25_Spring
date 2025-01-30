# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]  


# # 1 task
# def imdb_great(name):
#     for movie in movies:
#         if movie["name"] == name and movie["imdb"] > 5.5:
#             return True
#     return False

# movie_name = input("Enter the name of movie: ")
# print(imdb_great(movie_name))


# # 2 task
# def imdb_less_5():
#     sublist = []
#     for movie in movies:
#         if movie["imdb"] < 5.5:
#             sublist.append(movie)
#     [print(x) for x in sublist]

# imdb_less_5()


# # 3 task
# def by_category(category):
#     for movie in movies:
#         if movie["category"] == category:
#             print(movie['name'])

# category = input("Enter the category of movies: ")
# by_category(category)


# # 4 task
# def avg_imdb():
#     sum = 0
#     for movie in movies:
#         sum += movie["imdb"]
#     print (f"The average of IMDB: {sum / len(movies):.1f}")

# avg_imdb()


# # 5 task
# def avg_imdb_by_category(category):
#     sum = 0
#     cnt_movies = 0
#     for movie in movies:
#         if movie["category"] == category:
#             sum += movie["imdb"]
#             cnt_movies += 1
#     print (f"The average of IMDB on category {category}: {sum / cnt_movies:.1f}")

# category = input("Enter the category of movies: ")
# avg_imdb_by_category(category)