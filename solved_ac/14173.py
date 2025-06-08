x11, y11, x12, y12 = map(int, input().split())
x21, y21, x22, y22 = map(int, input().split())

xs = [x11, x12, x21, x22]
ys = [y11, y12, y21, y22]
new_sidelength = [
    max(xs)-min(xs),
    max(ys)-min(ys)
]
print(max(new_sidelength)**2)