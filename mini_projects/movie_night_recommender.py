class Movie:

    def __init__(self, title , genre , year , minutes , rating):

        self.title = title
        self.genre = genre
        self.year = year
        self.minutes = minutes
        self.rating = rating
        self.watched = False
        self.tags = set()

    def mark_watched(self):
        self.watched = True

    def short(self):
        return f"{self.title} ({self.year}) * {', '.join(self.genre)} * {self.rating}"

    def is_unwatched(self):
        return not self.watched


class Library:

    def __init__(self):

        self.movies = []

    def add_movie(self,movie):
        self.movies.append(movie)

    def list_all(self):
        result = list(map(Movie.short, self.movies))
        return result





movie1 = Movie("Interstellar" , ["Sci-Fi"] , 2014 , 169 , 8.6)
movie2 = Movie("Boomer" , ["Sci-Fi"] , 2014 , 169 , 8.6)

new_library = Library()
new_library.add_movie(movie2)
new_library.add_movie(movie1)
new_library.list_all()
print(new_library.list_all())


