
""" Atividade 1 
Implement a function that has as input is two sorted lists and has
as output, a sorted list with all items from input list. 
This function is part of merge sort. """


def merge( list_1, list_2):
    sorted_ok = False
    merge_result = []
    i = 0
    j = 0
    while not sorted_ok:
        
        print(merge_result)

        if i < len(list_1):
            x = list_1[i]
        else:
            while j < len(list_2):
                merge_result.append(list_2[j])
                j = j + 1
            sorted_ok = True
            

        if j < len(list_2):
            y = list_2[j]
        else:
            while i < len(list_1):
                merge_result.append(list_1[i])
                i = i + 1
            sorted_ok = True

        if not sorted_ok:
            if x > y:
                merge_result.append(y)
                j = j + 1
            else:
                merge_result.append(x)
                i = i + 1


    return merge_result
        

list_a = [0,3,7,9,40]
list_b = [1,2,12]
print(list_a)
print(list_b)
print(merge(list_a, list_b))
