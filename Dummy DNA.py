#Note,this is just a dummy
# As a Basic medical science student in tech world. I just felt I should construct a DNA strand using a letter you input...

c=input('Type a single letter for constructing a DNA? \n...')
if len(c)>1:
   c=c[0]
if len(c)<1:
   c="#"
Turns=4
s=" "
def bids(a,b,c="",d=""):
    return(a+b+c+d)

def strand():
    print(bids(s*19,c))
    print(bids(s*17,c*4))
    print(bids(s*16,c*6))
    print(bids(s*14,c*2,s*6,c*2))
    print(bids(s*12,c*14))
    print(bids(s*11,c*2,s*12,c*2))
    print(bids(s*11,c*16))
    print(bids(s*12,c*2,s*10,c*2))
    print(bids(s*14,c*10))
    print(bids(s*16,c*2,s*2,c*2))
    print(bids(s*17,c*4))
    print(bids(s*18,c*2))

for i in range(Turns):    
     strand()
print(" ")
print("Alaran, B.sc Anatomy, Osun state university")  



