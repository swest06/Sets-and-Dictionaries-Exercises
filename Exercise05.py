# Needs Refactoring 

n = int(input())
set1 = set(range(1, n + 1))
set2 = set()

finished = False
while not finished:
    print("loop")
    val = input().split()
    if val == ['HELP']:
        finished = True
    else:
        #print(val)
        response = input()
        if response[0] == "Y":
            for i in set1:
                if i not in val:
                    try:
                        set2.add(int(i))
                    except:
                        pass
            for i in set2:
                set1.remove(int(i))
        if response[0] == "N":
            for i in val: 
                print(i)
                #if i not in set:
                set1.remove(int(i))
                
    
#print(set)
