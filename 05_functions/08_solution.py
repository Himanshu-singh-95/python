# Keyword Arguments (**kwargs)

def print_kwargs (**kwargs):
    print(f"Keyword arguments received: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Usage
print_kwargs(name='Shaktiman', power='laser')
print_kwargs(name='Shaktiman', power='laser', enemy='Dr. Jackaal')