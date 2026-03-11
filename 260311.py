# # 프로그래밍 기초 1 - 2026/03/11(수)



# # region 기본 도형

# import turtle

# t = turtle.Turtle() # 객체 인스턴스
# t.shape("turtle")

# # # 삼각형
# # for _ in range(3) :
# #     t.forward(100)
# #     t.left(120)

# # # # 사각형
# # for _ in range(4) :
# #     t.forward(100)
# #     t.right(90)


# # turtle.mainloop()
# # turtle.bye()

# # endregion

# ======================== #


import sys
input = sys.stdin.readline

print("반지름을 입력해주세요 : ")
radius = int(input())

pi = 3.14
area = (radius**2) * pi

print(f"반지름 : {radius} / 원의 면적 : {area}")