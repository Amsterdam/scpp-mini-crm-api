from adapters.amsterdam import schools, tags


def run_jobs():
    """
    Run the adapters to get data from remote sources.
    """
    schools.run()
    tags.run()
    

if __name__ == "__main__":
    """
    Placeholder so the jobs script can also be ran from a command line, for cronjobs
    """
    run_jobs()    
