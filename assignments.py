class Week2:
    a = 0
    b = 0

    def a1(self):
        self.a = int(input())
        print(self.a)

    def a2(self):
        self.a, self.b = input().split(" ")
        self.a = int(self.a)
        self.b = int(self.b)
        print(self.a * self.b)

    def a3(self):
        self.a, self.b = input().split(" ")
        self.a = int(self.a)
        self.b = int(self.b)
        if self.a > self.b:
            print(self.a)
        else:
            print(self.b)


class Week3:
    a = 0
    b = 0
    n = 0

    def a1(self):
        self.a = [int(i) for i in input().split()]
        for i in self.a:
            if abs(i) % 10 != 4:
                print(i, end=" ")

    def a2(self):
        self.a = [int(i) for i in input().split()]
        self.b = []
        for i in self.a:
            if i not in self.b:
                self.a.append(i)
        self.b.sort()
        if (len(self.b) == 1):
            print(2 * self.b[0])
        else:
            print(self.b[1] + self.b[-2])

    def a3(self):
        self.n = int(input())
        self.a = [int(i) for i in input().split()]
        self.b = []
        for i in self.a:
            if i not in self.b:
                self.b.append(i)
                print(i, end=" ")

