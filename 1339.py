N = int(input())  
arr = []


for i in range(N):
    arr.append(input())


arr.sort(key=len, reverse=True)


listarr = []
for i in arr:
    listarr.append(list(i))


char_weight = {}


for word in listarr:
    length = len(word)
    for i in range(length):
        char = word[i]
        if char not in char_weight:
            char_weight[char] = 0
        
        char_weight[char] += 10 ** (length - i - 1)



sorted_chars = sorted(char_weight.items(), key=lambda x: x[1], reverse=True)

char_to_num = {}
num_to_assign = 9


for char, _ in sorted_chars:
    char_to_num[char] = num_to_assign
    num_to_assign -= 1

sum_total = 0
for word in arr:
    num_str = ''.join(str(char_to_num[char]) for char in word)
    sum_total += int(num_str)

print(sum_total)


"""
N=int(input())
arr=[]
for i in range(N):
    arr.append(input())

arr.sort(key=len, reverse=True)

listarr=[]
for i in arr:
    listarr.append(list(i))

abc=[9,8,7,6,5,4,3,2,1,0]
number=[0]*10

 
lenlen=0
ori=0
for i in range(N):
    lenlen=len(listarr[i])
    ori=len(listarr[i])
    for j in range(lenlen):
        if(lenlen==0):
            break
        
        if(listarr[i][j] in number):
            lenlen-=1
            continue
        if(lenlen!=0 and number[j]==0 ):
            number[j]=listarr[i][j]
            lenlen-=1
        elif(lenlen!=0 and number[j]!=0):
            number.insert(ori+j,listarr[i][j])
            lenlen-=1
      

for i in range(N):
    for j in range(len(listarr[i])):
        for k in range(len(number)):
            if(listarr[i][j]== number[k]):
                listarr[i][j]=9-k
                break

sum=0
for i in range(N):
    sum+=int(''.join(map(str,listarr[i])))
  
print(int(sum))
"""