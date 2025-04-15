# A very simple program that greets the user by name.

def greet(name):
  """This function takes a name as input and prints a greeting."""
  print(f"Hello, {name}!")

if __name__ == "__main__":
  user_name = input("What is your name? ")
  greet(user_name)
