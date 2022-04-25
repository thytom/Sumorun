import xml.etree.ElementTree as ET

def summary_report_as_str(summaries, attribute):
    """Print the report on a specific attribute."""
    arrived_counts = []
    try:
        for file in summaries:
            tree = ET.parse(file)
            root = tree.getroot()
            # highestarrival = [round(float(c.attrib[attribute]), 3) for c in root if c.tag == "step"]
            # arrived_counts.append(max(highestarrival))
            arrived_counts.append(round(float(root[-1].attrib[attribute]),3))

        # return "{},{},{},{}".format(attribute, max(arrived_counts), min(arrived_counts), round(sum(arrived_counts)/len(arrived_counts), 3))
        return ','.join([str(a) for a in arrived_counts])
    except KeyError:
        print("Attribute '{}' does not exist.".format(attribute))

# def print_summaries(run_number, summaries, attributes):
#     """Print the reports on a list of attributes."""
#     eq = "".join(["=" for i in range(0, 20)])
#     print("{}REPORT{}".format(eq, eq))
#     for attribute in attributes:
#         print_summary_report(run_number, summaries, attribute)

def write_full_summary(run_data, attributes):
    with open("./out.csv", 'w') as out_file:
        out_file.write("run_number,attribute\n")
        for (i, summaries) in enumerate(run_data):
            for attribute in attributes:
                out_file.write("{},{},".format(i, attribute)+summary_report_as_str(summaries,attribute)+'\n')