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
    sub_file_names = []
    file_names = []
    delimiters = ['.', ',', '!', ' ', '-', ';', '?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '/', '|', '<', '>']
    try:
        for filename in os.listdir(folder_to_track):
            filename = filename.lower()
            file_names.append(filename)
            sub_file_names.append(max(re.findall(r'[A-Za-z]+',filename),key=len))
            sub_file_names = list(set(sub_file_names))
        file_mappings = collections.defaultdict()
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
        
    except Exception as e:
        print(e)

    