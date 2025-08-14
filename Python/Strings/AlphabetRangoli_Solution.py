




#--------------------------second version-------------------
import string

def print_rangoli(size):
    
    # list from all alphabetic characters
    letters = list(string.ascii_lowercase) 

    if 0<size<27:
        #the maximum number of characters in the middle included the hyphens  
        Max_Width=4*size-3

        #list of specific letters
        rang=[letters[i] for i in range(size)] # if Letters_num=3  ==> [a,b,c]

        #the upper half
        for i in range(size-1,-1,-1) :
            col=rang[size-1:i:-1]+rang[i-size:i-size-1:-1] + rang[i+1:] 
            row="-".join(col).center(Max_Width,"-")
            print(row)

        #the lower half
        for i in range(size-1) :
            col=rang[size-1:(i+1):-1]+rang[(i+1)-size:(i+1)-size-1:-1] + rang[i+2:]
            row="-".join(col).center(Max_Width,"-")
            print(row)
            
#number of letters used to make the shape 
Letters_num=int(input())
print_rangoli(Letters_num)
    

#-----------------------------------first version -------------------------------------------------   
# import string
# # list from all alphabetic characters
# letters = list(string.ascii_lowercase) 
# Letters_num=int(input())
# Max_Length=(Letters_num*2)-1
# max_letters=Max_Length
# #عرض الشكل كله 
# Max_Width=((Letters_num*2)-1)+((Letters_num*2)-2)

# # print(Max_Width)
# # print(Max_Length)

# rang=[]
# in_rang=[]
# #list of specific letters
# for i in range(Letters_num) :
#     rang.append(letters[i])

# # print(rang[-1:-2:-1])
# # print(rang[-2:-3:-1])
# # print(rang[-3:-4:-1])


# #  ('_') الجزء ده قعدت فيه حوالي 5 ساعات عشان اعرف اعمله 

# #the upper half
# for i in range(Letters_num-1,-1,-1) :
#     lis=rang[Letters_num-1:i:-1]+rang[i-Letters_num:i-Letters_num-1:-1] + rang[i+1:]
#     row="-".join(lis).center(Max_Width,"-")
#     print(row)

# #نفس اللي فات ولكن هنعكس البداية بتاعت اللوب وكمان هنهمل بس اول حرف في اللليست
# for i in range(Letters_num-1) :
#     lis=rang[Letters_num-1:(i+1):-1]+rang[(i+1)-Letters_num:(i+1)-Letters_num-1:-1] + rang[i+2:]
#     row="-".join(lis).center(Max_Width,"-")
#     print(row)

    


# # for i in range(Max_Length):
# #     for j in range(max_letters):
        
        
        
            
    
    
    


# # for i in range(Max_Width_length):
    
    
    
    
    

# #3>>>5
# #5>>>9
# #10>>19