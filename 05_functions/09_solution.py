#  Even Number Generator(yield)

def even_number_generator(limit):
    """Generator to yield even numbers up to a specified limit."""
    for number in range(0, limit + 1, 2):
        yield number