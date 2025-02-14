import json

with open('C:\\Users\\User\\Desktop\\materials\\PP\\PP2\\labs\\lab4\\json\\data.json', 'r') as f:
    data = json.load(f)

print("Interface Status")
print(80 * "=")
print("DN" + 40 * ' ', "Description", "Speed ", "  MTU", sep = "\t")
print(43 * '-', 13 * '-', 7 * '-', 7 * '-', sep = '\t')
for item in data["imdata"]:
    print(item["l1PhysIf"]["attributes"]["dn"], end = "\t")
    if item["l1PhysIf"]["attributes"]["descr"] == "":
        print(" " * len("Description"), end = "\t")
    print(item["l1PhysIf"]["attributes"]["speed"], item["l1PhysIf"]["attributes"]["mtu"], sep = "   ")