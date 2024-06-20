inventory = {
    "laptop" : {
        "quantity": "10",
        "price": "2000"
    },
    "chair": {
        "quantity": "40",
        "price": "450"
    }
}

while True:
    print("\n=== Inventory Management System ===")

    print("\nwhat do u want to do?\n1. search for an item\n2. create new item\n3. add item into inventory\n4. purchase an item\n5. return an item\n6. delete an item no longer sold\n7. calculate total number of stocks in inventory\n8. exit program\n")
    action = input("enter an action: ")

    if action == "1":
        search_item = input("\ntype in a name to search: ")
        for key, value in inventory.items():
            if key == search_item:
                print("\nITEM FOUND!!!!")
                print(f"item name: {key}")
                for nest_key in value:
                    print(f"{nest_key}: {value[nest_key]}")
    elif action == "2":
        pass
    elif action == "3":
        pass
    elif action == "4":
        pass
    elif action == "5":
        pass
    elif action == "6":
        pass
    elif action == "7":
        pass
    elif action == "8":
        pass
    else:
        print("ONLY CHOOSE FROM THE CHOICES GIVEN!!!!!!!!!")
