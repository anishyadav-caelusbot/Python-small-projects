word="Yourname"
word=word.upper()
#''.join(' ' for y in range(len(word)-1,x,1))+
#''.join(word[z] for z in (x,0,-1))+
#word[:len(word)-x]
for x in range(len(word)-1,-1,-1):
    final=''.join(' ' for y in range(0,x,1))+''.join(word[z] for z in range(len(word)-x-1,0,-1))+word[:len(word)-x]
    print final
