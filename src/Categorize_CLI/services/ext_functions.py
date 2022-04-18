import os
import collections
from src.Categorize_CLI.extensions import *
from src.Categorize_CLI.secondary_functions import *
import time
from datetime import timedelta


# Group 1: Organize files based on extension
def all_extensions_category(folder_to_track):
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
                                count = count + 1
                                size = size + os.path.getsize(source)
                                moveIncrementing(source, destination)
                                movedFiles = True

                        if folder_exists:
                            for folder_item in folder_items:
                                source = os.path.join(folder_to_track, folder_item)
                                destination = os.path.join(folder_path, folder_item)
                                count = count + 1
                                size = size + os.path.getsize(source)
                                moveIncrementing(source, destination)
                                movedFiles = True

                    end_time = time.monotonic()

                    displayProgressbar(count)

                    size = int(size/1000000)

                    if len(str(size)) == 4:
                        size = str(int(size/1000)) + " GB"
                    else:
                        size = str(size) + " MB"

                    if movedFiles:
                        if count == 1:
                            return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}{os.linesep}Total size of files moved: {size}"
                        else:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}{os.linesep}Total size of files moved: {size}"
                    else:
                        return "Files with that extension do not exist in {}".format(folder_to_track)

                except Exception as e:
                    print(e)
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
                            if not os.path.isdir(os.path.join(folder_to_track, filename)) and any(
                                    filename.endswith(value) for filename in os.listdir(folder_to_track)) == True:
                                file_mappings.setdefault(get_key(extension), []).append(filename)

                    for folder_name, folder_items in file_mappings.items():
                        folder_path = os.path.join(folder_to_track, folder_name)
                        folder_exists = os.path.exists(folder_path)
                        if not folder_exists:
                            os.mkdir(folder_path)

                            for filename in os.listdir(folder_to_track):
                                for value in extension:
                                    if not os.path.isdir(os.path.join(folder_to_track, filename)) and filename.endswith(
                                            value):
                                        count = count + 1
                                        source = os.path.join(folder_to_track, filename)
                                        destination = os.path.join(folder_path, filename)
                                        moveIncrementing(source,destination)  # move all files containing sub_file_name in their filenames
                                        movedFiles = True

                        if folder_exists:
                            for filename in os.listdir(folder_to_track):
                                for value in extension:
                                    if not os.path.isdir(os.path.join(folder_to_track, filename)) and filename.endswith(
                                            value):
                                        count = count + 1
                                        source = os.path.join(folder_to_track, filename)
                                        destination = os.path.join(folder_path, filename)
                                        moveIncrementing(source,
                                                         destination)  # move all files containing sub_file_name in their filenames
                                        movedFiles = True

                    end_time = time.monotonic()

                    displayProgressbar(count)

                    if movedFiles:
                        if count == 1:
                            return f"Successfully moved {count} file{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                        else:
                            return f"Successfully moved {count} files{os.linesep}Time taken: {timedelta(seconds=end_time - start_time)}"
                    else:
                        return "Files with that extension do not exist in {}".format(folder_to_track)

                except Exception as e:
                    print(e)
                    return f'{folder_to_track}: is either empty or not organizable'

    else:
        return f'{folder_to_track}: is either empty or not organizable'


def safe(folder_to_track):
    return extension_category(media, folder_to_track)