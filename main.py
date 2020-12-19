def main():
    user = int(input("enter the no u want : "))
    boolean = int(input("choose 1 or 0 : "))
    convert = bool(boolean)
    if convert == True :
        for i in range(user):
            for j in range(i+1):
                print("*", end="")
            print("")
    else:
        for i in range(user):
            for j in range(user-i):
                print("*", end="")
            print("")
main()
for i in range(10):
    s = input("want to run again..\n press y for yes and n for no : ")
    if s == "y":
        main()
    else:
        print("\n thank U")
        exit()


