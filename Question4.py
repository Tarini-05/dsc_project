def bottle_shipping(num_bottles):
    carton_sizes = {
        'xl': 48,
        'large': 24,
        'medium': 12,
        'small': 6
    }
    carton_count = {size: 0 for size in carton_sizes}
    for size, capacity in carton_sizes.items():
        if num_bottles >= capacity:
            carton_count[size] = num_bottles // capacity
            num_bottles %= capacity
    output = []
    for size in carton_count:
        if carton_count[size] > 0:
            output.append(f"{carton_count[size]} {size}")
    print(", ".join(output))
try:
    num_bottles = int(input("Enter the number of bottles to be shipped: "))
    bottle_shipping(num_bottles)
except ValueError:
    print("Please enter a valid integer.")
