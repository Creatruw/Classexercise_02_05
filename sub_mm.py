def sub(a, b):
    c = float(a) - float(b)
    return c


def fm(a):
    small = min(a)
    big = max(a)
    return small, big


def interface():
    print("c = a - b")
    a = input("please enter a:")
    b = input("please enter b:")
    answer = sub(a, b)
    print("the result is {}".format(answer))
    d = [1, 2, 3, 4, 5, 6]
    e, f = fm(d)
    print("the min value and the max value in the list are")
    print("{}, {}".format(e, f))


if __name__ == "__main__":
    interface()
