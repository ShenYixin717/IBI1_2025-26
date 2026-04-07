# define food_item
class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

#define the function for calculation
def track_nutrition(food_list):
    total_cal = 0
    total_pro = 0
    total_carbs = 0
    total_fat = 0
    for food in food_list:
        total_cal += food.calories
        total_pro += food.protein
        total_carbs += food.carbs
        total_fat += food.fat
    reply = (f"You have taken {total_cal} calories, {total_pro}g proteins, {total_carbs}g carbs and {total_fat}g fat. \n")
    
    #warn if their are too much calories or fat
    if total_cal > 2500:
        reply += "Warning: You have taken too much calories \n"
    if total_fat > 90:
        reply += "Warning: You have taken too much fat \n"

    return(reply)


#example
apple = food_item("apple", 60, 0.3, 15, 0.5)
rice = food_item("rice", 130, 2.7, 28, 0.3)
chicken = food_item("chicken", 165, 31, 0, 3.6)
chocolate = food_item("chocolate", 540, 5, 55, 30)
consumed_food = [apple, rice, chicken, chocolate, chocolate,chocolate,chocolate,chocolate]
print(track_nutrition(consumed_food))