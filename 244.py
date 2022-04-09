# # (A)
# n = input()
# s = input()
# print(s[-1])

# (B)
# N = input()
# T = input()
# X = [0,0]
# DIRECTIONS = ["E","W","S","N"]
# NOW_DIRECTION = [0]
# for _ in range(len(T)):
#     if T[_] == "S":
#         if DIRECTIONS[NOW_DIRECTION] == "E":
#             X += [1,0]
#         if DIRECTIONS[NOW_DIRECTION] == "W":
#             X += [0,-1]
#         if DIRECTIONS[NOW_DIRECTION] == "S":
#             X += [-1,0]
#         if DIRECTIONS[NOW_DIRECTION] == "N":
#             X += [0,1]
#     else:
#         if NOW_DIRECTION != [3]:
#             NOW_DIRECTION += 1
#         else:
#             NOW_DIRECTION = [0]
# print(X)


