def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
number_list = []
n = int(input("Insert # of elements: "))
print("\n")
for i in range(0,n):
    print("Insert element for: ", i, " ")
    item = int(input())
    number_list.append(item)
print("The list is", number_list)
selectionSort(number_list, n)
print('Sorted Array in Ascending Order:')
print(number_list)
