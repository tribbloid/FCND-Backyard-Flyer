import inspect


def whoami() -> str:
    frame = inspect.currentframe()
    return inspect.getframeinfo(frame).function


def log():
    name = whoami()
    print(name, "...")


def distExp2(p1, p2):
    """"
    both using NED
    """
    nn = p1[0] - p2[0]
    ee = p1[1] - p2[1]
    dd = p1[2] - p2[2]
    return nn*nn + ee*ee + dd*dd
