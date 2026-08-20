# import csv
# try:
#     with open("test.csv","w", newline="") as file:
#         writer = csv.writer(file)
#         header = ["Name","contact"]
#         writer.writerow(header)
#         data = [["ram",9059845672],["sam",4837839729]]
#         writer.writerows(data)
#         print("content added")
# except Exception as e:
#     print(f"Something wrong in test.csv: {e}")

#reading csv file conntent
import csv
try:
    with open("test.csv","r") as file:
        reader = csv.reader(file)
        #print(list(reader))
        for row in reader:
            print(row)
        print("content added")
except Exception as e:
    print(f"Something wrong in test.csv: {e}")

# writing content into file
try:
    with open("test.csv","w") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
        print("content added")
except Exception as e:
    print(f"Something wrong in test.csv: {e}")
