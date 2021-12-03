from src.jobs import read


def get_unique_job_types(path):
    # """Checks all different job types and returns a list of them

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # list
    #     List of unique job types
    # """
    # return []
    data_jobs = read(path)
    unique_job_types = set()
    for job in data_jobs:
        if job['job_type'] != '' and job['job_type'] not in unique_job_types:
            unique_job_types.add(job['job_type'])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    # """Filters a list of jobs by job_type

    # Parameters
    # ----------
    # jobs : list
    #     List of jobs to be filtered
    # job_type : str
    #     Job type for the list filter

    # Returns
    # -------
    # list
    #     List of jobs with provided job_type
    # """
    # return []
    data_job_types = []
    for job in jobs:
        if job["job_type"] == job_type:
            data_job_types.append(job)
    return data_job_types


def get_unique_industries(path):
    # """Checks all different industries and returns a list of them

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # list
    #     List of unique industries
    # """
    # return []
    data_jobs = read(path)
    unique_industries = set()
    for industry in data_jobs:
        if industry['industry'] != '' and \
          industry['industry'] not in unique_industries:
            unique_industries.add(industry['industry'])
    return unique_industries


def filter_by_industry(jobs, industry):
    # """Filters a list of jobs by industry

    # Parameters
    # ----------
    # jobs : list
    #     List of jobs to be filtered
    # industry : str
    #     Industry for the list filter

    # Returns
    # -------
    # list
    #     List of jobs with provided industry
    # """
    # return []
    data_filtered_industries = []
    for job in jobs:
        if job["industry"] == industry:
            data_filtered_industries.append(job)
    return data_filtered_industries


def get_max_salary(path):
    # """Get the maximum salary of all jobs

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # int
    #     The maximum salary paid out of all job opportunities
    # """
    # pass
    data_jobs = read(path)
    max_salary = []
    for salary in data_jobs:
        if salary['max_salary'] != '' and \
          salary['max_salary'] != 'invalid':
            max_salary.append(int(salary['max_salary']))
    return max(max_salary)


def get_min_salary(path):
    # """Get the minimum salary of all jobs

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # int
    #     The minimum salary paid out of all job opportunities
    # """
    # pass
    data_jobs = read(path)
    min_salary = []
    for salary in data_jobs:
        if salary['min_salary'] != '' and \
          salary['min_salary'] != 'invalid':
            min_salary.append(int(salary['min_salary']))
    return min(min_salary)


def matches_salary_range(job, salary):
    # """Checks if a given salary is in the salary range of a given job

    # Parameters
    # ----------
    # job : dict
    #     The job with `min_salary` and `max_salary` keys
    # salary : int
    #     The salary to check if matches with salary range of the job

    # Returns
    # -------
    # bool
    #     True if the salary is in the salary range of the job, False otherwise

    # Raises
    # ------
    # ValueError
    #     If `job["min_salary"]` or `job["max_salary"]` doesn't exists
    #     If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
    #     If `job["min_salary"]` is greather than `job["max_salary"]`
    #     If `salary` isn't a valid integer
    # """
    # pass
    if (("min_salary" or "max_salary")) not in job:
        raise ValueError
    if ((type(job["min_salary"]) != int) or (type(job["max_salary"]) != int)):
        raise ValueError
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError
    if (type(salary) != int):
        raise ValueError
    return (job["min_salary"] <= salary <= job["max_salary"])


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
