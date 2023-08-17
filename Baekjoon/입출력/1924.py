x, y = map(int, input().split())

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

for i in range(x - 1):
    day += days[i]

print(week[(day + y) % 7])
