# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    executeFizzbuzz()

def executeFizzbuzz():
    for fizzbuzz in range(51):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("buzz")
            continue
        print(fizzbuzz)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Visitor')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
