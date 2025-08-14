    #  Size: 7 x 21 
    #---------.|.---------
    #------.|..|..|.------
    #---.|..|..|..|..|.---
    #-------WELCOME-------
    #---.|..|..|..|..|.---
    #------.|..|..|.------
    #---------.|.---------
    # --------------------
    # بتزيد كل مرة بمقدار 2 
    # لحد م توصل للنص بعدين تبدأ تقل بمقدار 2 


if __name__== '__main__':
    n= list(map(int,input().split()))
    N,M=n[0],n[1]
    
    if N % 2==1 and M == 3*N and 5 < N < 101 and 15 < M < 303 :
        
        odd=[i for i in range(N) if i % 2 ==1]
        #for the upper half
        for i in odd:
            print((f".|."*i).center(M,"-"))
        #for the center
        print("WELCOME".center(M,"-"))
        #for the lower half
        for i in sorted(odd,reverse=True):
            print((f".|."*i).center(M,"-"))


#-------------------------ANOTHER SOL ----------------
# if __name__== '__main__':
#     n= list(map(int,input().split()))
#     N,M=n[0],n[1]
    
#     if N % 2==1 and M == 3*N and 5 < N < 101 and 15 < M < 303 :
        
#         for i in range(1,N,2):
#             print((f".|."*i).center(M,"-"))
        
#         print("WELCOME".center(M,"-"))
    
#         for i in range(N-2,0,-2):
#             print((f".|."*i).center(M,"-"))

        
    

