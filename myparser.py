def parser_check(input_string):
    illegal_char = False
    state = 1

    for char in input_string:
        if char == 'a':
            if state == 1:
                state = 2
            elif state == 3:
                state = 4
            elif state == 5:
                state = 3
            else:
                illegal_char = True
                break
        elif char == 'b':
            if state == 1:
                state = 3
            elif state == 2:
                state = 4
            elif state == 3:
                state = 5
            elif state == 4:
                state = 3
            else:
                illegal_char = True
                break

    if not illegal_char and state == 3:
        return "Accepted"
    else:
        return "Not Accepted"
