
def quicksort(source_list):
    control_stack = []
    control_stack.append([0, len(source_list) - 1, (len(source_list) - 1) / 2])
    while len(control_stack) > 0:
        point = control_stack.pop()

    source_list.sort()
    return source_list
