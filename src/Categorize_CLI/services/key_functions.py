import os
import collections
import re
import time
from datetime import timedelta

from src.Categorize_CLI.common.secondary_functions import *


def specific_name_category(keyword, folder_to_track):
    start_time = time.monotonic()
    size = 0
    movedFiles = False
    count = 0
    file_mappings = collections.defaultdict()
    file_names = []
    keyword = keyword.lower()
    delimiters = ['.', ',', '!', ' ', '-', ';', '?', '*', '!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '/', '|','<', '>']
    regexPattern = '|'.join(map(re.escape, delimiters))

    if check_files(folder_to_track):
        for file in os.listdir(folder_to_track):
            if not os.path.isdir(os.path.join(folder_to_track, file)):
                try:
                    for filename in os.listdir(folder_to_track):
                        filename = filename.lower()
                        file_names.append(filename)

                    for filename in os.listdir(folder_to_track):
                        filename = filename.lower()
                        splittedstring = re.split(regexPattern, filename, 0)
                        if not os.path.isdir(os.path.join(folder_to_track, filename)) and keyword in splittedstring:
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
                                    size = size + os.path.getsize(source)
                                    destination = os.path.join(folder_path, filename)
                                    moveIncrementing(source, destination)
                                    movedFiles = True

                        if folder_exists:
                            for filename in file_names:
                                filename = filename.lower()
                                splittedstring = re.split(regexPattern, filename, 0)
                                if folder_name in splittedstring and not os.path.isdir(
                                        os.path.join(folder_to_track, filename)):
                                    count = count + 1
                                    source = os.path.join(folder_to_track, filename)
                                    size = size + os.path.getsize(source)
                                    destination = os.path.join(folder_path, filename)
                                    moveIncrementing(source, destination)
                                    movedFiles = True

                    end_time = time.monotonic()

                    displayProgressbar(count)

                    if movedFiles:
                        if count == 1:
                            return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}{os.linesep}Total size of files moved: {calc_size(size)}"
                        else:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}{os.linesep}Total size of files moved: {calc_size(size)}"
                    else:
                        return f"{folder_to_track}: is either empty or not organizable"

                except Exception as e:
                    return f'{folder_to_track}: is either empty or not organizable'
    else:
        return f'{folder_to_track}: is either empty or not organizable'