# 2188

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 왼쪽 정점수, 오른쪽 정점 수
n, m = map(int, input().split())

# 왼쪽 정점에서 연결 가능한 오른쪽 정점 번호들
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp[1:])

# 선택된 정점 번호
selected = [-1] * (m + 1)


def bimatch(N):                                           
    if visited[N]:                                        
        return False                                      
    visited[N] = True                                     
                                                          
    for num in graph[N]:                                   
        if selected[num] == -1 or bimatch(selected[num]):    
            selected[num] = N
            print(N, num)
            return True  
    return False               

for i in range(n):            
    visited = [False] * (n)      
    bimatch(i)

result = 0               
for i in range(1, m+1):  
    if selected[i] >= 0:         
        result += 1
print(result)