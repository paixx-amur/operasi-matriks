

def bisa_tambah_kurang(A, B):
    return len(A) == len(B) and len(A[0]) == len(B[0])


def bisa_kali(A, B):
    return len(A[0]) == len(B)


def tambah(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] + B[i][j])
        hasil.append(baris)
    return hasil


def kurang(A, B):
    hasil = []
    for i in range(len(A)):
        baris = []
        for j in range(len(A[0])):
            baris.append(A[i][j] - B[i][j])
        hasil.append(baris)
    return hasil


def kali(A, B):
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


def transpose(M):
    hasil = []
    for j in range(len(M[0])):
        baris = []
        for i in range(len(M)):
            baris.append(M[i][j])
        hasil.append(baris)
    return hasil
