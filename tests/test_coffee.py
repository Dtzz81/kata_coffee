from src.kata_coffee.coffee import how_much_coffee


def test_solve_some_kata_lower_case():
    assert how_much_coffee(["cw"]) == 1

def test_walk_a_cat_lower_case():
    assert how_much_coffee(["cat"]) == 1

def test_walk_a_dog_lower_case():
    assert how_much_coffee(["dog"]) == 1

def test_watch_a_movie_lower_case():
    assert how_much_coffee(["movie"]) == 1

def test_solve_some_kata_upper_case():
    assert how_much_coffee(["CW"]) == 1

def test_walk_a_cat_upper_case():
    assert how_much_coffee(["CAT"]) == 1

def test_walk_a_cat_and_a_dog():
    assert how_much_coffee(["cat""dog"]) == 2
