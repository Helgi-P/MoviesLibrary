class MoviesLibrary:

    def __init__(self, genres):
        self.data = {}
        for genre in genres:
            self.data[genre] = []

    def add_movie(self, genre, title):
        if genre in self.data:
            self.data[genre].append(title)
        else:
            print(f"Жанр {genre} не найден в библиотеке")

    def recommend(self, genre):
        if genre in self.data:
            return self.data[genre]
        else:
            print(f"Жанр {genre} не найден в библиотеке")
            return []


if __name__ == '__main__':
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика', 'Арт-хаус'])

    library.add_movie('Комедия', 'Весёлый питонист')
    library.add_movie('Комедия', 'Три разраба и тестировщик')
    library.add_movie('Ужасы', 'Питон в ночи')
    library.add_movie('Арт-хаус', 'Доктор-питонист')

    print(library.recommend('Комедия'))
    print(library.recommend('Ужасы'))
    print(library.recommend('Арт-хаус'))
    print(library.recommend('Фантастика'))