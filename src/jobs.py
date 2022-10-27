from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    import csv

    with open(path) as jobs_file:
        jobs = []
        jobs_dict = csv.DictReader(jobs_file)
        for job in jobs_dict:
            jobs.append(job)
    return jobs
