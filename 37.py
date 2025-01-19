#wap to Prompt the user for two 2D matrices (lists of lists) of the same dimensions. Perform matrix addition and print the result.

m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,2,3],[4,5,6],[7,8,9]]
m3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        m3[i][j]=m1[i][j]+m2[i][j]
print(m3)
