'''
Usefull Functions:
    isalnum() → Check alphanumeric
    isalpha() → Check alphabetic
    isdigit() → Check digits
    islower(), isupper() → Check case
    isspace() → Check for whitespace
    lower(), upper() → Convert case
    strip(), lstrip(), rstrip() → Remove spaces
    startswith(), endswith() → Check prefixes/suffixes
    replace(old, new) → Replace substring
    split(delimiter) → Split string
    join(iterable) → Join elements into string

    
List:
    my_list = [1, 2, 3, "hello"]
    my_list.append(5)
    my_list.insert(1, "new")
    my_list.remove("hello")
    item = my_list.pop()  # removes last element
    my_list.sort()
    my_list.reverse()

Tuples:
    tuple = (1,4,56)
    tuple.count(2)
    tuple.index(3)

Sets:
    my_set = {2,5,6,8,1}
    my_set.add(4)
    my_set.remove(2)
    my_set.union({5, 6})
    ->
    intersection(), difference(), symmetric_difference()

Dictionaries:
    my_dic = { "name" : "RJ", "age" : 22}
    print(mydict["name"])
    mydict["age"] = 21
    mydict.update({"city": "Delhi"})
    ->
    keys(), values(), items(), get(), pop(key), clear()


'''
str = "hello World"

my_set = {2,5,6,8,1}

squares = [x**2 for x in range(10)]

my_set = {2,5,6,8,1}
my_set2 = {"the", "bill","spent", 2, 1}

my_dic = { "name" : "RJ", "age" : 22, "place": "hydrabad"}
# print(my_dic.items())
# print(my_dic.pop("place"))
# print(my_dic.items())

