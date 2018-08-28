know_users=["Alice","Bob","Claire","Emma","Emma","Fred","Georgie","Harry"]


while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().lower().title()

    if name in know_users:
        print("Name recognised! Welcome {}!".format(name))
        remove=input("Would you like to be removed from the database?(y/n): ").lower()

        if remove=="y":
            while name in know_users:
               know_users.remove(name)
        else remove=="n":
            print("No problem! See yaa")
    else:
        print("Hmm... I don't think we've met {}".format(name))
        add=input("Would you like to be added to the database?(y/n): ").lower()
        if add=="y":
            known_users.append(name)
        else remove=="n":
            print("No problem! See yaa")
