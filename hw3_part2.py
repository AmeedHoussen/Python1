## function to check if the given string is palindromic
# ( if it is has the same letters from left to right and the opposite) ##
def check_if_palindrom(str):
    str_reverse=str[::-1]
    counter=0
    for i in str_reverse:
        if str[counter] != str_reverse[counter]:
            return False
        counter += 1
    return True

## function that take a string and return every possible palindromic part of it in each size and put thim in dictionary ##
def get_palindrom_dict(str):
    our_dict = {}
    if(len(str) == 0):
        return our_dict
    counter=0
    counter2 = 1
    our_list=[]
    new_list=[]
    while counter2 <= len(str):
      for j in str:
       our_list = [str[i:i + counter2] for i in range(0, len(str), 1)]
       w=0
       x=0
       while x < counter2-1:
           del our_list[-1]
           x+=1

       while w < len(our_list):
        cond = check_if_palindrom(our_list[w])
        if cond == False:
            our_list.remove(our_list[w])
            continue
        w += 1
       length = len(our_list)
       if length != 0:
        our_dict[counter2 ] = our_list
       counter2 += 1
    return our_dict

## function to check if the given string has a string takin from its odd places
# and its even places are similar to each other (as mintioned in the requirment ##
def check_match(str):
        if len(str) == 0:
            return True
        str_odd = str[1:len(str):2]
        str_even = str[0:len(str):2]

        if len(str_odd) != len(str_even):
            return False

        this_dict_even = {}

        count = 0
        y = True
        for i in str_even:
            if i in this_dict_even:
                if this_dict_even[i] != str_odd[count]:
                    y = False
                    break
            this_dict_even[i] = str_odd[count]
            count += 1
        return y
