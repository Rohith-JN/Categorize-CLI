import os
import collections
import re
from extensions import *
from Secondary_functions import *
import time
from datetime import timedelta

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

def name_category(folder_to_track):
    movedFiles = False
    count = 0
    start_time = time.monotonic()
    file_mappings = collections.defaultdict()
    delimiters = ['.', ',', '!', ' ', '-', ';', '?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '/', '|', '<', '>']
    sub_file_names = [] # most frequent sub file names
    file_names = [] # all file names
    regexPattern = '|'.join(map(re.escape, delimiters))

    for filename in os.listdir(folder_to_track):
        filename = filename.lower()
        file_names.append(filename)
        sub_file_names = find_common_keyword(file_names)

    if check_files(folder_to_track): # check if folder not empty or not only contains folders
        for file in os.listdir(folder_to_track):
            if not os.path.isdir(os.path.join(folder_to_track, file)):
                try:
                    for filename in os.listdir(folder_to_track):
                        if not os.path.isdir(os.path.join(folder_to_track, filename)):
                            for sub_file_name in sub_file_names:
                                file_mappings.setdefault(sub_file_name, []).append(filename) # append sub_file_name and filename to file_mappings

                    for folder_name, folder_items in file_mappings.items():
                        folder_path = os.path.join(folder_to_track, folder_name)
                        folder_exists = os.path.exists(folder_path)
                        if not folder_exists: # if folder does not exist then make a folder with the sub_file_name
                            os.mkdir(folder_path)

                            for filename in file_names:
                                filename = filename.lower()
                                splittedstring = re.split(regexPattern, filename, 0)
                                if folder_name in splittedstring:
                                    count = count + 1
                                    source = os.path.join(folder_to_track, filename)
                                    destination = os.path.join(folder_path, filename)
                                    moveIncrementing(source, destination) # move all files containing sub_file_name in their filenames
                                    movedFiles = True

                        if folder_exists: # if folder already exists then move all files containing sub_file_name keyword to that folder
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
                            file_mappings.setdefault('other', []).append(filename) # append 'other' and filename to the mappings

                    for folder_name, folder_items in file_mappings.items():
                        folder_path = os.path.join(folder_to_track, folder_name)
                        folder_exists = os.path.exists(folder_path)

                        if not folder_exists: # if the 'other' folder does not exist then make that folder then add all items without the sub_file_name keyword into that folder
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

print(name_category("D:\\Test"))

def specific_name_category(keyword, folder_to_track):
    file_mappings = collections.defaultdict()
    file_names = []
    success = False
    keyword = keyword.lower()
    delimiters = ['.', ',', '!', ' ', '-', ';', '?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '/', '|', '<', '>']
    regexPattern = '|'.join(map(re.escape, delimiters))

    for file in os.listdir(folder_to_track):
        if os.path.isdir(os.path.join(folder_to_track, file)) == False and os.listdir(folder_to_track).__len__() != 0:
            try:
                for filename in os.listdir(folder_to_track):
                    filename = filename.lower()
                    file_names.append(filename)

                for filename in os.listdir(folder_to_track):
                    if not os.path.isdir(os.path.join(folder_to_track, filename)) and keyword in re.split(regexPattern, filename, 0):
                        file_mappings.setdefault(keyword, []).append(filename)

                for folder_name, folder_items in file_mappings.items():
                    folder_path = os.path.join(folder_to_track, folder_name)
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)
                        
                        for filename in file_names:
                            filename = filename.lower()
                            i = 1
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
                                success = True
                if success:
                    return "Successfully organized files based on specified keyword"
                elif not success:
                    return "No file containing that keyword exists"

            except Exception as e:
                return f'{folder_to_track}: is either empty or not organizable'
    else:
        return f'{folder_to_track}: is either empty or not organizable'

def extension_category(extension, folder_to_track):
    success = False
    for file in os.listdir(folder_to_track):
        if os.path.isdir(os.path.join(folder_to_track, file)) == False and os.listdir(folder_to_track).__len__() != 0:
            try:
                file_mappings = collections.defaultdict()
                for filename in os.listdir(folder_to_track):
                    for value in extension:
                        if not os.path.isdir(os.path.join(folder_to_track, filename)) and any(filename.endswith(value) for filename in os.listdir(folder_to_track)) == True:
                            file_mappings.setdefault(get_key(extension), []).append(filename)

                for folder_name, folder_items in file_mappings.items():
                    folder_path = os.path.join(folder_to_track, folder_name)
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)

                    for filename in os.listdir(folder_to_track):
                        i = 1
                        for value in extension:
                            if not os.path.isdir(os.path.join(folder_to_track, filename)) and filename.endswith(value):
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
                                success = True

                    if success:
                        return "Successfully organized files based on specified extension"
                    elif not success:
                        return "No file with that extension exists"

            except Exception as e:
                return f'{folder_to_track}: is either empty or not organizable'
    
    else:
        return f'{folder_to_track}: is either empty or no file with that extension exists'