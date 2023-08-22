## function to sort the given list and its strings in alphabitical order ##
def in_alphabitical_order(new_str):
    words = [word.lower() for word in new_str]
    words.sort()
    counter=0
    for e in new_str:
        original = new_str[counter]
        counter+=1
        if e.lower() == words[0]:
            return original

## function that take a object(line) and a warehouse(matamikya)
# and add the object to the warehouse in its specific place ##
def add_product(line, matamikya):
    for k in matamikya:
        if k[0] == line[2]:
            return
    if float(line[3]) < 0:
        return
    if float(line[4]) < 0:
        return
    new_list = [line[2], float(line[3]), float(line[4]), 0]
    matamikya.append(new_list)



## function that take a object(line) and a warehouse(matamikya) and change the amount of the object in its warehouse
# to the new required amount ##
def change_amount(line, matamikya):
    if len(matamikya)==0:
        return
    for k in matamikya:
        if k[0] == line[2]:
            k[2] = k[2] + float(line[3])


## function that take a object(line) and a warehouse(matamikya)
# and ship the order (remove it from the warehouse) ##
def ship_order(line, matamikya):
    counter = 5
    if len(matamikya)==0:
        return
    for k in matamikya:
        x=line[2]
        y=k[0]+ ','
        if y == x:
            if k[2] >= float(line[3]):
                if float(line[3]) < 0 :
                    continue
                else:
                   k[2] = k[2] - float(line[3])
                   k[3] += k[1] * float(line[3])
                break
    cond = True
    length = len(line)
    if not (length < counter):
       while cond:
            size=0
            for k in matamikya:
                size+=1
                x = line[counter]
                y = k[0] + ','
                if not y==x:
                    if size >= len(matamikya):
                     counter+=3
                    if counter >= length:
                        cond = False
                        break
                if y == x:
                    size=0
                    if k[2] >= float(line[counter + 1]):
                        if float(line[counter + 1]) > 0 :
                           k[2] = k[2] - float(line[counter + 1])
                           k[3] += k[1] * float(line[counter + 1])
                        counter += 3
                        if counter >= length:
                            cond=False
                            break
                    else:
                        counter += 3
                        if counter >= length:
                            cond=False
                            break


## function that take file including objects and add them to warehouse with ther quantity and price and in the end check
# which of those objects were had the best selling(according to the requirement of the quiestion) by checking its price
# and the quantity of it that been sold (shipped) from our warehouse ##
def find_best_selling_product(file_name):
    my_input = open(file_name, 'r')
    matamikya = []
    new_counter = 0
    while True:
        line = my_input.readline().split()
        if not line:
            break
        new_counter+=1
        if line[0] == "add":
            add_product(line, matamikya)
        if line[0] == "change":
            change_amount(line, matamikya)
        if line[0] == "ship":
            ship_order(line, matamikya)



    if new_counter == 0:
        my_tuple = ('', 0)
        my_input.close()
        return my_tuple


    if len(matamikya) == 0:
        my_tuple = ('', 0)
        my_input.close()
        return my_tuple
    best_selling_list = []
    j = matamikya[0]
    for i in matamikya:
        if i[3] > j[3]:
            j = i

    for w in matamikya:
        if w[3] == j[3]:
            best_selling_list.append(w)
    if len(best_selling_list) == 1:
        i = best_selling_list[0]
        my_tuple = (i[0], i[3])
        my_input.close()
        return my_tuple

    our_new_list = []
    for i in best_selling_list:
        our_new_list.append(i[0])
    our_find = in_alphabitical_order(our_new_list)

    for k in best_selling_list:
        if k[0] == our_find:
            my_tuple = (k[0], k[3])
            my_input.close()
            return my_tuple


## function that take file including objects and a number k and add them to warehouse with ther quantity and price and in the end return
# which of those objects were had the most selling(according to the requirement of the quiestion) by checking its price
# and the quantity of it that been sold (shipped) from our warehouse and return them by there price then by there alphabitical order
def find_k_most_expensive_products(file_name, k):
    we_list = []
    my_input = open(file_name, 'r')
    matamikya = []
    new_counter = 0
    if k <= 0:
        my_input.close()
        return we_list
    while True:
        line = my_input.readline().split()
        if not line:
            break
        new_counter+=1
        if line[0] == "add":
            add_product(line, matamikya)


    if new_counter == 0:
        my_input.close()
        return we_list

    while True:
        j = matamikya[0]
        for i in matamikya:
            if float(i[1]) > float(j[1]):
                   j = i
            if j[0] > i[0] and float(i[1]) == float(j[1]) :
                j = i
        if len(we_list) == 0:
            we_list.append(j)
        else:
           helper = we_list[len(we_list) - 1]
           if j[1] == helper[1]:
               if j[0] < helper[0]:
                we_list.insert(len(we_list) - 2, j)
               else:
                   we_list.append(j)
           else:
                we_list.append(j)
        k -= 1
        matamikya.remove(j)
        if k == 0:
            break
        if len(matamikya) == 0:
            break

    our_new_list = []
    for i in we_list:
        our_new_list.append(i[0])

    my_input.close()
    return our_new_list



