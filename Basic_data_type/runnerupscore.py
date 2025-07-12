n = int(input())
arr = map(int, input().split())
score = list(arr)
    
revscore = list(set(score))
revscore.sort(reverse=True)
    
print(revscore[1])