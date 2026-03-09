import random
import time
from functools import wraps



def debug_call(func):

    @wraps(func)
    def wrapper(*args , **kwargs):

        print(f"Function: {func.__name__}")
        print(f"Arguments: {args} {kwargs}")

        result = func(*args, **kwargs)

        print(f"Returned: {result}")

        return result
    return wrapper

def measure_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"It took the function {end_time- start_time} s")

        return result
    return wrapper

def validate_positive_n(func):

    @wraps(func)
    def wrapper(*args , **kwargs):
        n = args[1]
        if n <= 0:
            raise ValueError("n must be positive")
        result = func(*args, **kwargs)
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
        self.load_from_file("movies.txt")


    def add_movie(self,movie):
        duplicate_new = next(filter(lambda m: m.title.lower() == movie.title.lower() , self.movies), None)
        if  duplicate_new:
            return False


        self.movies.append(movie)
        self.save_to_file("movies.txt")

        return True

    def list_all(self):
        return [movie.short() for movie in self.movies]

    def list_unwatched(self):

        return [movie.short() for movie in self.movies if movie.is_unwatched()]

    def mark_watched_by_title(self, title):
        movie = next(filter(lambda m: m.title.lower() == title.lower(), self.movies ), None)
        if movie:
            movie.mark_watched()
            self.save_to_file("movies.txt")
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

        return [movie.short() for movie in self.movies if keyword.lower() in movie.title.lower()]

    def remove_movie_by_title(self, title):
        movie = next(filter(lambda m: m.title.lower() == title.lower(), self.movies), None)

        if movie:
            self.movies.remove(movie)
            self.save_to_file("movies.txt")
            return True
        return False

    def average_rating(self):
        if not self.movies:
            return 0

        return sum(movie.rating for movie in self.movies) / len(self.movies)

    def total_watch_time(self):
        return sum(movie.minutes for movie in self.movies)


    def longest_movie(self):
        if not self.movies:
            return None

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

    def recommend_random_unwatched(self):
        result = [movie.short() for movie in self.movies if movie.is_unwatched()]
        if not result:
            return "No unwatched movies"

        return random.choice(result)



    def save_to_file(self,filename):

        with open(filename , "w" , encoding="utf-8") as f:
            for movie in self.movies:
                f.write(f"{movie.title}|{', '.join(movie.genre)}|{movie.year}|{movie.minutes}|{movie.rating}|{movie.watched}\n")

    def load_from_file(self,filename):
        self.movies = []
        try:

            with open(filename , "r" , encoding="utf-8") as f:

                for line in f:
                    line = line.strip()

                    if not line:
                        continue

                    title, genre , year , minutes , rating , watched  = line.split("|")
                    genre = genre.split(",")
                    year = int(year)
                    minutes = int(minutes)
                    rating = float(rating)
                    watched = watched == "True"

                    movie = Movie(title, genre ,year ,minutes ,rating)
                    movie.watched = watched

                    self.movies.append(movie)

        except FileNotFoundError:
            print("No file was found")


    def export_stats(self):
        genre_lines = "\n".join(
            [f"- {genre}: {count}" for genre, count in self.count_by_genre().items()])

        return (f"Movies in library: {len(self.movies)}\n"
                f"Average rating: {self.average_rating():.2f}\n"
                f"Total watch time: {self.total_watch_time()} minutes\n"
                f"Longest movie: {self.longest_movie()}\n"
                f"Genres:\n{genre_lines}")




def main():
    lib = Library()


    while True:
        print("1 Add movie")
        print("2 List movies")
        print("3 Mark watched")
        print("4 Recommend movie")
        print("5 Show stats")
        print("6 Exit")

        choice = input("Please enter an option:")

        if choice == "1":
            title = input("Please enter your movie's title:")
            genre = [input("Please enter your movie's genre:").strip()]
            try:
                year = int(input("Please enter your movie's year:"))
                minutes = int(input("Please enter your movie's length:"))
                rating = float(input("Please enter your movie's rating:"))
            except ValueError:
                print("Invalid input")
                continue

            movie = Movie(title,genre,year,minutes,rating)
            lib.add_movie(movie)
            print("Movie added")

        elif choice == "2":
            if not lib.movies:
                print("There is no movies to be listed")
                continue

            for movie in lib.movies:
                print(movie.short())

        elif choice =="3":
            if not lib.movies:
                print("The list is empty")
                continue

            title = input("Please enter the name of the movie you have watched: ").strip()

            if lib.mark_watched_by_title(title):
                print(f"You just marked {title} as watched!")
            else:
                print("Movie not found")


        elif choice == "4":


            genre = input("Genre (Press enter to skip): ").strip()
            if genre == "":
                genre = None

            max_minutes = input("Max minutes (Press enter to skip): ")
            if max_minutes == "":
                max_minutes = None
            else:
                max_minutes = int(max_minutes)

            min_rating = input("Minimum rating (Press enter to skip): ")
            if min_rating == "":
                min_rating = None
            else:
                min_rating = float(min_rating)

            only_unwatched = input("Only unwatched? (Enter=yes / n=no): ").strip().lower()

            if only_unwatched == "":
                only_unwatched = True
            elif only_unwatched in ("n", "no", "false"):
                only_unwatched = False
            else:
                only_unwatched = True

            top_n = input("How many movies you want me to recommend ? (Press enter to skip))")
            if top_n == "":
                top_n = 5
            else :
                top_n = int(top_n)


            result =lib.recommend(genre,max_minutes,min_rating,only_unwatched,top_n)

            if not result:
                print("No matching movies found")
            else:
                for movie in result:
                    print(movie)


        elif choice  == "5":
            print(lib.export_stats())


        elif choice == "6":
            break

        else:
            print("Invalid option")



if __name__ == "__main__":
    main()



