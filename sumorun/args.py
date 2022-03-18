import argparse

def compile_args():
    """Argument parser."""
    parser = argparse.ArgumentParser(description="Automated run script for SUMO configurations.")
#    parser.add_argument('-c', '--config', dest="config_file", help="The configuration file to use.", required=True)
#    parser.add_argument('-n', '--number', dest="iterations", help="The number of iterations to perform", type=int, default=10)
#    parser.add_argument('--aggressive-clean', dest="aggressive_clean", help="Force cleans the output directory.", action="store_const", const=True, default=False)
#    parser.add_argument('--summary-items', dest="summary_items", help="A comma-separated list of summary items to show.", default="arrived")
    parser.add_argument('-s', '--scheme'
                            , dest="schemefile_location"
                            , help="The scheme file to use. (./scheme.yaml by default)"
                            , default="./scheme.yaml")
    parser.add_argument('--create-default-schemefile'
                        , dest="create_schemefile"
                        , help="Create a default schemefile in the current working directory."
                        , action="store_const"
                        , const=True
                        , default=False)
    parser.add_argument('-d', '--dry-run'
                        , dest="dry_run"
                        , help="Don't run SUMO, just set up the files as would be."
                        , action="store_const"
                        , const=True
                        , default=False)
    return parser.parse_args()