import os
import collections
import re
from extensions import *
from Secondary_functions import *

def all_extensions_category(folder_to_track):
    if check_files(folder_to_track) == True:
        for file in os.listdir(folder_to_track):
            if os.path.isdir(os.path.join(folder_to_track, file)) == False and os.listdir(folder_to_track).__len__() != 0:
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
                            os.rename(source, destination)                    
                            
                    return "Successfully organized files based on extension"
                            
                except Exception as e:
                    return f'{folder_to_track}: is either empty or not organizable'
    
    else:
        return f'{folder_to_track}: is either empty or not organizable'

all_extensions_category("D:\\Test")

def name_category(folder_to_track):
    file_mappings = collections.defaultdict()
    sub_file_names = []
    file_names = []
    delimiters = ['.', ',', '!', ' ', '-', ';', '?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '/', '|', '<', '>']
    for file in os.listdir(folder_to_track):
        if os.path.isdir(os.path.join(folder_to_track, file)) == False and os.listdir(folder_to_track).__len__() != 0:
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
                                
                return "Successfully organized files based on name"

            except Exception as e:
                return f'{folder_to_track}: is either empty or not organizable'
    else:
        return f'{folder_to_track}: is either empty or not organizable'

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