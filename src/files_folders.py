import os
import errno
import settings


def set_output_folder():
    """Concatenate two strings and add a '/' to form the output directory string

    Returns:
        string: output directory
    """
    directory = settings.results_folder + settings.data_type + '/'
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise Exception('Error related to creation of output directory, check permissions etc.')

    return directory