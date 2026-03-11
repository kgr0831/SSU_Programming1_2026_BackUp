# # 프로그래밍 기초 1 - 2026/03/11(수)

# region turtle 라이브러리

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

# # # #  원
# import turtle

# t = turtle.Turtle()

# t.shape("turtle")
# t.circle(50)
# t.fd(30)
# t.circle(50)


# # turtle.mainloop()
# # turtle.bye()

# # endregion

# ====================================== #

# region 원의 면적 계산

# import sys
# input = sys.stdin.readline

# print("반지름을 입력해주세요 : ")
# radius = int(input())

# pi = 3.14
# area = (radius**2) * pi

# print(f"반지름 : {radius} / 원의 면적 : {area}")

# endregion

# ====================================== #

# region 별까지의 거리 계산하기

distance = 40 * (10**12)
yearVelocity = 300000 * 3600 * 24 * 365 # 빛이 1년간 가는 거리(광년 속도)

print(distance / yearVelocity)

# endregion
