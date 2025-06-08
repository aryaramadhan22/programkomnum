import math

def build_backward_deltaerence_table(nilai_X, nilai_Y):
    combined = sorted(zip(nilai_X, nilai_Y), reverse=True)
    x_st, y_st = zip(*combined)

    table = [list(y_st)]
    while len(table[-1]) > 1:
        prev = table[-1]
        new_row = [round(prev[i] - prev[i + 1], 2) for i in range(len(prev) - 1)]
        table.append(new_row)

    return x_st, table

def extract_deltas_at_x0(x_st, table, x0):
    if x0 not in x_st:
        raise ValueError("error")

    idx = x_st.index(x0)
    extracted = []

    for level in range(len(table)):
        if idx < len(table[level]):
            extracted.append(table[level][idx])

    return extracted

def derivative_ng_backward_verbose(nilai_X, nilai_Y, x0, x):
    h = round(nilai_X[1] - nilai_X[0], 2)
    s = round((x - x0) / h, 2)  

    x_st, table = build_backward_deltaerence_table(nilai_X, nilai_Y)
    delta = extract_deltas_at_x0(x_st, table, x0)

    while len(delta) < 5:
        delta.append(0)

    print(f"s = {s}")
    print(f"h = {h}")
    
    pembilang1 = delta[1] 
    print(f"pembilang1 = {pembilang1}")

    koef2 = round((2 * s + 1) / 2, 2)
    part2 = round(koef2 * delta[2], 2)
    pembilang2 = round(pembilang1 + part2, 2)
    print(f"pembilang2 = pembilang1 + ((2*{s} + 1)/2) * delta2 = {pembilang1} + {koef2} * {delta[2]} = {pembilang2}")

    s2 = round(s ** 2, 2)
    koef3 = round((3 * s2 + 6 * s + 2) / 6, 2)
    pembilang3 = round(koef3 * delta[3], 2)
    print(f"pembilang3 = ((3*{s2} + 6*{s} + 2)/6) = {koef3} * delta3 = {pembilang3}")

    s3 = round(s ** 3, 2)
    koef4 = round((4 * s3 + 18 * s2 + 22 * s + 6) / 24, 2)
    pembilang4 = round(koef4 * delta[4], 2)
    print(f"pembilang4 = ((4*{s3} + 18*{s2} + 22*{s} + 6)/24) = {koef4} * delta4 = {pembilang4}")

    derivative = (pembilang2 + pembilang3 + pembilang4) / h
    print(f"\nf'({x}) ≈ (({pembilang2} + {pembilang3} + {pembilang4}) / {h}) = {round(derivative, 2)}")

    return round(derivative, 2)

nilai_X = [2, 4, 6, 8, 10, 12, 14, 16, 18]
nilai_Y = [-940, -6008, -11652, 1040, 74020, 279960, 729932, 1581088, 3044340]

x0 = 10
x = 11

result = derivative_ng_backward_verbose(nilai_X, nilai_Y, x0, x)
print(f"\nHasil akhir turunan f'({x}) ≈ {result}")