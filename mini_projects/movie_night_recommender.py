import time


def debug_call(func):

    def wrapper(*args , **kwargs):

        print(f"Function: {func.__name__}")
        print(f"Arguments: {args} {kwargs}")

        result = func(*args, **kwargs)

        print(f"Returned: {result}")

        return result
    return wrapper

def measure_time(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"It took the function {end_time- start_time} s")

        return result
    return wrapper

def validate_positive_n(func):

    def wrapper(*args , **kwargs):
        result = func(*args ,**kwargs)
        n = args[1]
        if n <= 0:
            raise ValueError("n must be positive")

        return result
    return wrapper



class Movie:

    def __init__(self, title , genre , year , minutes , rating):

        self.title = title
        self.genre = genre
        self.year = year
        self.minutes = minutes
        self.rating = rating
        self.watched = False
        self.tags = set()

    def __repr__(self):
        return f"{self.title} ({self.rating})"

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

    @measure_time
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

    def total_watch_time(self):
        return sum(movie.minutes for movie in self.movies)


    def longest_movie(self):
        longest = max(self.movies, key=lambda m: m.minutes)
        return longest.short()

    def count_by_genre(self):

        m_dict = {}

        for movie in self.movies:
            for genre in movie.genre:
                if genre  not in m_dict:
                    m_dict[genre] = 1
                else:
                    m_dict[genre]+=1
        return m_dict


    @validate_positive_n
    def top_rated(self,n=3):
        highest_rating = sorted(self.movies , key = lambda movie: movie.rating , reverse=True)

        return [movie.short() for movie in highest_rating[:n]]






lib = Library()

m1 = Movie("Interstellar", ["Sci-Fi"], 2014, 169, 8.6)
m2 = Movie("Inception", ["Action"], 2010, 148, 8.8)
m3 = Movie("Gladiator", ["Action"], 2000, 111, 10.0)
m4 = Movie("Catch me if you can", ["Drama"], 2005, 128, 6.8)
m5 = Movie("The girl next door", ["Comedy"], 2016, 140, 2.8)
m6 = Movie("The girl next door 2", ["Comedy"], 2016, 140, 2.8)

lib.add_movie(m1)
lib.add_movie(m2)
lib.add_movie(m3)
lib.add_movie(m4)
lib.add_movie(m5)
lib.add_movie(m6)

lib.longest_movie()
lib.top_rated(-1)





