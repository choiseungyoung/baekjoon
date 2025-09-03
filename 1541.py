arr=list(input())
number=[]
character=[]
for i in arr:
    if i.isdigit():
        number.append(i)
    else:
        character.append(i)
