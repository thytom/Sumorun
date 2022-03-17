from genericpath import exists, isfile
from . import args
from . import io_utils
from . import iterator
from . import summary
from . import schemeparser
from . import xml_injector

summary_dir = "./out"

def main():
    arguments = args.compile_args()

    if arguments.create_schemefile:
        schemeparser.create_schemefile()
        exit(0)

    scheme = schemeparser.read_schemefile(arguments.schemefile_location)
    
    iterations = scheme['iterations']
    config_file = scheme['files']['sumo_configuration']
    attributes = scheme['attributes']
    aggressive_clean = scheme['aggressive_clean']
    
    print("Performing vtype injection...")
    xml_injector.xml_inject_route_file(scheme)


    print("Performing {} iterations using configuration file {}..."
        .format(iterations, config_file))

    io_utils.prepare_output_dir(aggressive_clean, summary_dir)
    summaries = iterator.iterate(config_file, summary_dir, iterations)
    summary.print_summaries(summaries, attributes)

    exit(0)

if __name__ == '__main__':
    main()