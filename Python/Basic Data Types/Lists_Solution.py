# Problem: Lists
# Platform: HackerRank
# Description: Perform various operations on a list based on user input commands.


if __name__== "__main__":
    N=int(input())
    lis=[]
    for i in range(N):
        op,*line =input().split()
        op=op.lower().strip()
        if all(int for i in line):
            nums=list(map(int,line)) if len(line) >=0 else []
            if op=='insert' and len(nums)== 2:
                lis.insert(nums[0],nums[1])
            elif op=='print' and len(nums)== 0:
                print(lis)
            elif op=='remove' and len(nums)== 1:
                lis.remove(nums[0])
            elif op=='append' and len(nums)== 1:
                lis.append(nums[0])
            elif op=='sort' and len(nums)== 0:
                lis.sort()
            elif op=='pop' and len(nums)== 0:
                lis.pop()
            elif op=='reverse' and len(nums)== 0:
                lis.reverse()
