class MyNode:
    def __init__(self, digit):
        if type(digit) is not int:
            raise TypeError("Value must be Integer")
        self.digit = int(digit)
        self.next = None

class MyList:
    def __init__(self, *digits):
        self.head = None
        for digit in digits:
            if self.head is None:
                self.head = MyNode(digit)
                self.last = self.head
            else:
                self.last.next = MyNode(digit)
                self.last = self.last.next

    def addNode(self, digit):
        if self.head is None:
            self.head = MyNode(digit)
            self.last = self.head
        else:
            self.last.next = MyNode(digit)
            self.last = self.last.next

    def removeByValue(self, value):
        temp = self.head
        last = None
        while temp:
            if temp.digit == value:
                if temp == self.head:
                    self.head = temp.next
                else:
                    last.next = temp.next
                    temp = last
            last = temp
            temp = temp.next

    def removeByNumber(self, number):
        temp = self.head
        last = None
        while number:
            last = temp
            if temp.next != None:
                temp = temp.next
            else:
                return
            number -= 1
        if last:
            last.next = temp.next
        else:
            self.head = temp.next

    def find(self, number):
        temp = self.head
        while number:
            if temp.next is None:
                return None
            temp = temp.next
            number -= 1
        return temp.digit

    def size(self):
        temp = self.head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        return size

    def __str__(self):
        temp = self.head
        out = ""
        while temp:
            out += str(temp.digit) + " "
            temp = temp.next
        if not out:
            return "List is empty!"
        else:
            return out

def numberToList(number=0):
    a = MyList()
    if number == 0:
        a.addNode(0)
    while number:
        a.addNode(number % 10)
        number //= 10
    return a

def main():
    a = numberToList(9876)
    print (a)

if __name__ == "__main__":
    main()