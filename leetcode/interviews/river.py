def check_neighbors(land: list[list[int]], i: int, j: int, size: int) -> int:
  buffer = []
  buffer.append([i, j])
  land[i][j] = -1
  river_size = 1
  while len(buffer) > 0:
    [x, y] = buffer[0]
    buffer = buffer[1:]
    for r in [-1, 0, 1]:
      for c in [-1, 0, 1]:
        if x+r >= 0 and y+c >= 0 and x+r < size and y+c < size and land[x+r][y+c] == 0:
          land[x+r][y+c] = -1
          river_size += 1
          buffer.append([x+r, y+c])
  return river_size

def compute_pond_sizes(land: list[list[int]]) -> list[int]:
  river_sizes = []
  for i in range(len(land)):
    for j in range(len(land[i])):
      if land[i][j] == 0:
        river_sizes.append(check_neighbors(land, i, j, len(land)))

  for i in range(len(land)):
    for j in range(len(land[i])):
      if land[i][j] == -1:
        land[i][j] = 0
  return river_sizes