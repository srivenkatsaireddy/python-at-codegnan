# add 1 to N numbers in output.txt file
file = None
try:
    file = open("output.txt","w")
    n = 10
    for i in range(1,n+1):
        file.write(str(i) + \n)
except:
    print("something wrong")
finally:
    if file is not None:
        file.close()
