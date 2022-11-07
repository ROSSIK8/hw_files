with open('cook book.txt', encoding='utf-8',) as file:
    cook_book = {}
    cook_book_list = [item.strip() for item in file.readlines()] + ['']
    for _ in range(cook_book_list.count('')):
        dish = cook_book_list.pop(0)
        quantity = int(cook_book_list.pop(0))
        cook_book[dish] = []
        for __ in range(quantity):
            ingredient = cook_book_list.pop(0).split(' | ')
            cook_book[dish].append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
        cook_book_list.pop(0)
    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    for item in dishes:
        for elem in cook_book[item]:
            if elem['ingredient_name'] not in dishes_dict:
                dishes_dict[elem['ingredient_name']] = {'measure': elem['measure'], 'quantity': elem['quantity'] * person_count}
            else:
                dishes_dict[elem['ingredient_name']]['quantity'] += elem['quantity'] * person_count
    return dishes_dict

print()
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 123))
