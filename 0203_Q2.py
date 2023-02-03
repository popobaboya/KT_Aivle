# Q2 Answer template

def solution(numbers):
    answer = -1
    nlist = []

    for i in range(10):
        nlist.append(i)
        
    for x in numbers:
        if x in nlist:
            nlist.remove(x)
    answer = sum(nlist)
    
    return answer

numbers = [1,2,3,4,6,7,8,0]
answer = solution(numbers)
print(answer)
