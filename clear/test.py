def p(x):
    return x

def test_yield():
    yield p(2)
    yield p(20)

def main():
    pi = test_yield()
    print(pi)
    number = next(test_yield())
    print(number, pi)
    number = next(test_yield())
    print(number, pi)

if __name__ == "__main__":
    main()