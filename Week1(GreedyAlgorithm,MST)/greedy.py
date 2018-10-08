from heapq import heappush, heappop
import itertools

class GreedySolver():
    def __init__(self):
        self.raw = []
        self.sorted_data = []
        self.readFile()

    def readFile(self):
        file = open('jobs.txt')
        lines = file.readlines()
        jobs_n = lines[0]
        lines = lines[1:]
        self.raw = [ x.strip('\n').split(' ') for x in lines]
        for i in range(len(self.raw)):
            job = [int(self.raw[i][0]), int(self.raw[i][1])]
            self.raw[i] = job

    def sort_diff(self):
        self.sorted_data = sorted(self.raw, key=lambda x: (x[0] - x[1], x[0]) , reverse=True)

    def sort_frac(self):
        self.sorted_data = sorted(self.raw, key=lambda x: (float(x[0]) / x[1], x[0]) , reverse=True)

    def addTime(self):
        time_counter = 0
        total = 0
        for i, job in enumerate(self.sorted_data):
            w, l = job[0], job[1]
            time_counter += l
            total += w * time_counter
        return total

if __name__ == "__main__":
    solver = GreedySolver()
    solver.sort_frac()
    frac_total = solver.addTime()
    print("Ratio: ",frac_total)

    solver.sort_diff()
    diff_total = solver.addTime()
    print("Diff: ", diff_total)