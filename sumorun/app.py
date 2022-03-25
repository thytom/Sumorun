from genericpath import exists, isfile
from re import I
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

    print("Looking for interval statements in vtype scheme...")

    interval_count = 0
    # Find the variable in vtypes to alter
    varray = None
    vtype_altering = None
    attrib_to_alter = None
    for vtype in scheme['vtypes']:
        for attrib in vtype:
            if isinstance(vtype.get(attrib), list):
                varray = vtype.get(attrib)
                vtype_altering = vtype.get('id')
                attrib_to_alter = attrib
                interval_count += 1
    
    if interval_count == 0:
        print("No intervals. Proceeding with single run...")
    elif interval_count > 1:
        print("Multiple intervals in schemefile, cannot continue.")
    else:
        print("Intervals found. Will run for every value and output data accordingly.")
    
    if arguments.dry_run:
        print("Dry run completed.")
        exit(0)

    run_data = []

    for (i, value) in enumerate(varray):
        out_dir = summary_dir + "_{}".format(i)

        for (j,vtype) in enumerate(scheme['vtypes']):
            if vtype.get('id') == vtype_altering:
                scheme['vtypes'][j][attrib_to_alter] = value

        print("Performing vtype injection...")
        xml_injector.xml_inject_route_file(scheme)

        print("Performing {} iterations using configuration file {}..."
            .format(iterations, config_file))
        
        io_utils.prepare_output_dir(aggressive_clean, out_dir)
        summaries = iterator.iterate(config_file, out_dir, iterations)
        run_data.append(summaries)

    summary.write_full_summary(run_data, attributes)

    exit(0)

if __name__ == '__main__':
    main()