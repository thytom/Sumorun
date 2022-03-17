from genericpath import exists, isfile
import args
import io_utils
import iterator
import summary

summary_dir = "./out"

def main():
    arguments = args.compile_args()
    config_file = arguments.config_file
    iterations = arguments.iterations
    attributes = arguments.summary_items.split(',')

    print("Performing {} iterations using configuration file {}..."
        .format(iterations, config_file))

    io_utils.prepare_output_dir(arguments.aggressive_clean, summary_dir)
    summaries = iterator.iterate(config_file, summary_dir, iterations)
    summary.print_summaries(summaries, attributes)

    exit(0)

if __name__ == '__main__':
    main()