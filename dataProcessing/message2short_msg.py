str=input('enter ur msg: ')
l=str.split(' ')
vowels=['a','e','i','o','u']
msg=[]
#print(l)
for i in l:
   # print(len(i))
    if(len(i)>3):
        #print(len(i))
        for j in range(0,len(i)):
            if(j==0 or j==(len(i)-1)or i[j] not in vowels or (j!=(len(i)-1) and i[j+1]==',')):
                msg.append(i[j]);
        msg.append(" ")
    else:
        msg.append(" "+i+" ");
        
msg="".join(msg);
print('\n\n\n\n')
print(msg)
