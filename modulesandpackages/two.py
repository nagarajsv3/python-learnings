import one

print("TOP Level in two.py")

one.func()

if __name__ == "__main__":
    print("two.py is run directly")
else:
    print("two.py is imported")