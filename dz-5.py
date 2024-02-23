# example_list = [1, 2, 3, 4, 5, 6]
# example_list = [1, 2, 3]
# example_list = [1, 2, 3, 4, 5]
# example_list = [1]
example_list = []

list_length = len(example_list)
list_divider = int((len(example_list) / 2))
new_list = []

if not list_length % 2 == 0:
    list_divider += 1

first_half = example_list[0:list_divider]
second_half = example_list[list_divider:list_length]
new_list.append(first_half)
new_list.append(second_half)

print(new_list)


