def findOrder(numCourses,prerequisites):
  if len(prerequisites) == 0:
    return [0]

  courses = []
  requisites = {}

  for i in range(len(prerequisites)):
    if prerequisites[i][0] not in requisites.keys():
      requisites[i] = []
    if (prerequisites[i][0] in requisites.values()) and (prerequisites[i][1] in requisites.keys()):
      requisites[prerequisites[i][0]].append(prerequisites[i][1])
  
  # for k, v in requisites.items():
  #   if v not in courses:
  #     courses.append(v)

  # for i in range(len(prerequisites)):
  #   if prerequisites[i][0] not in courses:
  #     courses.append(prerequisites[i][0])
  
  print(requisites)
  # print(courses)

findOrder(4, [[1,0],[2,0],[3,1],[3,2]])

findOrder(2, [[1,0]])