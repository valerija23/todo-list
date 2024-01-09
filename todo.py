def add(list, item):
  pass


def remove(list, index):
  pass


def clear(list):
  pass


def print_list(list):
  pass


list = []
print("List is empty now, what you want to do?")
while True:
  choice = int(input("1. Add\n2. Remove\n3. Clear\n4. Print list\n"))
  if choice == 1:
    item = input("What you want to add?\n")
    add(list, item)
    print_list(list)
  elif choice == 2:
    index = int(input("What you want to remove?\n"))
    remove(list, index)
    print_list(list)
  elif choice == 3:
    clear(list)
    print_list(list)
  elif choice == 4:
    print_list(list)
  else:
    print("Invalid input")
