# Program Komnum Newton-Gregory Backwards, versi Differensial.
Tugas final project komnum 2025


---


Cara kerja Kode: 

## **1. Pembuatan tabel Delta x terbalik (dari x terbesar ke terkecil)**

### A. Program akan menyortir dari nilai x paling besar ke paling kecil karena kita menggunakan Newton-Gregory Backward-Differensial.
```
def build_backward_deltaerence_table(nilai_X, nilai_Y):
    combined = sorted(zip(nilai_X, nilai_Y), reverse=True)
    x_st, y_st = zip(*combined)
```
Nanti ```x_st``` dan ```y_st``` digunakan untuk menyimpan data.

### B. Untuk Kolom pertama program akan menetapkan nilai y dari X0 pertama, lalu program akan mengulangi kalkulasi Delta terbalik (Δy₀ = y₀ - y₁ ; Δ²y₀ = Δy₀ - Δy₁ ; ...). Setiap level nantinya akan ditambahkan ke ```table```. 
```
table = [list(y_st)]
    while len(table[-1]) > 1:
        prev = table[-1]
        new_row = [round(prev[i] - prev[i + 1], 2) for i in range(len(prev) - 1)]
        table.append(new_row)
```

### C. Mengembalikan x yang sudah disortir dan tabel Delta sepenuhnya.
```
return x_st, table
```

---

## **2. Pengambilan nilai Delta yang diperlukan di X0**

### A. Validasi niali X0.
```
def extract_deltas_at_x0(x_st, table, x0):
    if x0 not in x_st:
        raise ValueError("error")
```

### B. Mencari Baris dimana ada X0.
```
    idx = x_st.index(x0)
    extracted = []

    for level in range(len(table)):
        if idx < len(table[level]):
            extracted.append(table[level][idx])
```
Untuk setiap Tingkatan berbeda, akan diambil nilai deltanya di index X0. Program juga akan Mengabaikan Data-Data yang tidak diperlukan.

### C. Mengembalikan nilai Delta yang tersedia.
```
    return extracted
```

---

## **3. Function utama untuk kalkulasi Derivasi**

### A. Kalkulasi ```h``` dan kalkulasi ```s = (x - x₀)/h``` sebagai jarak X0.
```
def derivative_ng_backward_verbose(nilai_X, nilai_Y, x0, x):
    h = round(nilai_X[1] - nilai_X[0], 2)
    s = round((x - x0) / h, 2)
```

### B. Membuat tabel terbalik dan ambil nilai Delta di x0. Membatasi untuk 5 nilai Delta saja.
```
    x_st, table = build_backward_deltaerence_table(nilai_X, nilai_Y)
    delta = extract_deltas_at_x0(x_st, table, x0)

    while len(delta) < 5:
        delta.append(0)
```

### C. Kalkulasi Derivasi Pembilang yang nanti akan digunakan di rumus.
Untuk Koefisien 2 kita perlu:
```
    koef2 = round((2 * s + 1) / 2, 2)
    part2 = round(koef2 * delta[2], 2)
    pembilang2 = round(pembilang1 + part2, 2)
```

Untuk Koefisien 3 kita perlu:
```
    s2 = round(s ** 2, 2)
    koef3 = round((3 * s2 + 6 * s + 2) / 6, 2)
    pembilang3 = round(koef3 * delta[3], 2)
```

Untuk Koefisien 4 kita perlu:
```
    s3 = round(s ** 3, 2)
    koef4 = round((4 * s3 + 18 * s2 + 22 * s + 6) / 24, 2)
    pembilang4 = round(koef4 * delta[4], 2)
```

Kalkulasi Akhir:
```
    derivative = (pembilang2 + pembilang3 + pembilang4) / h
```
hanya ada 3 koefisien karena koefisien pertama sudah ditambah ke koefisien kedua.

---

## **4. Input dan Eksekusi Kode**

Data :
```
nilai_X = [2, 4, 6, 8, 10, 12, 14, 16, 18]
nilai_Y = [-940, -6008, -11652, 1040, 74020, 279960, 729932, 1581088, 3044340]

x0 = 10
x = 11
```
Memanggil Fungsi dan Mencetak hasil akhir.
```
result = derivative_ng_backward_verbose(nilai_X, nilai_Y, x0, x)
print(f"\nHasil akhir turunan f'({x}) ≈ {result}")
```
