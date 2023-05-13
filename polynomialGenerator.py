import math

def get_lagrange(index, data):
    lag_poly = [None for _ in data]
    current = 1
    for i,val in enumerate(data):
        if i == index: continue
        lag_poly[current] = -val[0]
        current += 1
    mult = data[index][0]
    first = 1
    for val in lag_poly:
        if val == None: continue
        first *= (mult+val)
    lag_poly[0] = first
    return lag_poly

def str_lag(lag):
    string = ""
    if lag[0]>=0:
        string += f"(1/{lag[0]})"
    else:
        string += f"(-1/{abs(lag[0])})"
    for i in range(1, len(lag)):
        if lag[i]>=0:
            string += f"(x+{lag[i]})"
        else:
            string += f"(x{lag[i]})"
    return string

def poly_simp(lag_poly):
    out = [1]
    for val in range(1, len(lag_poly)):
        val = lag_poly[val]
        for i in range(len(out)):
            if i == len(out)-1:
                out[i] = val*out[i]
            else:
                out[i] = val*out[i]+out[i+1]
        out.insert(0,1)
    return out

def add_fractions(fractions):
    lcm = fractions[0][1]
    for i in range(1, len(fractions)):
        lcm = math.lcm(lcm, fractions[i][1])
    added = []
    for fract in fractions:
        added.append((int((lcm / fract[1]) * fract[0]), lcm))
    print(added)
    sum = 0
    for fract in added:
        sum += fract[0]
    return (sum,lcm)

def main():
    points = [(0,-1), (1,0), (2, 1), (3, 0)]
    lag_polys = []
    for i in range(len(points)):
        lag_polys.append(get_lagrange(i, points))


    fractions = []
    poly = [0 for _ in range(len(points))]

    for i,pt in enumerate(points):
        for j,val in enumerate(poly_simp(lag_polys[i])):
            poly[j] += (val*pt[1])/lag_polys[i][0]

    for i,place in enumerate(poly):
        if place == 0:
            continue
        power = abs(i-len(poly)+1)
        if power == 0:
            if place>=0:
                print("+" + str(place))
            else:
                print(place)
        elif power == 1:
            if place>=0:
                print(f"+{place}x", end="")
            else:
                print(f"{place}x", end="")
        else:
            if place>=0:
                print(f"+{place}x^{power}", end="")
            else:
                print(f"{place}x^{power}", end="")
main()

