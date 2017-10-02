def main():
    print("Contact Manager 1.0")
    try:
       friends = []
       infile = open("contacts.txt", "r")
       line = infile.readline()
       while line:
           friends.append(line.rstrip("\n").split(","))
           line = infile.readline()
       infile.close()
    except FileNotFoundError:
        print("File not found!")
        print("Starting a new address book")
        friends = []



    choice = 0
    while choice != 4:
        print("1) Add friend")
        print("2) Look up a friends")
        print("3) Display friends")
        print("4) Quit")
        choice = eval(input())

        if choice == 1:
           print("Adding friend")
           name = input("Namn: ")
           phone = input("Mobil: ")
           email = input("Email: ")
           friends.append([name, phone, email])

        elif choice == 2:
             print("Look up a friend")
             keyword = input("Enter search term: ")
             for friend in friends:
                 if keyword in friend:
                    print(friend)

        elif choice == 3:
            print("Display all friends")
            for i in range(len(friends)):
                print(friends[i])

        elif choice == 4:
            print("Quitting...")
        else:
            print("Invalid response")


    outfile = open("contacts.txt", "w")
    for friend in friends:
        outfile.write(",".join(friend) + "\n")
    outfile.close()

if __name__ == '__main__':
    main()
