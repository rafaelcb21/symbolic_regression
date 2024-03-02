import csv
import importlib
from inspect import getmembers, isfunction
from line_profiler import LineProfiler
import random
import string


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Load the module algorithm.py
functions_module = importlib.import_module("algorithm")

def remove_functions(functions_list):
    list = []
    for study_func in functions_list:
        function_name = study_func.__name__
        if function_name not in ['siftdown']:
            list.append(study_func)
    return list

# Get all functions from module
all_functions_list = [func[1] for func in getmembers(functions_module) if isfunction(func[1])]
functions_list = remove_functions(all_functions_list)

n_max = 1000
id_func = 1
list_to_csv = []
# csv_file_path = 'output.csv'
column_titles = ['function_id', 'function_name', 'n', 'code_line', 'hits', 'time']

for study_func in functions_list:
    print(study_func.__name__)
    for n in range(2, n_max + 1):
        random_numbers = random.choices(range(10000), k=n)
        function_name = study_func.__name__
        string1 = generate_random_string(n)
        string2 = generate_random_string(n)

        lprofiler = LineProfiler()
        lp_wrapper = lprofiler(study_func)

        if function_name in ['insertion_sort', 'insertion_sort_bin', 'selection_sort', 'shell', 'quick_sort', 'heapsort']:
            lp_wrapper(random_numbers)
        elif function_name in ['binary_search', 'binary_search_recursive']:
            lp_wrapper(sorted(random_numbers))
        elif function_name in ['levenshteinDistance']:
            lp_wrapper(string1, string2)
            # print(n)
        else:
            lp_wrapper(n)

        stats = lprofiler.get_stats()
        # lprofiler.print_stats(output_unit=1e-03)

        line_numbers = []
        hits = []
        time = []

        for line in stats.timings.values():
            for i in line:
                line_numbers.append(i[0])
                hits.append(i[1])
                time.append(i[2])

        for index, code_line in enumerate(line_numbers):
            list_to_csv.append([id_func, function_name, n, code_line, hits[index], time[index]])
    
    with open(function_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_titles)
        for row in list_to_csv:
            writer.writerow(row)

    list_to_csv = []
    id_func  += 1


