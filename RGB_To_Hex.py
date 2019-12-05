def rgb(r, g, b):
    r = 0 if r < 0 else 255 if r > 255 else r
    g = 0 if g < 0 else 255 if g > 255 else g
    b = 0 if b < 0 else 255 if b > 255 else b
    return "%02X%02X%02X" % (r, g, b)

# best solution
# def rgb(r, g, b):
#     round = lambda x: (min(255, max(x, 0)))
#     return ("{:02X}"*3).format(round(r), round(g), round(b))
print(rgb(-1, 255, 0))