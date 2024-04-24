def add_contact(contact_list):
    def add(name,phone):
        contact_list[name]=phone
        print(f"Contact'{name}'added successfully.")
    return add

def delete_contact(contact_list):
    def delate(name):
        if name in contact_list:
            del contact_list[name]
            print(f"Contact'{name}'delate successfully.")
        else:
            print(f"Contact'{name} not found.'")
    return delate

def search_contact(contact_list):
    def search(name):
        if name in contact_list:
            print(f"Nmae:{name}, Phone:{contact_list[name]}")
        else:
            print(f"Contact'{name}'not found.")
    return search

def view_contacts(contact_list):
    def view():
        if contact_list:
            print("Contacts:")
            for name, phone in contact_list.items():
                print(f"Name:{name},Phone:{phone}")
        else:
            print("Contact list is empty.")
    return view


contacts={}

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2.Delete Contact")
    print("3.Search Contact")
    print("4.View Contacts")
    print("5.Exit")

    choice=input("Enter your choice:")

    if choice=='1':
        name=input("Enter contact name:")
        phone=input("Enter contact phone number:")
        add=add_contact(contacts)
        add(name,phone)
    elif choice=='2':
        name=input("Enter contact name to delete:")
        delete=delete_contact(contacts)
        delete(name)
    elif choice=='3':
        name=input("Enter contact name to search:")
        search=search_contact(contacts)
        search(name)
    elif choice=='4':
        view=view_contacts(contacts)
        view()
    elif choice=='5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice.Please enter a number between 1 and 5.")
        

