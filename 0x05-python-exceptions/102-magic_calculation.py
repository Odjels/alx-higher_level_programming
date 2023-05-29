102-magic_calculation.py

def magic_calculation(a, b):
    res = 0
    for c in range(1, 3):
        try:
            if c > a:
                raise Exception('Too far')
            else:
                res += a ** b / c
        except Exception:
            res = b + a
            break
    return res
