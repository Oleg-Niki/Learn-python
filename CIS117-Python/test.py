my_list = [1,2,3,4,1,2,3,4,5,6,8,9,5,4,3]
print(my_list)
my_char = 'Oleg'
#print(set(my_list))

my_list.sort()
print(my_list)

my_list += [my_char]
print(my_list)

days = {"Sunday": 1, "Monday" : 2, "Tuesday" : 4}
print(days)
print(days["Sunday"])
total_days = sum(days.values())
print(total_days)

#recipes = {"Indian" : {"paneer tikka masala" : {serv1 : (banana, apple, paneer)} }}

def frequency(itemList):
    counters = {}
    for item in itemList:
        if item in counters:
            counters[item] += 1
        else:
            counters[item] = 1
        return counters

   
print(frequency(days))