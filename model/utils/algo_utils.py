B = 2

def h(t, p):
    if t < 0:
        return 0
    else:
        return p * (t ** B)  # for now, time * probability