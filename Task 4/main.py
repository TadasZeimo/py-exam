# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title, director, budget):
        self.title = str(title)
        self.director = str(director)
        self.budget = int(budget)

    def __str__(self) -> str:
        return f'Title: {self.title}, Director: {self.director}, Budget: {self.budget}.'

    def wasExpensive(self):
        if self.budget > 1e+8:
            return True
        else:
            return False


terminator = Movie('The Terminator', 'James Cameron', 6400000)
print(terminator)
print(terminator.wasExpensive())


got = Movie('Game of Thrones', 'David Benioff & D. B. Weiss', 2e+9)
print(got)
print(got.wasExpensive())
