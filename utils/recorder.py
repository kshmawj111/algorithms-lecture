"""
    Class for recording num_iterations, execution time etc.

    call by "execute" method with argument with F: function and args.

    returns Dict type which contains the history

"""
from time import time, time_ns
from sorting.quick_sort import quick_sort
from sorting.merge_sort import merge_sort
import pandas as pd
from copy import copy


class Recorder(object):
    def __init__(self):
        self.record = {}

    # method for executing a specific function given as F
    def execute(self, F, original_data, *args, **kwargs):
        c_data = copy(original_data)
        self.initialize_F_info(F)

        new_arg = [c_data]
        for item in args:
            for i in item:
                new_arg.append(i)

        s = time()
        s_n = time_ns()

        F(*new_arg, **kwargs)
        end = time()
        end_n = time_ns()

        self.record[F.__name__]['sec'].append(end-s)
        self.record[F.__name__]['nano'].append(end_n - s_n)

    # add function info to member dictionary containing execution times
    def initialize_F_info(self, F):
        fun_name = F.__name__

        if fun_name not in self.record.keys():
            self.record[fun_name] = {'nano': [], 'sec': []}

    # getter
    def get_record(self):
        return self.record

    def get_record_df(self):
        df = pd.DataFrame.from_dict(self.record, orient='index')
        return df


"""

    Guide for using recorder object
    
"""
if __name__ == '__main__':
    a = [5,8,4,6,2,3,1,1,2,5,6,8,6,4,5,8,9,6,2,1,3,2,5,6,2,3,4,5,4,6,4]
    recorder = Recorder()
    args = [0, len(a)-1]
    recorder.execute(merge_sort, a, [0, len(a) - 1])
    record = recorder.get_record()

    print(record)
    df = pd.DataFrame.from_dict(record, orient='index')
    print(df)