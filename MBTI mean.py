"""MBTI what in 4 letters mean?"""

def main():
    """MBTL mean input"""
    print("your mbtl: _ _ _ _ (4 letters only! no other punc & space)")
    mbtl = input("input: ")
    if mbtl.isalpha() and len(mbtl) == 4:
        m, b, t, l = mbtl.upper()
        print()
        print("You have a:")
        if m == "I":
            print("I = Introvert")
        elif m == "E":
            print("E = Extrovert")
        else:
            print("? = ???")
        if b == "S":
            print("S = Sensing")
        elif b == "N":
            print("N = Intuition")
        else:
            print("? = ???")
        if t == "T":
            print("T = Thinking")
        elif t == "F":
            print("F = Feeling")
        else:
            print("? = ???")
        if l == "J":
            print("J = Judging")
        elif l == "P":
            print("P = Perceiving")
        else:
            print("? = ???")
    else:
        print("input error")

if __name__ == '__main__':
    main()
