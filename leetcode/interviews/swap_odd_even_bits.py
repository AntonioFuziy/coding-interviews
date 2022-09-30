def swap_odd_even_bits(x: int) -> int:
  odds = 0x55555555 
  evens = 0xAAAAAAAA
  x = (x & odds) << 1 | (x & evens) >> 1
  return x