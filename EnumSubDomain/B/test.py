f = open('./test.txt','w')
for i in range(1,5):
    for j in range(1,255):
        f.write('147.8.'+str(i)+'.'+str(j)+'\n')

f.close()

    
