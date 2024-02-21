# Inputs
# 1. The pressed keys (original string)
# 2. The displayed keys (broken string)

quiet_key = '-'
silly_key = ''
corresponding_key = ''

pressed_keys = str(input())
displayed_keys = str(input())

last_key_was_quiet = False
shifted = 0

def charat(cstring, index, default=None): 
    char = default

    try:
        char = cstring[index]
    except IndexError:
        char = default

    return char

for x in range(len(pressed_keys)):
    pressed_key = charat(pressed_keys, x, '')
    displayed_key = charat(displayed_keys, x-shifted, '')

    next_pressed_key = charat(pressed_keys, x+1, '')
    next_displayed_key = charat(displayed_keys, x+1, '')

    if pressed_key == quiet_key:
        shifted += 1
        
    if (next_pressed_key == displayed_key) and quiet_key == '-':
        quiet_key = pressed_key
        last_key_was_quiet = True
        shifted += 1
        continue
    elif (pressed_key != displayed_key) and (next_pressed_key == next_displayed_key) and not last_key_was_quiet:
        silly_key = displayed_key
        corresponding_key = pressed_key 
    
    last_key_was_quiet = False

print(f'{corresponding_key} {silly_key}')
print(quiet_key)

        