
todos = []

while True:
    todos.append(raw_input("unesi jedan broj: "))

    jos = raw_input("zelite li jos da / ne: ")

    var1 = "da"
    var2 = "ne"

    if jos.lower() != var1:
        break
i = 1
for task in todos:
    print str(i) + ". task: " + task
    i = i + 1




