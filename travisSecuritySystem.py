#Creating a travis the rediculous security system
known_users = ["Nik","Jack","Cloe","Emma","Fred","Michael"]

while True:
    print("Hi! My name is Travis.")

    print("What is your name?")
    name = input().strip().capitalize()  #using strip function to reduce the extra space, if enterd by user

    if name in known_users:
        print("Hello {}!".format(name))
        print("Do you want to get removed from the system (y/n)?")
        remove = input().strip().lower()
        if remove=="y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove=="n":
            print("No problem. I didn't want you to leave anyway!")

    else:
        print("Hmm I don't think  I have met you yet {} ".format(name))
        print("Would you like to be added to the system (y/n)")
        add_me = input().strip().lower()
        if add_me=="y":
            known_users.append(name)
            print(known_users)
        elif add_me=="n":
            print("No worries, see you around!")
