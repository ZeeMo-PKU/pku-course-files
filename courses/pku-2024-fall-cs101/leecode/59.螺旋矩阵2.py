class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out=[]
        for i in range(0,n):
            out.append([0]*n)
        gao=n
        kuan=n
        shuru=1
        shang,xia,zuo,you=0,n-1,0,n-1
        while shuru<=n**2:
            for i1 in range(zuo,you+1):
                out[shang][i1]=shuru
                shuru+=1
            shang+=1
            for i2 in range(shang,xia+1):
                out[i2][you]=shuru
                shuru+=1
            you-=1
            for i3 in range(you,zuo-1,-1):
                out[xia][i3]=shuru
                shuru+=1
            xia-=1
            for i4 in range(xia,shang-1,-1):
                out[i4][zuo]=shuru
                shuru+=1
            zuo+=1
        return out
#0ms
