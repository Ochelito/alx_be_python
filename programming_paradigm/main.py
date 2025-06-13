import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    try:
        numerator = float(sys.argv[1])
        denominator = float(sys.argv[2])

    except ValueError:
        print("Error: Please enter numeric values only.")
        return

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()