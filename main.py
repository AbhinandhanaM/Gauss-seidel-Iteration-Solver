# Gauss-Seidel Iteration Solver
# Solves a 3x3 system of linear equations

print("=" * 50)
print("       GAUSS-SEIDEL ITERATION SOLVER")
print("=" * 50)

print("\nEnter the 9 coefficients of Matrix A row by row.")
print("Example: 4 1 1")

A = []

for i in range(3):
    while True:
        try:
            row = list(map(float, input(f"Row {i + 1}: ").split()))
            if len(row) != 3:
                print("Please enter exactly 3 numbers.")
                continue
            A.append(row)
            break
        except ValueError:
            print("Please enter numbers only.")

print("\nEnter the 3 RHS constants of Vector B:")
while True:
    try:
        B = list(map(float, input("B: ").split()))
        if len(B) != 3:
            print("Please enter exactly 3 numbers.")
            continue
        break
    except ValueError:
        print("Please enter numbers only.")

# Check for zero diagonal elements
for i in range(3):
    if A[i][i] == 0:
        print("\nError: A diagonal coefficient cannot be zero.")
        print("The equations must be rearranged before applying Gauss-Seidel.")
        exit()

# Display the original system
print("\n" + "=" * 50)
print("SYSTEM OF LINEAR EQUATIONS")
print("=" * 50)

variables = ["x", "y", "z"]

for i in range(3):
    print(
        f"{A[i][0]:g}x + {A[i][1]:g}y + {A[i][2]:g}z = {B[i]:g}"
    )

# Display rearranged equations
print("\n" + "=" * 50)
print("REARRANGED EQUATIONS")
print("=" * 50)

print(f"x = ({B[0]:g} - ({A[0][1]:g})y - ({A[0][2]:g})z) / ({A[0][0]:g})")
print(f"y = ({B[1]:g} - ({A[1][0]:g})x - ({A[1][2]:g})z) / ({A[1][1]:g})")
print(f"z = ({B[2]:g} - ({A[2][0]:g})x - ({A[2][1]:g})y) / ({A[2][2]:g})")

# Initial guesses
print("\n" + "=" * 50)
print("INITIAL GUESSES")
print("=" * 50)

guess = input("Enter x0 y0 z0 (press Enter for 0 0 0): ").strip()

if guess == "":
    x, y, z = 0.0, 0.0, 0.0
else:
    try:
        values = list(map(float, guess.split()))
        if len(values) != 3:
            print("Invalid input. Using 0 0 0.")
            x, y, z = 0.0, 0.0, 0.0
        else:
            x, y, z = values
    except ValueError:
        print("Invalid input. Using 0 0 0.")
        x, y, z = 0.0, 0.0, 0.0

print(f"\n(x⁰, y⁰, z⁰) = ({x:.6f}, {y:.6f}, {z:.6f})")

# Number of iterations
while True:
    try:
        iterations = int(input("\nNumber of iterations (1-10): "))
        if 1 <= iterations <= 10:
            break
        print("Please enter a number from 1 to 10.")
    except ValueError:
        print("Please enter a whole number.")

# Gauss-Seidel iterations
print("\n" + "=" * 50)
print("GAUSS-SEIDEL ITERATIONS")
print("=" * 50)

for n in range(1, iterations + 1):

    # Gauss-Seidel:
    # New x is used immediately for calculating y and z
    new_x = (B[0] - A[0][1] * y - A[0][2] * z) / A[0][0]

    new_y = (B[1] - A[1][0] * new_x - A[1][2] * z) / A[1][1]

    new_z = (B[2] - A[2][0] * new_x - A[2][1] * new_y) / A[2][2]

    x, y, z = new_x, new_y, new_z

    print(f"Iteration {n}:")
    print(f"(x⁽{n}⁾, y⁽{n}⁾, z⁽{n}⁾) = "
          f"({x:.6f}, {y:.6f}, {z:.6f})")

# Final solution
print("\n" + "=" * 50)
print("FINAL SOLUTION")
print("=" * 50)

print(f"x = {x:.6f}")
print(f"y = {y:.6f}")
print(f"z = {z:.6f}")

print("\nThe iteration converges towards:")
print(f"({x:.6f}, {y:.6f}, {z:.6f})")

print("=" * 50)
print("        END OF PROGRAM")
print("=" * 50)