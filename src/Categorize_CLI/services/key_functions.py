import os
import collections
import re
import time
from datetime import timedelta
from colorama import init
from colorama import Fore

from src.Categorize_CLI.common.secondary_functions import *

init()

def specific_name_category(keyword, folder_to_track, verbose):
    start_time = time.monotonic()
    moved = {}
    movedList = []
    no_of_files_moved = 0
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
                                    moved[filename] = folder_name + '/' + filename
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
                                    moved[filename] = folder_name + '/' + filename
                                    moveIncrementing(source, destination)
                                    movedFiles = True

                    end_time = time.monotonic()

                    for key, value in moved.items():
                        no_of_files_moved = no_of_files_moved + 1
                        movedList.append(f"{no_of_files_moved}) {key} {Fore.GREEN} --> {Fore.WHITE} {value}")

                    output = '\n'.join(map(str, movedList))

                    if movedFiles:
                        displayProgressbar(count)
                        if count == 1 and verbose:
                            return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}{os.linesep}Total size of files moved: {calc_size(size)}{os.linesep}{os.linesep}Files Moved:{os.linesep}{output}{os.linesep}"
                        elif count != 1 and verbose:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}{os.linesep}Total size of files moved: {calc_size(size)}{os.linesep}{os.linesep}Files Moved:{os.linesep}{output}{os.linesep}"
                        elif count == 1 and not verbose:
                            return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}{os.linesep}Total size of files moved: {calc_size(size)}{os.linesep}"
                        elif count != 1 and not verbose:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}{os.linesep}Total size of files moved: {calc_size(size)}{os.linesep}"
                        else:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}{os.linesep}Total size of files moved: {calc_size(size)}{os.linesep}"

                    else:
                        return os.linesep + Fore.RED + f'Error: Could not organize {folder_to_track}' + os.linesep

                except Exception as e:
                    return os.linesep + Fore.RED + f'Error: Could not organize {folder_to_track}' + os.linesep

    elif os.listdir(folder_to_track).__len__() == 0:
        return os.linesep + Fore.RED + f'Error: {folder_to_track} is empty' + os.linesep
    elif all(os.path.isdir(os.path.join(folder_to_track, file + '//')) for file in os.listdir(folder_to_track)):
        return os.linesep + Fore.RED + f'Error: {folder_to_track} only contains folders' + os.linesep
    else: 
        return os.linesep + Fore.RED + f'Error: Could not organize {folder_to_track}' + os.linesep
