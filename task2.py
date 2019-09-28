from task1 import MyList, numberToList
def main():
    l1 = numberToList(input("please enter da first number list "))
    l2 = numberToList(input("please enter da second number list "))
    if l1.size() >= l2.size():
        large = l1
        small = l2
    else:
        large = l2
        small = l1
    lsize = large.size()
    ssize = small.size()
    new = MyList()
    fl = 0
    for i in range (0, ssize):
        temp = small.find(i) + large.find(i) + fl
        new.addNode(temp % 10)
        fl = temp // 10
    for j in range (i + 1, lsize):
        print(j)
        temp = large.find(j) + fl
        new.addNode(temp % 10)
        fl = temp // 10
    if fl:
        new.addNode(1)
    print(new)


if __name__ == "__main__":
    main()

