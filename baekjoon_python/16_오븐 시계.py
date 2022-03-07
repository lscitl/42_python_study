h, m = input().split(" ")
c = input()

t = int(h) * 60 + int(m) + int(c)
if t // 60 > 23:
    t_h = t // 60 - 24
else:
    t_h = t // 60
t_m = t % 60
print("{} {}".format(t_h, t_m))