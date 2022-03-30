import os
import collections
import re

path = ""
folder_to_track = os.path.normpath(path)

#categorize files based on extensions
def extension_category():
    try:
        file_mappings = collections.defaultdict()
        for filename in os.listdir(folder_to_track):
            if not os.path.isdir(os.path.join(folder_to_track, filename)):
                file_type = filename.split('.')[-1]
                file_mappings.setdefault(file_type, []).append(filename)

        for folder_name, folder_items in file_mappings.items():
            folder_path = os.path.join(folder_to_track, folder_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            for folder_item in folder_items:
                source = os.path.join(folder_to_track, folder_item)
                destination = os.path.join(folder_path, folder_item)
                os.rename(source, destination)

    except Exception as e:
        print(e)

#categorize files based on keyword
def name_category():
    file_mappings = collections.defaultdict()
    sub_file_names = []
    file_names = []
    delimiters = ['.', ',', '!', ' ', '-', ';', '?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '/', '|', '<', '>']
    if os.listdir(folder_to_track).__len__() == 0:
        try:
            for filename in os.listdir(folder_to_track):
                filename = filename.lower()
                file_names.append(filename)
                sub_file_names = find_common_keyword(file_names)

            for filename in os.listdir(folder_to_track):
                if not os.path.isdir(os.path.join(folder_to_track, filename)):
                    for sub_file_name in sub_file_names:
                        file_mappings.setdefault(sub_file_name, []).append(filename)

            for folder_name, folder_items in file_mappings.items():
                folder_path = os.path.join(folder_to_track, folder_name)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
                    
                    for filename in file_names:
                        filename = filename.lower()
                        i = 1
                        regexPattern = '|'.join(map(re.escape, delimiters))
                        splittedstring = re.split(regexPattern, filename, 0)
                        if folder_name in splittedstring:
                            new_name = filename
                            file_exits = os.path.isfile(folder_path + '\\' + new_name)
                            while file_exits:
                                i += 1
                                new_name = os.path.splitext(folder_to_track + '\\' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + new_name)[1]   
                                new_name = new_name.split("\\")[4]
                                file_exits = os.path.isfile(folder_path + "\\" + new_name)
                            src = folder_to_track + "\\" + filename
                            new_name = folder_path + "\\" + new_name
                            os.rename(src, new_name)
            
            for filename in os.listdir(folder_to_track):
                if not os.path.isdir(os.path.join(folder_to_track, filename)):
                    file_mappings.setdefault('other', []).append(filename)

            for folder_name, folder_items in file_mappings.items():
                folder_path = os.path.join(folder_to_track, folder_name)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                    for filename in os.listdir(folder_to_track):
                        filename = filename.lower()
                        i = 1
                        regexPattern = '|'.join(map(re.escape, delimiters))
                        splittedstring = re.split(regexPattern, filename, 0)
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            new_name = filename
                            file_exits = os.path.isfile(folder_path + '\\' + new_name)
                            while file_exits:
                                i += 1
                                new_name = os.path.splitext(folder_to_track + '\\' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + new_name)[1]   
                                new_name = new_name.split("\\")[4]
                                file_exits = os.path.isfile(folder_path + "\\" + new_name)
                            src = folder_to_track + "\\" + filename
                            new_name = folder_path + "\\" + new_name
                            os.rename(src, new_name)
            
        except Exception as e:
            print(e)
    else:
        print(f'{folder_to_track} is either empty or not organizable')

#secondary functions
from collections import Counter

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
