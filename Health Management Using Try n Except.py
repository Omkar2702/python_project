# Health Management System
client_list = {1: "Omkar", 2: "Gurleen", 3: "Simrat"}
Log_list = {1: "Exercise", 2: "Diet"}


def getdate():
    import datetime
    return datetime.datetime.now()


try:
    print("Select Client Name:")
    for key, value in client_list.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input())

    print("Selected Client : ", client_list[client_name], "\n", end="")

    print("Press 1 to Log Data")
    print("Press 2 for Retrieving Data")
    op = int(input())

    if op == 1:
        for key, value in Log_list.items():
            print("Press", key, "to Log", value, "\n", end="")
        Log_name = int(input())
        print("Selected Job : ", Log_list[Log_name])
        f = open(client_list[client_name] + "_" + Log_list[Log_name] + ".txt", "a")
        k = 'y'
        while k != "n":
            print("Enter", Log_list[Log_name], "\n", end="")
            my_input = input()
            f.write("[ " + str(getdate()) + " ] : " + my_input + "\n")
            k = input("WANT TO ADD MORE? y/n:")
            continue
        f.close()
    elif op == 2:
        for key, value in Log_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        Log_name = int(input())
        print(client_list[client_name], "-", Log_list[Log_name], "Report :", "\n", end="")
        f = open(client_list[client_name] + "_" + Log_list[Log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("Invalid Input !!!")
except Exception as e:
    print("Wrong Input !!!")