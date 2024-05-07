#add import
# main.py
from question_b import stock_purchase_history

def main():
    while True:
        print("\nMenu:")
        print("1- Display stock purchase history")
        print("2- Exit")
        
        option = input("Enter your choice: ")
        
        if option == "1":
            stock_purchase_history()
        elif option == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
