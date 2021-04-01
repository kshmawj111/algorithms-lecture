"""
    Class for recording num_iterations, execution time etc.

    call by "execute" method with argument with F: function and args.

    returns Dict type which contains the history

"""
from time import time, time_ns
from sorting.quick_sort import quick_sort
import pandas as pd


class Recorder(object):
    def __init__(self):
        self.record = {}

    # method for executing a specific function given as F
    def execute(self, F, *args, **kwargs):
        self.initialize_F_info(F)

        s = time()
        s_n = time_ns()
        F(*args, **kwargs)
        end = time()
        end_n = time_ns()

        self.record[F.__name__]['sec'].append(end-s)
        self.record[F.__name__]['nano'].append(end_n - s_n)

    # getter
    def get_times(self):
        return self.record

    # add function info to member dictionary containing execution times
    def initialize_F_info(self, F):
        fun_name = F.__name__

        if fun_name not in self.record.keys():
            self.record[fun_name] = {'nano': [], 'sec': []}

"""

    Guide for using recorder object
    
"""
if __name__ == '__main__':
    a = [5,8,4,6,2,3,1,1,2,5,6,8,6,4,5,8,9,6,2,1,3,2,5,6,2,3,4,5,4,6,4]
    recorder = Recorder()
    args = [a, 0, len(a)-1]
    recorder.execute(quick_sort, *args)
    record = recorder.get_times()

    print(record)
    df = pd.DataFrame.from_dict(record, orient='index')
    print(df)