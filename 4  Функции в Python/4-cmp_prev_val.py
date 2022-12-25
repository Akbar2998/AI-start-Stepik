counter = 0
cd = []
def cmp_prev(val):
    cd.append(val)
    global counter
    counter += 1
    if counter > 3 or counter == 3:
        return val > cd[-2]+cd[-3]
    elif (counter == 1 or counter == 2) and val > 0:
        return True
    else:
        return False
