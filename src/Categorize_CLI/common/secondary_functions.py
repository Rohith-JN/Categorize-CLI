#secondary functions
from collections import Counter
import os
import re
import time
from .extensions import *
from progress.bar import IncrementalBar 


UNITS_MAPPING = [
    (1<<50, ' PB'),
    (1<<40, ' TB'),
    (1<<30, ' GB'),
    (1<<20, ' MB'),
    (1<<10, ' KB'),
    (1, (' byte', ' bytes')),
]


def calc_size(bytes, units=UNITS_MAPPING):
    for factor, suffix in units:
        if bytes >= factor:
            break
    amount = int(bytes / factor)

    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix


def find_prefixes(strings):
    prefix_cnts = Counter()                   
    pattern = re.compile('[^a-zA-Z0-9]')     
    for string in strings:
        arr = pattern.split(string)  
        for pos, prefix in enumerate(arr[:-1]):
            if not prefix.isdigit():
                prefix_cnts[f'{prefix} {pos}'] += 1     
    
    prefix_cnts = {k:v for k, v in prefix_cnts.items() if v > 1}
    prefix_cnts = sorted(prefix_cnts.items(), key = lambda kv: (-kv[1], int(kv[0].split()[1])))
    prefixes = [k for k, v in prefix_cnts]
    prefix_cnts = Counter(prefixes)

    for string in strings:
        arr = pattern.split(string)  
        for pos, prefix in enumerate(arr[:-1]):   
            token = f'{prefix} {pos}'
            if token in prefixes:
                prefix_cnts[token] += 1           
                break
           
    prefixes = {k.split()[0] for k, v in prefix_cnts.items() if v > 1}
    mapping = {}

    for string in strings:
        arr = pattern.split(string)   
        for prefix in arr[:-1]:   
            if prefix in prefixes:
                mapping[string] = prefix
                break
        else:
            mapping[string] = 'other'
                
    return prefixes


def find_common_keyword(filenames):
    final = []
    sub_strings = []
    delimiters = ['.', ',', '!', ' ', '-', ';', '?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '/', '|', '<', '>']
    
    for filename in filenames:
        filename = filename.lower()
        filename = filename.split('.')[0]
        regexPattern = '|'.join(map(re.escape, delimiters))
        sub_string = re.split(regexPattern, filename, 0)
        sub_strings.append(sub_string[0])

    for sub_string in sub_strings:
        if sub_strings.count(sub_string) > 1 and not sub_string.isdigit() and sub_string != '':
            final.append(sub_string)

    return set(final)


def get_key(val):
    for key, value in extensions.items():
         if val == value:
             return key

def check_files(folder_to_track):
    files = os.listdir(folder_to_track)
    isdir = any(os.path.isdir(os.path.join(folder_to_track, file + '//')) for file in files)
    allisdir = all(os.path.isdir(os.path.join(folder_to_track, file + '//')) for file in files)
    
    if allisdir or files.__len__() == 0:
        return False
    else: 
        return True


def moveIncrementing(source, destination):
    try:
        i = 0
        destination_name = os.path.splitext(destination)[0]
        destination_extension = os.path.splitext(destination)[-1]
        while True:
            try:
                if i == 0:
                    destination = destination_name + destination_extension
                else:
                    destination = destination_name + " " + "(" + str(i) + ")" + destination_extension

                return os.rename(source, destination if i else destination)
                
            except OSError as ex:
                i = i + 1
                pass
    except Exception as e:
        pass


def displayProgressbar(item_count):
    print(os.linesep)
    if (item_count > 0):
        bar = IncrementalBar('Organizing...', max=item_count)

        for i in range(item_count):
            bar.next()
            time.sleep(0.01)

        bar.finish()