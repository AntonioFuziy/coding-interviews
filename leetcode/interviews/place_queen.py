def place_queens(n: int) -> list[list[int]]:
    def place_queens_rec(n: int, row: int, queens: list[int]) -> list[list[int]]:
        if row == n:
            return [queens]
        solutions = []
        for col in range(n):
          if all(abs(col - queens[i]) not in (0, row - i) for i in range(row)):
            solutions += place_queens_rec(n, row + 1, queens + [col])
        return solutions  
    return place_queens_rec(n, 0, [])

if __name__ == "__main__":
    print(place_queens(4))