def nellie_food(full_days_gone, partial_days_gone):
    food = 2
    food_needed = (full_days_gone * food) + (partial_days_gone * (food/2))
    medication = .5
    medication_needed = (full_days_gone + partial_days_gone) * medication
    return f"Nellie needs {food_needed} scoops of food and {medication_needed} pills"
    
print(nellie_food(4, 1))