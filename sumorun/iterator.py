from os import system

def iterate(config_file:str, summary_dir: str, iterations:int):
    """This function performs the sumo iterations, using the configuration file provided."""
    summaries = []
    for i in range(0, iterations):
        summary_file = summary_dir + "/run_{}.xml".format(i)
        print("Performing iteration {}...".format(i))
        system("sumo --random --summary-output {} -c {}".format(summary_file, config_file))
        print("Output written to {}".format(summary_file))
        summaries.append(summary_file)
    return summaries