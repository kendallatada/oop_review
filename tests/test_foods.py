import pytest
from oop_review.Food import Food
from oop_review.AllFood import AllFood

# test beg
def test_food_attributes_created():
    #Arrange / Act
    noodles = Food(False, 600, "Noodles")

    #Assert
    assert noodles.is_candy == False
    assert noodles.calories == 600
    assert noodles.name == "Noodles"
