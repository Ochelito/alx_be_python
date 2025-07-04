import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)


    numerator=(sys.argv[1])
    denominator=(sys.argv[2])

    result=safe_divide(numerator, denominator)

     # Only prefix with "Result:" if it's a valid number
    if isinstance(result, (int, float)):
        print(f"The result of the division is {result:.1f}")

    else:
        print(result)
    

if __name__ == "__main__":
    main()