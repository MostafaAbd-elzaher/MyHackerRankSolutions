def print_formatted(n):
    
    if 1<= n <= 99:
        width = len(format(n, 'b'))
        for i in range(1, n + 1):
            deci = str(i)
            octal = format(i, 'o')
            hexa = format(i, 'X')
            binary = format(i, 'b')
            
            print("{:>{w}} {:>{w}} {:>{w}} {:>{w}}".format(
                deci, octal, hexa, binary, w=width
            ))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)




# print(bin(99)[2:])
# print(format(99, "b")) 
  
# for i in range(1,n+1):
#     print(f"{i:<5}{"{:<5}".format(i,"o")}{"{:<5}".format(i,"x")}{"{:<5}".format(i,"b")}")
   
#     print("{:>5}{:>5}{:>5}{:>5}".format(i,oct(i)[2:],hex(i)[2:],bin(i)[2:]))
#print("{:>2}{:>3}{:>3}{:>3}".format(i,oct(i)[2:],hex(i)[2:],bin(i)[2:]))




