n = []
try:
    n[1]
except Exception as e:
    print("%s: %s" % (type(e), e))

list = [1,1,1,0,0,1]
#with open()
for i,item in enumerate(list):
    try:
        print(1/list[i])
    except:
        list = [1,1,1,2,1,1]
        print(1/list[i])

