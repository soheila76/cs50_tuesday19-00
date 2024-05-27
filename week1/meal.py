def main():
    time=input("What time is it?")
    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 19.0:
        print("dinner time")
    else:
        return

def convert(time):
    x,y= time .split(":")
    h=float(x)
    m=float(y) *1 / 60
    return float(h+m)


if __name__ == "__main__":
    main()

