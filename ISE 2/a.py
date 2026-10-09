class Demo:
    def __init__(self):
        self.a = []
        self.even_count = 0
        self.odd_count = 0
        self.p_count = 0
        self.n_count = 0

    def user(self):
        n = int(input("Enter how many numbers: "))

        for i in range(n):
            num = int(input("Enter a number: "))
            self.a.append(num)

    def count(self):
        for i in self.a:
            if i % 2 == 0:
                self.even_count += 1
            else:
                self.odd_count += 1

            if i > 0:
                self.p_count += 1
            elif i < 0:
                self.n_count += 1

    def display(self):
        print("Even numbers:", self.even_count)
        print("Odd numbers:", self.odd_count)
        print("Positive numbers:", self.p_count)
        print("Negative numbers:", self.n_count)


d1 = Demo()
d1.user()
d1.count()
d1.display()
