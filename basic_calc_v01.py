def greet():
    # Deafault instructions
    print("""----------Basic_Calculator----------
         **Enter 0 to exit**
Enter index corresponding to the desired operation
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division \n""")

def user_input():
    # Ask user to input numbers separated by commas or spaces
    num = input("Enter numbers-- separated by commas or spaces:\n")
    lis = [n for n in num.replace(',', ' ').split() if n.strip()]
    if not lis:
        print("No valid numbers.\n")
        return "Empty"

    num_list = []
    for n in lis:
        try:
            num_list.append(float(n))
        except Exception as e:
            print(f"Skipped input, something went wrong: {e}")
    return num_list


        
def add():
    numbers = user_input()
    if numbers == "Empty":
        pass
    else:
        print(f"The sum is: {sum(numbers)}\n")

def mult():
    numbers = user_input()
    if numbers == "Empty":
        pass
    else:   
        ans = 1
        for n in numbers:
            ans *= n
        print(f"The product is: {ans}\n")

def sub():
    numbers = user_input()
    if numbers == "Empty":
        pass
    else:
        ans = numbers[0]
        for n in numbers[1:]:
            ans -= n
        print(f"The subtraction is: {ans}\n")

def div():
    numbers = user_input()
    if numbers == "Empty":
        pass
    else:
        ans = numbers[0]
        try:
            for n in numbers[1:]:
                ans /= n
            print(f"The division is: {ans}\n")
        except ZeroDivisionError:
            print("Division by zero not allowed!!!\n")
        except Exception as e:
             print(f"Error: {e}\n")



greet()
while True:
    uin = input("Enter your choice: ").strip()
    if not uin:
        print("You entered nothing!!\nEnter a number between 1 to 4 (0 to exit):")
        continue
    try:
        x = int(uin)
        
        match x:
            case 0:
                print("Thank you for using my calculator.\nExiting...")
                break
            case 1:
                add()
            case 2:
                sub()
            case 3:
                mult()
            case 4:
                div()
            case _:
                print("Invalid input... \nEnter a number between 1 to 4 (0 to exit):Try again!!!")
    except ValueError:
        print("Invalid input!!! \nEnter a number between 1 to 4 (0 to exit):")



