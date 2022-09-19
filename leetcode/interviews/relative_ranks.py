score = [123123,11921,1,0,123]
indexes = []
for i in range(len(score)):
  current_max = 0
  index_max = 0
  for s in range(len(score)):
    if score[s] >= current_max:
      current_max = score[s]
      index_max = s

  print(score)
  score[index_max] = -1
  indexes.append(index_max)
for j in range(len(score)):
  if j == 0:
    score[indexes[j]] = "Gold Medal"
  elif j == 1:
    score[indexes[j]] = "Silver Medal"
  elif j == 2:
    score[indexes[j]] = "Bronze Medal"
  else:
    score[indexes[j]] = str(j+1)

print(score)
print(indexes)