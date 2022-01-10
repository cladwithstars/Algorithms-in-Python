def solution(dishes):
    """
    You are given a list of dishes, where each element consists of a list of strings beginning 
    with the name of the dish, followed by all the ingredients used in preparing it. 
    You want to group the dishes by ingredients, 
    so that for each ingredient you'll be able to find all the dishes that contain it 
    (if there are at least 2 such dishes).

    Return an array where each element is a list beginning with the ingredient name, followed by
    the names of all the dishes that contain this ingredient. The dishes inside each list should 
    be sorted lexicographically, and the result array should be sorted lexicographically by the
    names of the ingredients.
    """
    d = dict()
    for dish in dishes:
        for ingredient in dish[1:]:
            if ingredient not in d:
                d[ingredient] = [dish[0]]
            else:
                d[ingredient].append(dish[0])
    
    outputMatrix = []
    for key in d:
        if len(d[key]) > 1:
            outputMatrix.append([key] + sorted(d[key]) )
            
    #now need to sort array lexigraphiicaly based on ingredient
    return sorted(outputMatrix, key=lambda x: x[0])

dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

print(solution(dishes))
"""
expecting 
[["Cheese", "Quesadilla", "Sandwich"],
["Salad", "Salad", "Sandwich"],
["Sauce", "Pizza", "Quesadilla", "Salad"],
["Tomato", "Pizza", "Salad", "Sandwich"]]
"""