def sayhi():                    # First definition
    print("Hello User")

sayhi()                         # Works → prints: Hello User

def sayhi(name):                # Second definition (overwrites the first)
    print("Hello " + name)

sayhi("Shubham")                # Works → prints: Hello Shubham
sayhi("Bunty")                  # Works → prints: Hello Bunty

def sayhi(name, age):           # Third definition (overwrites previous one again)
    print("Hello " + name +  ", You are " + age)

sayhi("Shubham", "29")          # Works → prints: Hello Shubham, You are 29
sayhi("Bunty", "29")            # Works → prints: Hello Bunty, You are 29
