import xml.etree.ElementTree as ET

def print_summary_report(summaries, attribute):
    """Print the report on a specific attribute."""
    arrived_counts = []
    try:
        for file in summaries:
            tree = ET.parse(file)
            root = tree.getroot()
            highestarrival = [round(float(c.attrib[attribute]), 3) for c in root if c.tag == "step"]
            arrived_counts.append(max(highestarrival))

        print("{: <16}: Best {: <8}  Worst {: <8}  AVG {: <8}"
            .format(attribute, max(arrived_counts), min(arrived_counts), round(sum(arrived_counts)/len(arrived_counts), 3)))
    except KeyError:
        print("Attribute '{}' does not exist.".format(attribute))

def print_summaries(summaries, attributes):
    """Print the reports on a list of attributes."""
    eq = "".join(["=" for i in range(0, 20)])
    print("{}REPORT{}".format(eq, eq))
    for attribute in attributes:
        print_summary_report(summaries, attribute)