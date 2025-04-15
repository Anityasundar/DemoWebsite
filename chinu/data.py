def sum_two_numbers_input():
  """Takes two numerical inputs from the user and prints their sum."""
  try:
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")

    num1 = float(num1_str)
    num2 = float(num2_str)

    sum_result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", sum_result)

  except ValueError:
    print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
  sum_two_numbers_input()
