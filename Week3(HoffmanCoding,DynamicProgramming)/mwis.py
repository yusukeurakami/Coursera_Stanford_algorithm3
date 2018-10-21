class MWIS():
    def __init__(self):
        self.node_n = 0
        self.G = self.readfile()
        self.A = [0] * (1+self.node_n)
        self.IS = []

    def readfile(self):
        File = open('test.txt')
        self.node_n = int(File.readline())
        return [ int(x.strip()) for x in File.readlines() ]

    def scan(self):
        self.A[1] = self.G[0]
        for i in range(2, self.node_n+1):
            self.A[i] = max(self.A[i-1], self.A[i-2]+self.G[i-1] )

    def reconstruction(self):
        i = len(self.A)-1
        # print(i)
        while i>= 1:
            if self.A[i-1] >= self.A[i-2] + self.G[i-1]:
                i -= 1
            else:
                self.IS.append(i)
                i -= 2

    def check_include(self):
        check_list = [1, 2, 3, 4, 17, 117, 517, 997]
        result = ""
        for x in check_list:
            if x in self.IS:
                result += "1"
            else:
                result += "0"
        return result


    def main(self):
        self.scan()
        self.reconstruction()
        print(self.check_include())

        

if __name__ == "__main__":
    solver = MWIS()
    solver.main()
    # print(solver.node_n)
    # print(solver.G)
    # print(solver.IS)