import csv

# file = open("test.csv", mode="r", encoding="utf8")
# data = csv.reader(file)

# file.seek(0)
# file.close()
# file.seek(0)
with open("backup.csv", encoding="utf8") as file:
    data = csv.reader(file, delimiter=";")
    headers = next(data)
    print(headers)