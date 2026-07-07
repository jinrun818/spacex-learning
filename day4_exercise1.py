# Day 4 - 火箭速度计算器

print("=== 火箭速度计算器 ===")

distance = float(input("输入距离 (公里): "))
time = float(input("输入时间 (分钟): "))

speed = distance / time
print("火箭速度是", round(speed, 2), "公里/分钟")

speed_hour = speed * 60
print("每小时速度是", round(speed_hour, 2), "公里/小时")