import random

def get_num():
    l = random.randint(1, 12)
    results = {
        "a" : random.randint(1, 12),
        "b" : random.randint(1, 12),
        "c" : random.randint(1, 12),
        "d" : random.randint(1, 12),
        "y" : random.randint(1, 10),
        "z" : random.randint(1, 10),
        "x" : random.randint(1, 10),
        "l" : l if not l / 2 == 0 else l+1,
        "q" : float("{:.1f}".format(random.random()))
    }
    return results