import sys

if len(sys.argv) < 4:
    print("Usage: python calc.py <number_1> <number_2> <operation>")
    sys.exit(1)

try:
    num_1 = int(sys.argv[1])
    num_2 = int(sys.argv[2])
    operation = sys.argv[3]
except ValueError:
    print("Please write a number.")
    sys.exit(1)

operation_map = {
    "add": "+", "+": "+",
    "subtract": "-", "-": "-",
    "multiply": "*", "*": "*",
    "division": "/", "/": "/",
}

if operation not in operation_map:
    print("Please write a valid operation.")
    sys.exit(1)

op = operation_map[operation]

if op == "+":
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
elif op == "-":
    print(f"{num_1} - {num_2} = {num_1 - num_2}")
elif op == "*":
    print(f"{num_1} × {num_2} = {num_1 * num_2}")
elif op == "/":
    if num_2 == 0:
        print("Cannot divide by zero.")
        sys.exit(1)
    print(f"{num_1} ÷ {num_2} = {num_1 / num_2}")
else:
    print("Please write a valid operation.")
    sys.exit(1)
