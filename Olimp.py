input_data = open('input.txt', 'r') 
data = input_data.read() 
#-------------------------------------------------------------------------
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])

vpr = 0
npr = 0
sr = 0

if a > b and a > c:
    vpr = a
elif b > a and b > c:
    vpr = b
elif c > a and c > b:
    vpr = c   
elif a == b and a > c: 
    vpr = a or b     
elif a == c and a > b: 
    vpr = a or c 
elif b == c and b > a: 
    vpr = b or c        




if a < b and a < c:
    npr = a
elif b < a and b < c:
    npr = b
elif c < a and c < b:
    npr = c 
elif a == b and a < c: 
    npr = a or b     
elif a == c and a < b: 
    npr = a or c 
elif b == c and b < a: 
    npr = b or c        


if a > b > c:
    sr = b
elif a < b < c:
    sr = b
elif b < a < c:
    sr = a
elif b > a > c:
    sr = a
elif b < c < a:
    sr = c
elif b > c > a:
    sr = c




vpr = int(vpr)
npr = int(npr)  
sr = int(sr)        






st1 = npr + npr + sr + npr + vpr
st5 = a + a + b + a + b + c 
st3 = c + c + b + c + b + a


aut = 0
 
if st1 < st3 and st1 < st5:
    aut = 1
elif st3 < st1 and st3 < st5:
    aut = 3
elif st5 < st1 and st5 < st3:
    aut = 5 
elif st1 == st5 and st1 < st3: 
    aut = 1    
elif st1 == st3 and st1 < st5: 
    aut = 1 
elif st3 == st5 and st3 < st1: 
    aut = 3




#-------------------------------------------------------------------------
output_data = open('output.txt', 'w') 
output_data.write(str(aut))

input_data.close() 
output_data.close()