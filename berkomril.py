objek = 2
arr = [[1 for h in range(25)] for i in range(objek)]
arrS = []
def cek(n, g):
    while len(arrS) > 0:
        arrS.pop()
    avaH = 0
    i = 9
    while i + n - 1 <= 21:          
        streak = 0                 
        for a in range(i, i + n):  
            if arr[g][a] != 0:
                streak += 1
        if streak == n:            
            avaH += 1
            arrS.append(i)
        i += 1
    return avaH

def clean(g, choice, n):           
    for i in range(arrS[choice], arrS[choice] + n):
        arr[g][i] = 0


while True:
    apaajh = ["", "Sekolah", "Gudang"]
    for i in range(1, len(apaajh)):
        print("[" + str(i) + "] " + apaajh[i])
    g = int(input("opsi?  ")) - 1  
    n = int(input("Brp jam? "))
    cek(n, g)
    for i in range(len(arrS)):
        print("[" + str(i + 1) + "] " + str(arrS[i]) + ":00 - " + str(arrS[i] + n) + ":00")
    choice = int(input("mskan 1 - " + str(len(arrS))))
    clean(g, choice - 1, n)        
    ans = input("Mw booking lg?(ya/tidak) ")
    if ans == "tidak":
        break