#add import
# main.py
from question_d import create_multiplication_table, display_multiplication_table

def main():
    while True:
        print("\nMultiplication Table:")
        table = create_multiplication_table()
        display_multiplication_table(table)
        
        choice = input("\nDo you want to continue? (yes/no): ")
        if choice.lower() != "yes":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
