

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

def imbd5 (movie):
    return movie["imdb"] > 5.5

print(imbd5(movies[1]))


def movielist(movie):
    goodmovies = []
    for i in movie:
        if i["imdb"] > 5.5:
            goodmovies.append(i)

    return goodmovies

print(movielist(movies))

def moviecategory(movie, categor):
    moviecat = []
    for i in movie:
        if i["category"].lower() == categor.lower():
            moviecat.append(i)

    return moviecat


print(moviecategory(movies, "Romance"))

def averagepoints(movie):
    sum = 0
    for i in  movie:
        sum += i["imdb"]
    return sum/len(movie)

print(averagepoints([movies[1], movies[2]]))

def averagecat(movie, categor):
    moviecat =[]
    sum = 0

    for i in movie:
        if i["category"] == categor:
            moviecat.append(i)

    for i in moviecat:
        sum += i["imdb"]

    return sum/len(moviecat)

print(averagecat(movies, "Romance"))



