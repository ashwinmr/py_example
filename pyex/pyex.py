import re

def main():

  str = "Hello World"

  if(re.fullmatch(".*el.*",str)):
    print("Matched")
  else:
    print("Not Matched")

if __name__ == "__main__":
  main()
