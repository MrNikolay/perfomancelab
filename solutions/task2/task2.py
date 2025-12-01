import sys

def read_ellipse(path):
    with open(path) as f:
        h, k = map(float, f.readline().split())
        a, b = map(float, f.readline().split())

    return h, k, a, b


def read_points(path):
    pts = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            pts.append(tuple(map(float, line.split())))

    return pts


def classify(h, k, a, b, x, y):
    dx = x - h
    dy = y - k
    v = (dx*dx)/(a*a) + (dy*dy)/(b*b)
    
    if v == 1:
        return 0
    elif v < 1:
        return 1
    else: 
        return 2


def main():
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    h, k, a, b = read_ellipse(ellipse_file)
    points = read_points(points_file)

    for x, y in points:
        print(classify(h, k, a, b, x, y))


if __name__ == "__main__":
    main()
