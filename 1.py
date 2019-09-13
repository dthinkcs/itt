
n = (eval(input().strip()))
print(n)


def transpose_matrix(matrix):
    newMatrix = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            newMatrix[j][i] = matrix[i][j]
    # print(newMatrix)
    return newMatrix

matrix =  [ [  i**3 - j for j in range(3)] for i in range(3)]
print("Matrix:", matrix)
transposedMatrix = transpose_matrix(matrix)
print("Transpose: ", transposedMatrix)

def mulMatrices(A, B):
    # pxq rxs = pxs
    p, q, r, s = len(A), len(A[0]), len(B), len(B[0])
    assert q == r
    C = [[0 for j in range(p)] for i in range(s)]
    for i in range(p):
        for j in range(s):
            for k in range(q):
                C[i][j] += A[i][k] * B[k][j]
    return C

def I(n):
    return [ [1 if j == i else 0 for j in range(n)] for i in range(n)]
matrixA = matrix
matrixB = transposedMatrix
matrixC = mulMatrices(matrixA, matrixB)
print("Multiplication Result = ", matrixC)

def addMatrices(A, B):
    assert len(A) == len(B) and len(A[0]) == len(B[0])
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print("Addition Result = ", addMatrices(matrixA, matrixB))


def sumofFirstNNatrualNumbers(n):
    return (n * (n + 1)) // 2
print(sumofFirstNNatrualNumbers(n))


def fib(n):
    curr, next = 0, 1
    for i in range(n):
        curr, next = next, curr + next
    return curr
print(fib(n))

def binOctHex(n):
    return "Binary:{} Octal:{} Hexadecimal:{}".format(bin(n), oct(n), hex(n))
print(binOctHex(n))


def setOperations():
    setA = {i for i in range(5)}
    setB = {i + 2 for i in range(5)}
setOperations()

def isPalin(w):
    return w[::-1] == w
print("isPalin('dad') =", isPalin("dad"))
print("isPalin('diddy') =", isPalin("diddy"))

def caesarCipher(plaintext, key):

    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.islower():
                ciphertext += chr(( ord(c) - ord('a') + key ) % 26 + ord('a'))
            else:
                ciphertext += chr(( ord(c) - ord('A') + key ) % 26 + ord('A'))
        else:
            ciphertext += c
    return ciphertext
plaintext = "Attack On Pearl Harbour: December 7, 1941"
print("Plaintext: {}\nCiphertext: {}".format(plaintext, caesarCipher(plaintext, n)))

#----------DONE WRITE BEFORE THIS

def isPrime(n):
    n = abs(n)
    if n in [0, 1]:
        return False
    possibleDivisor = 2
    while possibleDivisor*possibleDivisor <= n:
        if n % possibleDivisor == 0:
            return False
        possibleDivisor += 1
    return True


def generateAllPrimes(m, n):
    listPrimes = []
    for i in range(m, n + 1):
        if isPrime(i):
            listPrimes.append(i)
    return listPrimes

listPrimes = generateAllPrimes(n, n** 2)
print("Primes from {} to {} are: ".format(n, n**2), listPrimes)

def myInPlaceSort(lt):
    for i in range(len(lt) - 1):
        minIdx = i
        for j in range(i + 1, len(lt)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        if minIdx != i:
            arr[i], arr[minIdx] = arr[minIdx], arr[i]

lt = reversed(listPrimes)
print("List:", lt)
myInPlaceSort(lt)
print("Sorted List:", lt)
