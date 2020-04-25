# Enter your code here. Read input from STDIN. Print output to STDOUT

def pattern(x,y):
    
    str_temp = '.|.'
    str_to_print = 'WELCOME'
    for i in range(1,x+1):
        
            
            val_hyphen = int((y - 3*(2*i-1))/2)
            if val_hyphen > 0:
                val_hyphen = int((y - 3*(2*i-1))/2) #val kami kami karaychiye
                str_mid = 2*i-1 #hi vadvaychiye
            
                for i in range(val_hyphen,0,-1):
                    print("-",end = '')
                for i in range(1,str_mid+1):
                    print(str_temp,end = '')
                for i in range(val_hyphen,0,-1):
                    print("-",end = '')    
            elif val_hyphen == 0:
                val_mid = int((y - len(str_to_print))/2)
                for i in range(1,val_mid+1):
                    print("-",end = '')
                print(str_to_print,end = '')
                for i in range(1,val_mid+1):
                    print("-",end = '')

            else:
                str_mid = int((2*val_hyphen + y)/3) #val kami kami karaychiye
                val_hyphen = abs(val_hyphen) #hi vadvaychiye
                #print("val_hyphen_2 "+str(val_hyphen_2))
                #print("str_mid "+str(str_mid))
                for i in range(1,val_hyphen+1):
                    print("-",end = '')
                for i in range(1,str_mid+1):
                    print(str_temp,end = '')
                for i in range(1,val_hyphen+1):
                    print("-",end = '')
                t = 2    
                
            
            print("")
                        
            
           

if __name__ == '__main__':
    x, y = input().split()
    pattern(int(x),int(y))
    #Please give inputs or x in range 5 to 101 and y = 3x!!!
