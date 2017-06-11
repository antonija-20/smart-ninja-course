todos = {}

var1 = "da"
var2 = "ne"

while True:
    key = raw_input("unesi jedan broj: ")
    #todos[key] = True
    rijesen = raw_input("task rijesen da / ne: ")
    nerijeseno = False

    todos[key] = rijesen.lower() == var1

    jos = raw_input("zelite li jos da / ne: ")

    if jos.lower() != var1:
        break

resultFile = open("result.txt", "w+")

print "rijeseno\n"
resultFile.write("Rijeseni zadaci:\n")

for task in todos:
    if todos[task]:
        print task
        resultFile.write(task + "\n")

print "nije rijeseno\n"
resultFile.write("Nerijeseni zadaci:\n")

for task in todos:
    if not todos[task]:
        print task
        resultFile.write(task + "\n")

resultFile.close()