from datetime import datetime
import os
import collections
import re
from extensions import *
from Secondary_functions import *
import time
from datetime import timedelta

#Group 1: Organize files based on extension
def all_extensions_category(folder_to_track):
    movedFiles = False
    count = 0
    start_time = time.monotonic()
    if check_files(folder_to_track):
        for file in os.listdir(folder_to_track):
            if not os.path.isdir(os.path.join(folder_to_track, file)):
                try:
                    file_mappings = collections.defaultdict()

                    for filename in os.listdir(folder_to_track):
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            file_type = filename.split('.')[-1]
                            file_mappings.setdefault(file_type, []).append(filename)
        
                    for folder_name, folder_items in file_mappings.items():
                        folder_path = os.path.join(folder_to_track, folder_name)
                        folder_exists = os.path.exists(folder_path)

                        if not folder_exists:
                            os.mkdir(folder_path)
        
                            for folder_item in folder_items:
                                source = os.path.join(folder_to_track, folder_item)
                                destination = os.path.join(folder_path, folder_item)
                                moveIncrementing(source, destination)
                                count = count + 1
                                movedFiles = True
                                
                        if folder_exists:
                            for folder_item in folder_items:
                                source = os.path.join(folder_to_track, folder_item)
                                destination = os.path.join(folder_path, folder_item)
                                count = count + 1
                                moveIncrementing(source, destination)
                                movedFiles = True

                    end_time = time.monotonic()

                    if movedFiles:
                        if count == 1:
                            return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                        else:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                    else:
                        return "Couldn't move files"
                            
                except Exception as e:
                    return f'{folder_to_track}: is either empty or not organizable'
    
    else:
        return f'{folder_to_track}: is either empty or not organizable'

def extension_category(extension, folder_to_track):
    start_time = time.monotonic()
    movedFiles = False
    count = 0
    if check_files(folder_to_track):
        for file in os.listdir(folder_to_track):
            if not os.path.isdir(os.path.join(folder_to_track, file)):
                try:
                    file_mappings = collections.defaultdict()
                    for filename in os.listdir(folder_to_track):
                        for value in extension:
                            if not os.path.isdir(os.path.join(folder_to_track, filename)) and any(filename.endswith(value) for filename in os.listdir(folder_to_track)) == True:
                                file_mappings.setdefault(get_key(extension), []).append(filename)

                    for folder_name, folder_items in file_mappings.items():
                        folder_path = os.path.join(folder_to_track, folder_name)
                        folder_exists = os.path.exists(folder_path)
                        if not folder_exists:
                            os.mkdir(folder_path)

                            for filename in os.listdir(folder_to_track):
                                for value in extension:
                                    if not os.path.isdir(os.path.join(folder_to_track, filename)) and filename.endswith(value):
                                        count = count + 1
                                        source = os.path.join(folder_to_track, filename)
                                        destination = os.path.join(folder_path, filename)
                                        moveIncrementing(source, destination) # move all files containing sub_file_name in their filenames
                                        movedFiles = True

                        if folder_exists:
                            for filename in os.listdir(folder_to_track):
                                for value in extension:
                                    if not os.path.isdir(os.path.join(folder_to_track, filename)) and filename.endswith(value):
                                        count = count + 1
                                        source = os.path.join(folder_to_track, filename)
                                        destination = os.path.join(folder_path, filename)
                                        moveIncrementing(source, destination) # move all files containing sub_file_name in their filenames
                                        movedFiles = True

                    end_time = time.monotonic()

                    if movedFiles:
                        if count == 1:
                            return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                        else:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                    else:
                        return "Couldn't move files"

                except Exception as e:
                    return f'{folder_to_track}: is either empty or not organizable'
    
    else:
        return f'{folder_to_track}: is either empty or not organizable'


#Group 2: Organize files based on name
def name_category(folder_to_track):
    movedFiles = False
    count = 0
    start_time = time.monotonic()
    file_mappings = collections.defaultdict()
    delimiters = ['.', ',', '!', ' ', '-', ';', '?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '/', '|', '<', '>']
    sub_file_names = [] 
    file_names = [] 
    regexPattern = '|'.join(map(re.escape, delimiters))

    for filename in os.listdir(folder_to_track):
        filename = filename.lower()
        file_names.append(filename)
        sub_file_names = find_common_keyword(file_names)

    if check_files(folder_to_track):
        for file in os.listdir(folder_to_track):
            if not os.path.isdir(os.path.join(folder_to_track, file)):
                try:
                    for filename in os.listdir(folder_to_track):
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            for sub_file_name in sub_file_names:
                                file_mappings.setdefault(sub_file_name, []).append(filename)

                    for folder_name, folder_items in file_mappings.items():
                        folder_path = os.path.join(folder_to_track, folder_name)
                        folder_exists = os.path.exists(folder_path)
                        if not folder_exists:
                            os.mkdir(folder_path)

                            for filename in file_names:
                                filename = filename.lower()
                                splittedstring = re.split(regexPattern, filename, 0)
                                if folder_name in splittedstring:
                                    count = count + 1
                                    source = os.path.join(folder_to_track, filename)
                                    destination = os.path.join(folder_path, filename)
                                    moveIncrementing(source, destination) 
                                    movedFiles = True

                        if folder_exists:
                            for filename in file_names:
                                filename = filename.lower()
                                splittedstring = re.split(regexPattern, filename, 0)
                                if folder_name in splittedstring and not os.path.isdir(os.path.join(folder_to_track, filename)):
                                    count = count + 1
                                    source = os.path.join(folder_to_track, filename)
                                    destination = os.path.join(folder_path, filename)
                                    moveIncrementing(source, destination)
                                    movedFiles = True

                    for filename in os.listdir(folder_to_track):
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            file_mappings.setdefault('other', []).append(filename) 

                    for folder_name, folder_items in file_mappings.items():
                        folder_path = os.path.join(folder_to_track, folder_name)
                        folder_exists = os.path.exists(folder_path)

                        if not folder_exists:
                            os.mkdir(folder_path)

                            for filename in os.listdir(folder_to_track):
                                filename = filename.lower()
                                if not os.path.isdir(os.path.join(folder_to_track, filename)):
                                    count = count + 1
                                    source = os.path.join(folder_to_track, filename)
                                    destination = os.path.join(folder_path, filename)
                                    moveIncrementing(source, destination)
                                    movedFiles = True
                            
                    end_time = time.monotonic()

                    if movedFiles:
                        if count == 1:
                            return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                        else:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                    else:
                        return "Couldn't move files"

                except Exception as e:
                    print(e)
                    return f'{folder_to_track}: is either empty or not organizable'
    else:
        return f'{folder_to_track}: is either empty or not organizable'

def specific_name_category(keyword, folder_to_track):
    start_time = time.monotonic()
    movedFiles = False
    count = 0
    file_mappings = collections.defaultdict()
    file_names = []
    keyword = keyword.lower()
    delimiters = ['.', ',', '!', ' ', '-', ';', '?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '/', '|', '<', '>']
    regexPattern = '|'.join(map(re.escape, delimiters))

    if check_files(folder_to_track):
        for file in os.listdir(folder_to_track):
            if not os.path.isdir(os.path.join(folder_to_track, file)):
                try:
                    for filename in os.listdir(folder_to_track):
                        filename = filename.lower()
                        file_names.append(filename)

                    for filename in os.listdir(folder_to_track):
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            file_mappings.setdefault(keyword, []).append(filename)

                    for folder_name, folder_items in file_mappings.items():
                        folder_path = os.path.join(folder_to_track, folder_name)
                        folder_exists = os.path.exists(folder_path)
                        if not folder_exists:
                            os.mkdir(folder_path)

                            for filename in file_names:
                                filename = filename.lower()
                                splittedstring = re.split(regexPattern, filename, 0)
                                if folder_name in splittedstring:
                                    count = count + 1
                                    source = os.path.join(folder_to_track, filename)
                                    destination = os.path.join(folder_path, filename)
                                    moveIncrementing(source, destination) 
                                    movedFiles = True

                        if folder_exists:
                            for filename in file_names:
                                filename = filename.lower()
                                splittedstring = re.split(regexPattern, filename, 0)
                                if folder_name in splittedstring and not os.path.isdir(os.path.join(folder_to_track, filename)):
                                    count = count + 1
                                    source = os.path.join(folder_to_track, filename)
                                    destination = os.path.join(folder_path, filename)
                                    moveIncrementing(source, destination) 
                                    movedFiles = True

                    end_time = time.monotonic()

                    if movedFiles:
                        if count == 1:
                            return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                        else:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                    else:
                        return "Couldn't move files"

                except Exception as e:
                    return f'{folder_to_track}: is either empty or not organizable'
    else:
        return f'{folder_to_track}: is either empty or not organizable'

#Group 3: Organize files based on time
def year_category(folder_to_track):
    start_time = time.monotonic()
    movedFiles = False
    years = set()
    count = 1
    if check_files:
        try:
            for file in os.listdir(folder_to_track):
                if not os.path.isdir(os.path.join(folder_to_track, file)):
                    raw_time = os.path.getctime(os.path.join(folder_to_track, file))
                    year = time.ctime(raw_time)[-4:]
                    years.add(year)

            for year in years:
                folder_path = os.path.join(folder_to_track, year)
                folder_exists = os.path.exists(folder_path)
                folder_name = year

                if not folder_exists:
                    os.mkdir(folder_path)

                    for filename in os.listdir(folder_to_track):
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            file_raw_time = os.path.getctime(os.path.join(folder_to_track, filename))
                            file_year = time.ctime(file_raw_time)[-4:]
                            if folder_name == file_year:
                                count = count + 1
                                source = os.path.join(folder_to_track, filename)
                                destination = os.path.join(folder_path, filename)
                                moveIncrementing(source, destination) 
                                movedFiles = True

                if folder_exists:

                    for filename in os.listdir(folder_to_track):
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            file_raw_time = os.path.getctime(os.path.join(folder_to_track, filename))
                            file_year = time.ctime(file_raw_time)[-4:]
                            if folder_name == file_year:
                                count = count + 1
                                source = os.path.join(folder_to_track, filename)
                                destination = os.path.join(folder_path, filename)
                                moveIncrementing(source, destination) 
                                movedFiles = True

            end_time = time.monotonic()

            if movedFiles:
                if count == 1:
                    return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                else:
                    return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
            else:
                return "Couldn't move files"

        except Exception as e:
            return f'{folder_to_track}: is either empty or not organizable'
    else:
        return f'{folder_to_track}: is either empty or not organizable'


def month_year_category(folder_to_track):
    years = set()
    months = set()
    if check_files:
        
            for file in os.listdir(folder_to_track):
                if not os.path.isdir(os.path.join(folder_to_track, file)):
                    raw_time = os.path.getctime(os.path.join(folder_to_track, file))
                    year = time.ctime(raw_time)[-4:]
                    years.add(year)

            for year in years:
                folder_path = os.path.join(folder_to_track, year)
                folder_exists = os.path.exists(folder_path)
                folder_name = year

                if not folder_exists:
                    os.mkdir(folder_path)

                    for filename in os.listdir(folder_to_track):
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            file_raw_time = os.path.getctime(os.path.join(folder_to_track, filename))
                            file_year = time.ctime(file_raw_time)[-4:]
                            if folder_name == file_year:
                                source = os.path.join(folder_to_track, filename)
                                destination = os.path.join(folder_path, filename)
                                moveIncrementing(source, destination) 

                if folder_exists:

                    for filename in os.listdir(folder_to_track):
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            file_raw_time = os.path.getctime(os.path.join(folder_to_track, filename))
                            file_year = time.ctime(file_raw_time)[-4:]
                            if folder_name == file_year:
                                source = os.path.join(folder_to_track, filename)
                                destination = os.path.join(folder_path, filename)
                                moveIncrementing(source, destination) 
                                
            for filename in os.listdir(folder_to_track):
                if os.path.isdir(os.path.join(folder_to_track, filename)):
                    for file in os.listdir(os.path.join(folder_to_track, filename)):
                        raw_time = os.path.getctime(os.path.join(folder_to_track, filename, file))
                        month = time.ctime(raw_time).split(' ')[1]
                        months.add(month)

                        folder_path = os.path.join(folder_to_track, filename, month)
                        folder_exists = os.path.exists(folder_path)
                        folder_name = month

                        if not folder_exists:
                            os.mkdir(folder_path)
                            
    else:
        return "Could not move files"