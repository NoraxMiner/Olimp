input_data = open('input.txt', 'r') 
data = input_data.read() 
#-------------------------------------------------------------------------
data = data.split()
a = int(data[0])
b = int(data[1])
c = int(data[2])

vpr = 0
npr = 0

if a > b and a > c:
    vpr = a
elif b > a and b > c:
    vpr = b
elif c > a and c > b:
    vpr = c   



if a < b and a < c:
    npr = a
elif b < a and b < c:
    npr = b
elif c < a and c < b:
    npr = c 
      

vpr = str(vpr)
npr = str(npr)         
aut = str(vpr + ' '  + npr)


st1 = 0
st2 = 0
st3 = 0




#-------------------------------------------------------------------------
output_data = open('output.txt', 'w') 
output_data.write(aut)

input_data.close() 
output_data.close()