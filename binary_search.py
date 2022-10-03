def binary_search(entered_list, element):
    middle = 0
    start = 0
    end = len(entered_list)
    steps = 0

    while start <= end:
        print("Step " + str(steps) + ": " + str(entered_list[start:end+1]))

        steps = steps + 1
        middle = (start + end) // 2

        if element == entered_list[middle]:
            return middle

        if element < entered_list[middle]:
            end = middle - 1

        if element > entered_list[middle]:
            start = middle + 1

        if element not in entered_list:
            print(str(element) + " is not present in " + str(entered_list))
            break

    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = int(input("Enter the element to be search: "))
binary_search(my_list, target)
