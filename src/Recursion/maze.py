#This prgram is find the path from (0,0) postion to (r,c) , a example for maze.
def maze(A,pos,r,c):
    global parsed
    if pos==(r-1,c-1):
        return [pos]
    x, y = pos
    if x<0 or y<0 or x>=r or y>=c:
        return
    parsed[x][y]=1
    if x-1 >=0 and y<c and A[x-1][y]==1 and parsed[x-1][y]==0:
        a=maze(A,(x-1,y),r,c)
        if(a!=None):
            return [(x,y)]+a
    if x+1 <r and y<c and A[x+1][y]==1 and parsed[x+1][y]==0:
        b=maze(A,(x+1,y),r,c)
        if(b!=None):
            return  [(x,y)]+b
    if x <r and y-1<c and A[x][y-1]==1 and parsed[x][y-1]==0:
        e=maze(A,(x,y-1),r,c)
        if(e!=None):
            return  [(x,y)]+e
    if x <r and y+1<c and A[x][y+1]==1 and parsed[x][y+1]==0:
        f=maze(A,(x,y+1),r,c)
        if(f!=None):
            return  [(x,y)]+f
    parsed[x][y] == 0

arr = [[1,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,1,1]]
parsed= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
rows=5
columns=4
pos=(0,0)
print(maze(arr,pos,rows,columns))