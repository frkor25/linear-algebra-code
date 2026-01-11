import numpy as np
from sympy import Matrix

def input_matrix():
    """Input interface for matrix entry"""
    print("\n" + "="*50)
    print("MATRIX INPUT")
    print("="*50)
    
    # Input m x n dimensions
    while True:
        try:
            rows = int(input("Rows(m): "))
            cols = int(input("columns(n): "))
            if rows <= 0 or cols <= 0:
                print("m or n must be positive integers!")
                continue
            break
        except ValueError:
            print("Error!")
    
    print(f"\nInsert values for the ({rows}x{cols}) matrix:")
    print("-" * 50)
    
    # Input matrix elements
    data = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    val = float(input(f"Element [{i+1},{j+1}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("Insert a valid number!")
        data.append(row)
    
    return np.array(data)

def print_matrix(matrix, title="Matrix"):
    """Pretty print matrix"""
    print(f"\n{title}:")
    print("-" * 50)
    print(matrix)
    print()

def main():
    """Main program"""
    A = input_matrix()
    print_matrix(A, "matrix")

if __name__ == "__main__":
    main()


