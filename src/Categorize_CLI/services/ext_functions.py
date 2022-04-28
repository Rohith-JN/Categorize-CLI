import os
import collections
import time
from datetime import timedelta
from colorama import init
from colorama import Fore

from src.Categorize_CLI.common.secondary_functions import *

init()

def all_extensions_category(folder_to_track, verbose):
    moved = {}
    movedList = []
    no_of_files_moved = 0
    size = 0
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
                                moved[folder_item] = folder_name + '/' + folder_item
                                count = count + 1
                                size = size + os.path.getsize(source)
                                moveIncrementing(source, destination)
                                movedFiles = True

                        if folder_exists:
                            for folder_item in folder_items:
                                source = os.path.join(folder_to_track, folder_item)
                                destination = os.path.join(folder_path, folder_item)
                                moved[folder_item] = folder_name + '/' + folder_item
                                count = count + 1
                                size = size + os.path.getsize(source)
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


def extension_category(extension, folder_to_track, verbose):
    start_time = time.monotonic()
    moved = {}
    movedList = []
    no_of_files_moved = 0
    size = 0
    movedFiles = False
    count = 0
    if check_files(folder_to_track):
        for file in os.listdir(folder_to_track):
            if not os.path.isdir(os.path.join(folder_to_track, file)):
                try:
                    file_mappings = collections.defaultdict()
                    for filename in os.listdir(folder_to_track):
                        for value in extension:
                            if not os.path.isdir(os.path.join(folder_to_track, filename)) and any(
                                    filename.endswith(value) for filename in os.listdir(folder_to_track)):
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
                                        size = size + os.path.getsize(source)
                                        destination = os.path.join(folder_path, filename)
                                        moved[filename] = folder_name + '/' + filename
                                        moveIncrementing(source,destination)
                                        movedFiles = True

                        if folder_exists:
                            for filename in os.listdir(folder_to_track):
                                for value in extension:
                                    if not os.path.isdir(os.path.join(folder_to_track, filename)) and filename.endswith(value):
                                        count = count + 1
                                        source = os.path.join(folder_to_track, filename)
                                        size = size + os.path.getsize(source)
                                        destination = os.path.join(folder_path, filename)
                                        moveIncrementing(source, destination)
                                        moved[filename] = folder_name + '/' + filename
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
                        return os.linesep + Fore.RED + f'Error: {folder_to_track} does not contain any {get_key(extension)} files' + os.linesep

                except Exception as e:
                    return os.linesep + Fore.RED + f'Error: {folder_to_track} does not contain any {get_key(extension)} files' + os.linesep

    elif os.listdir(folder_to_track).__len__() == 0:
        return os.linesep + Fore.RED + f'Error: {folder_to_track} is empty' + os.linesep
    elif all(os.path.isdir(os.path.join(folder_to_track, file + '//')) for file in os.listdir(folder_to_track)):
        return os.linesep + Fore.RED + f'Error: {folder_to_track} only contains folders' + os.linesep
    else: 
        return os.linesep + Fore.RED + f'Error: Could not organize {folder_to_track}' + os.linesep