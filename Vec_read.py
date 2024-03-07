from Vect import Vectors

class VectorsReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        all_vect = []
        with open(self.file_name) as f:
            for line in f:
                args = list(map(int, line.strip().split()))
                vector = Vectors(*args)
                vect = [vector.dimension(), vector.length(), vector.middle(), vector.max(), vector.min()]
                all_vect.append(vect)
        return all_vect

    def worker(self):
        all_vect = self.read()
        res_1 = max(all_vect, key=lambda x: (x[0], x[1]))
        res_2 = max(all_vect, key=lambda x: (x[1], -x[0]))
        mid = sum(vect[1] for vect in all_vect) / len(all_vect)
        print(f"The biggest dimension: {res_1}")
        print(f"The biggest length: {res_2}")
        print(f"The middle: {mid}")

if __name__ == '__main__':
    reader = VectorsReader('input01.txt')
    print(*reader.read())
    reader.worker()
