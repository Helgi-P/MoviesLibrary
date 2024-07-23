from main import MoviesLibrary


def test_if_one_genre():
    library = MoviesLibrary(['Триллер'])

    library.add_movie('Триллер','Питонист и анаконда')
    library.add_movie('Триллер', 'Блуждание в питоне')

    assert ['Питонист и анаконда', 'Блуждание в питоне'] == library.recommend('Триллер')


def test_if_many_genres():
    library = MoviesLibrary(['Триллер', 'Арт-хаус'])

    library.add_movie('Триллер','Питон и анаконда')
    library.add_movie('Триллер', 'Блуждание в питоне')
    library.add_movie('Арт-хаус', 'Доктор-питонист')

    assert ['Доктор-питонист'] == library.recommend('Арт-хаус')







