#add import
# main.py
from question_a import find_lowest, find_highest, calculate_total, calculate_average

def main():
    numbers = [float(input("Enter number {}: ".format(i+1))) for i in range(5)]
    
    lowest = find_lowest(numbers)
    print("The lowest number is:", lowest)
    
    highest = find_highest(numbers)
    print("The highest number is:", highest)
    
    total = calculate_total(numbers)
    print("The total of the numbers is:", total)
    
    average = calculate_average(numbers)
    print("The average of the numbers is:", average)

if __name__ == "__main__":
    main()
