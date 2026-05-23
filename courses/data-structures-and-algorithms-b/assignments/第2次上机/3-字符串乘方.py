def main(juzi):
    if juzi=='':
        return 0
    l=len(juzi)
    for l_zichuan in range(1,l+1):
        if l%l_zichuan==0:
            if juzi[0:l_zichuan]*(l//l_zichuan)==juzi:
                return l//l_zichuan
        else:
            continue
while True:
     a=input()
     if a=='.':
         break
     else:
         print(main(a))