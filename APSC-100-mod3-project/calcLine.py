def calcLine(xi, yi, xg,yg):  # intial rover positions and destination positions on 2D grid. Change as we find out the input format
    m = float((yg - yi) / (xg - xi))
    b = float((yi) - (xi * m))

    return (m, b)  # make this a tuple