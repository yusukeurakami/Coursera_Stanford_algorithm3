from heapq import heapify, heappush, heappop

class Hoffman():
    def __init__(self):
        self.char_n = 0
        self.char_list = []

    def readfile(self):
        File = open('huffman.txt')
        self.char_n = int(File.readline().strip())
        data = [int(x.strip()) for x in File.readlines()]

        for id in range(self.char_n):
            char_object = [data[id], [str(id), "", 0]]
            heappush(self.char_list, char_object)

        heapify(self.char_list)


    def main(self):
        while(len(self.char_list)>1):
            low = heappop(self.char_list)
            high = heappop(self.char_list)
            for x in low[1:]:
                x[1] = "0" + x[1]
                x[2] += 1
            for x in high[1:]:
                x[1] = "1" + x[1]
                x[2] += 1
            heappush(self.char_list, [low[0]+high[0]] + low[1:] +  high[1:])

        # print(self.char_list)

        min_len = self.char_n
        max_len = 0

        for x in self.char_list[0][1:]:
            if x[2] > max_len:
                max_len = x[2]
            if x[2] < min_len:
                min_len = x[2]
        print("min", min_len)
        print("max", max_len)

if __name__ == "__main__":
    solver = Hoffman()
    solver.readfile()
    solver.main()

        

