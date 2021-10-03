def run(json):
    for y, row in enumerate(json):
        for x, stone in enumerate(row):
            if stone is None:
                return x, y
