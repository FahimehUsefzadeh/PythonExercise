import random
true_char=[]
words=['apple' , 'banana' , 'orange' , 'kiwi' , 'strawberry' , 'cucamber' , 'suorcherry']
word=random.choice(words)
score=(len(word))
print('-'*len(word))
while True:
    char=input('enter a character:')
    if char in word:
        true_char.append(char)
    else:
        score-=1
    for i in range (len(word)):
        if word[i] in true_char:
            print(word[i],end='')
        else:
            print('-', end='')
    counter=0
    for w in word:
        if w in true_char:
            counter+=1
    if counter==len(word):
        print('you win')
        break
    if score==0:
        print('you lose')
        break
    

