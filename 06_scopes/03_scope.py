x = 99  # Global

def f1():
    x = 88  # Local to f1
    
    def func2():
        print(x)  # Accesses f1's local x (88), not global x (99)
    
    func2()

f1()  # Prints: 88

def func3():
    global x  # Tells Python to use the global x
    x = 12    # Modifies the global variable
    print(x)  # Prints: 12

func3()
print(x)  # Prints: 12 (global x was changed)