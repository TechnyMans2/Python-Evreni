#@technymans / matrisli sayıları toplayalım.

x = [[1,3,5],[4,5,7],[8,9,2]]

y = [[7,1,4],[6,2,1],[3,5,7]]

sonuc = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        sonuc [i][j] = x[i][j]+y[i][j]
           
print(sonuc)
         