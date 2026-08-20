# opening a file in 'w' mode
# file = open("sample.txt","w")
# file.write("hello world")
# file.close()
# print("content Added")


# opening file in append mode
# file = open("sample.txt","a")
# file.write("sai")
# file.close()
# print("content Added")


# add content at start of file,and open in append mode
# opening file in append mode
# file = open("sample1.txt","r")
# string = """I am a student i am learnig
# python course"""
# file.seek(0)
# file.write(string)
# file.close()
# print("content Added")

# open a file in read mode
try:
    file = open("sample.txt",'r')
    data = file.readlines()
    print(data)
except Exception as e:
    print(f"something wrong,because : {e}")
finally:

    if file:
        file.close()  