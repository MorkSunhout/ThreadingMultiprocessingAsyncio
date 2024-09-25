import random

def generate_numbers_file(filename, num_numbers, min_value, max_value):
    """Generates a file with random numbers."""
    full_path = f'ThreadingMultiprocessingAsyncio\{filename}' 
                                                              
    with open(full_path, "w") as f:
        for _ in range(num_numbers):
            number = random.randint(min_value, max_value)
            f.write(f"{number}\n")
    print(f"File '{filename}' with {num_numbers} random numbers generated.")
