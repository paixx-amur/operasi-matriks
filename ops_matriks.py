# ==============================
# UTILITAS DASAR
# ==============================

def copy_matrix(A):
    return [row[:] for row in A]

def shape(A):
    return len(A), len(A[0])

def bisa_tambah_kurang(A, B):
    return shape(A) == shape(B)

def bisa_kali(A, B):
    return len(A[0]) == len(B)

# ==============================
# OPERASI DASAR
# ==============================

def tambah(A, B):
    if not bisa_tambah_kurang(A, B):
        raise ValueError("Ordo matriks tidak sama")

    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil

def kurang(A, B):
    if not bisa_tambah_kurang(A, B):
        raise ValueError("Ordo matriks tidak sama")

    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil

def kali(A, B):
    if not bisa_kali(A, B):
        raise ValueError("Jumlah kolom A harus sama dengan jumlah baris B")

    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            baris.append(total)
        hasil.append(baris)
    return hasil

def transpose(A):
    hasil = []
    for j in range(len(A[0])):
        baris = []
        for i in range(len(A)):
            baris.append(A[i][j])
        hasil.append(baris)
    return hasil

# ==============================
# DETERMINAN (NxN)
# ==============================

def determinan(A):
    if len(A) != len(A[0]):
        raise ValueError("Matriks harus persegi")

    n = len(A)
    M = copy_matrix(A)
    det = 1

    for i in range(n):
        if M[i][i] == 0:
            for k in range(i+1, n):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    det *= -1
                    break
            else:
                return 0

        pivot = M[i][i]
        det *= pivot

        for j in range(i, n):
            M[i][j] /= pivot

        for k in range(i+1, n):
            faktor = M[k][i]
            for j in range(i, n):
                M[k][j] -= faktor * M[i][j]

    return round(det, 5)

# ==============================
# TRANSFORMASI BARIS ELEMENTER
# ==============================

def swap_rows(A, i, j):
    A = copy_matrix(A)
    A[i], A[j] = A[j], A[i]
    return A

def multiply_row(A, i, k):
    A = copy_matrix(A)
    A[i] = [k * x for x in A[i]]
    return A

def add_multiple_row(A, source, target, k):
    A = copy_matrix(A)
    A[target] = [
        A[target][j] + k * A[source][j]
        for j in range(len(A[0]))
    ]
    return A

# ==============================
# GAUSS ELIMINATION (RREF)
# ==============================

def gauss_elimination(A):
    A = copy_matrix(A)
    n = len(A)
    m = len(A[0])

    row = 0
    for col in range(m):
        if row >= n:
            break

        pivot = row
        for i in range(row, n):
            if A[i][col] != 0:
                pivot = i
                break
        else:
            continue

        A[row], A[pivot] = A[pivot], A[row]

        pivot_val = A[row][col]
        for j in range(m):
            A[row][j] /= pivot_val

        for i in range(n):
            if i != row:
                factor = A[i][col]
                for j in range(m):
                    A[i][j] -= factor * A[row][j]

        row += 1

    return A

