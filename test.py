# This program demonstrates on the stacks in python
# This is done by using the list data structures
stack = []
size = int(input("Enter the size of the stack to be created :"))


def add_to_stack(item):
    if len(stack) < size:
        stack.append(item)
    else:
        print("The stack is overflowing. The requested element is not added")


def rm_stack(index=(len(stack)-1)):
    if len(stack) > 0:
        stack.pop(index)
    else:
        print("The stack is underflow.")


def display():
    print(stack)


choice = 0
print("\t\t\t1.Append\n\t\t\t3.Pop\n\t\t\t3.display\n\t\t\t4.Quit")

while choice != 4:

    choice = int(input("Enter option: "))
    if choice == 1:
        if len(stack) < size:
            add_to_stack((input("Enter the element to be added: ")))
        else:
            print("The stack is already full")
    elif choice == 2:
        rm_stack(int(input("Enter the index to pop:")))
    elif choice == 3:
        display()
    else:
        print("Quitting..")
