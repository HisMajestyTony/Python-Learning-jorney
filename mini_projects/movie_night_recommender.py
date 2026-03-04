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

    def list_unwatched(self):
        result = list(
            map(Movie.short,
                filter(Movie.is_unwatched, self.movies)
                )
        )
        return result

    def mark_watched_by_title(self, title):
        movie = next(filter(lambda m: m.title.lower() == title.lower(), self.movies ), None)
        if movie:
            movie.mark_watched()
            return True
        else :
            return  False

    def recommend(self, genre=None, max_minutes=None, min_rating=None, only_unwatched=True, top_n=5):
        candidates = self.movies

        if only_unwatched:
            candidates = filter(Movie.is_unwatched, candidates)

        if genre:
            candidates = filter(lambda m: genre.lower() in [g.lower() for g in m.genre], candidates)

        if max_minutes is not None:
            candidates = filter(lambda m: m.minutes <= max_minutes, candidates)

        if min_rating is not None:
            candidates = filter(lambda m: m.rating >= min_rating, candidates)

        candidates = sorted(candidates, key=lambda m: m.rating, reverse=True)[:top_n]

        return list(map(Movie.short, candidates))

    def search_by_title(self,keyword):
        movies = self.movies

        movies = list(
            map(Movie.short,filter(lambda movie: keyword.lower() in movie.title.lower(), self.movies)
        ) )

        return movies

    def remove_movie_by_title(self, title):
        movie = next(filter(lambda m: m.title.lower() == title.lower(), self.movies), None)

        if movie:
            self.movies.remove(movie)
            return True
        return False

    def average_rating(self):
        if not self.movies:
            return 0

        return sum(movie.rating for movie in self.movies) / len(self.movies)





lib = Library()

m1 = Movie("Interstellar", ["Sci-Fi"], 2014, 169, 8.6)
m2 = Movie("Inception", ["Action"], 2010, 148, 8.8)

lib.add_movie(m1)
lib.add_movie(m2)
lib.mark_watched_by_title("Inception")
lib.mark_watched_by_title("Interstellar")


#print(lib.search_by_title("Inter"))
print(lib.average_rating())







