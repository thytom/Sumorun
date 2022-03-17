import os
from genericpath import exists, isfile

def prepare_output_dir(aggressive_clean, summary_dir):
    """Prepares the output directory for data to be sent to."""
    if exists(summary_dir) and len(os.listdir(summary_dir)) != 0:
        if aggressive_clean:
            print("Performing clean of output directory...")
            for file in os.listdir(summary_dir):
                if isfile(summary_dir + "/" + file):
                    os.remove("{}/{}".format(summary_dir,file))
                    print("Deleted {}".format(file))
        else:
            print("Error. Output directory is not empty. Use --aggressive-clean to clean it.")
            exit(1)
    elif not exists(summary_dir):
        os.mkdir(summary_dir)