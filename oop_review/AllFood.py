from .Food import Food

class AllFood:
    def __init__(self):
        self.food = []
        self.candy_list = []
    
    def add_food(self, food):
        self.food.append(food)
        if food.is_candy:
            self.candy_list.append(food.name)

    def get_candy(self):
        return self.candy_list

all_food = AllFood()
starburst = Food(True, 100, "starburst")
hamburger = Food(False, 500, "hamburger")
reeses = Food(True, 0, "reeses")
all_food.add_food(starburst)
all_food.add_food(hamburger)
all_food.add_food(reeses)
print(all_food.get_candy())
