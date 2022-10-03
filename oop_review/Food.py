class Food:
    # attributes - info
    # init funcition - what to do when we create an instance
    # methods - behavior
    def __init__(self, is_candy, calories = None, name = None):
        self.is_candy = is_candy
        self.calories = calories
        self.name = name
    
    def beg(self, custom_beg):
        print(custom_beg)
    


# adding this if statement so code doesn't run when imported
if __name__ == "__main__":
    # create class instances
    starburst = Food(True, 100, "starburst")
    hamburger = Food(False, 500, "hamburger")
    reeses = Food(True, 0, "reeses")

    food_list = [starburst, hamburger, reeses]

    # access name attribute
    print(starburst.name)
    print(hamburger.name)
    print(reeses.name)
    
    # iterating over objects
    candy_list = []
    for food in food_list:
        if food.is_candy:
            candy_list.append(food.name)

    print(candy_list)