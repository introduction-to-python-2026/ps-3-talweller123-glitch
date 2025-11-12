def move(my_list, direction):
    index = my_list.index(1)
    if direction == 'right':
        if index < len (my_list) -1:
            my_list[index] = 0
            my_list[index + 1] = 1
    elif direction == 'left':
        if index > 0:
            my_list[index] = 0
            my_list[index - 1] = 1
    return my_list
