import os
import time
from datetime import timedelta

from src.Categorize_CLI.common.secondary_functions import *

def year_category(folder_to_track):
    start_time = time.monotonic()
    size = 0
    movedFiles = False
    years = set()
    count = 0
    if check_files(folder_to_track):
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
                                size = size + os.path.getsize(source)
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
                return f'{folder_to_track}: is either empty or not organizable'

        except Exception as e:
            return f'{folder_to_track}: is either empty or not organizable'
    else:
        return f'{folder_to_track}: is either empty or not organizable'