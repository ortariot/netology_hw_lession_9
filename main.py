with open('recipes.txt', encoding='utf-8') as f:
    out = {}
    for line in f:
        dish = line.strip()
        num = int(f.readline().strip())
        i = 0
        ingr = []
        while True:
            if i == num:
                break
            i += 1
            ingr_str = f.readline().strip()
            row = {}
            row['ingredient_name'] = ingr_str[0 : ingr_str.find(' | ')]
            row['quantity'] = int(ingr_str[ingr_str.find(' | ') + 3 : ingr_str.rfind(' | ')])
            row['measure'] = ingr_str[ingr_str.rfind(' | ') + 3:]
            ingr.append(row)
        out[dish] = ingr
        f.readline()


    print(out)