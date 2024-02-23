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

#Ex 1
def more_than_5(movie):
    return movie.get("imdb") > 5.5

for movie in movies:
    if more_than_5(movie):
        print('True')
    else:
        print('False')

#Ex 2
def imdb_more_than_5_2(movie):
    return movie.get("imdb", 0) > 5.5

list = [movie for movie in movies if imdb_more_than_5_2(movie)]
for movie in list:
    print(f"{movie['name']} {movie['imdb'] } {movie['category']}")

#Ex 3
def category(category):
    return[movie for movie in movies if movie['category'] == category]

category_input = category(input(""))
print(category_input)

#Ex 4
def average_score(movies):
    total = 0
    num_mov = 0
    for movie in movies:
        total = movie['imdb']
        num_mov += 1
    return total / num_mov

average = average_score(movies)
print(average) 

#Ex 5
def mov_category(category):
    return[movie for movie in movies if movie['category'] == category]

def avg_score(movies):
    total = 0
    num_mov = 0
    for movie in movies:
        total = movie['imdb']
        num_mov += 1
    return total / num_mov

def avg_of_category(category):
    movies = mov_category(category)
    return avg_score(movies)

average_score = avg_of_category(input(""))
print(average_score)
