"""
    Class for recording num_iterations, execution time etc.

    Designed to return python list

"""
from time import time, time_ns
from sorting.quick_sort import quick_sort


class Recorder(object):
    def __init__(self):
        self.exe_nano = []
        self.exe_sec = []

    def execute(self, F, *args, **kwargs):
        s = time()
        s_n = time_ns()
        F(*args, **kwargs)
        end = time()
        end_n = time_ns()

        self.exe_sec.append(end-s)
        self.exe_nano.append(end_n-s_n)

    def get_times(self):
        return self.exe_sec, self.exe_nano


if __name__ == '__main__':
    a = [5,8,4,6,2,3,1,1,2,5,6,8,6,4,5,8,9,6,2,1,3,2,5,6,2,3,4,5,4,6,4]
    recorder = Recorder()
    args = [a, 0, len(a)-1]
    recorder.execute(quick_sort, *args)
    print(recorder.get_times())