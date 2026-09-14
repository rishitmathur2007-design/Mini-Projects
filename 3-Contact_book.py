file_name="Book.txt"
def Add_contact():
    name=input("Enter Name:")
    num=input("Enter Number:")
    with open(file_name,"a") as file:
        file.write(name+","+num+"\n")
        print("Contact Added Successfully!!")
        return
def view_contact():
    try:
        with open(file_name,'r') as file:
            print("\n--------Contact List--------")
            for line in file:
                name,numb=line.strip().split(",")
                print("Name:",name)
                print("Number:",numb)
                print("--------------------------")
    except FileNotFoundError:
        print("No Contacts Available")
    return
def search_contact():
    sear_name=input("Enter Name:")
    with open(file_name,'r') as file:
        for line in file:
            name,numb=line.strip().split(",")
            if name.lower()==sear_name.lower():
                print("----Contact Found----")
                print("Name:",name)
                print("Number:",numb)
                return
            else:
                print("\nContact Not Found!")
                return
def del_contact():
    del_nm=input("Enter Name:")
    try:
        with open(file_name,'r') as file:
            lines=file.readlines()
        with open(file_name,'w') as file:
            found=False
            for line in lines:
                name,num=line.strip().split(",")
                if name.lower()!=del_nm.lower():
                    file.write(line)
                else:
                    found=True
            if found:
                print("Contact Deleted Successfully")
            else:
                print("Contact Not Found")
    except FileNotFoundError:
        print("No Contact found")
while True:
    print("1-Add Contact")
    print("2-View Contact")
    print("3-Search Contact")
    print("4-Delete Contact")
    print("5-Exit")
    ch=input("Enter your choice:")
    match ch:
        case '1':
            Add_contact()
        case '2':
            view_contact()
        case '3':
            search_contact()
        case '4':
            del_contact()
        case '5':
            print("Bye")
            break
