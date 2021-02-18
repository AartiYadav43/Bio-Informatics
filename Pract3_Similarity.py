sequence_one=input("Enter the first sequence:")
sequence_two=input("Enter the second sequence:")
how_many=int(input("how many element for similarity calculation"))
similarities=[]
for i in range(0,how_many):
    a=input("Enter an element:")
    c=int(input("how many elements is it similar to?"))
    similarities.append([])
    similarities[i].append(a)

    for j in range (0,c):
        b=input("what is it similar to?")

        similarities[i].append(b)

def compare(o,t,s):
    print(0)
    print(t)
    print(s)
    #checking if similar
    score=0
    for i in range(len(0)):
        for j in range(len(s)):

            if 0[i] in s[j] and t[i] in s[j] and o[i]!=t[i]:
                score+=1
    #calculating similarity
    similarity=(score*100)/len(0)
    return similarity
print(compare(list(sequence_one),list(sequence_two),similarities),"%")           
