def calculate_power(base_val, exponent_val):
    result = base_val ** exponent_val
    return result

base_value = 2
exponent_value = 3

# This demonstrates how order matters in positional arguments!
# Since exponent_value (3) is passed first, it becomes 'base_val'
result = calculate_power(exponent_value, base_value)
print(result)