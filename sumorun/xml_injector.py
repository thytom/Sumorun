import xml.etree.ElementTree as ET
from.xml_utils import (load_xml_file
                        , write_xml_file
                        , filter_tags_from_xml_tree
                        , add_elem_to_tree_root)

def xml_inject_route_file(scheme:dict):
    file_location = scheme['files']['routes_file']
    tree = load_xml_file(file_location)
    inject_vtypes_and_flows(tree, scheme)
    write_xml_file(tree, file_location)

def inject_vtypes_and_flows(tree: ET.Element, scheme:dict) -> ET.ElementTree:
    filter_tags_from_xml_tree(tree, "vType") 
    filter_tags_from_xml_tree(tree, "flow") 

    vtypes = scheme['vtypes']
    xml_vtypes = []
    for vtype in vtypes:
        xml_vtype = ET.Element("vType")
        xml_vtype.set("id", vtype['id'])
        xml_vtype.set("minGap", vtype['minGap'])
        xml_vtype.set("speedFactor", vtype['speedFactor'])
        xml_vtype.set("impatience", vtype['impatience'])
        xml_vtype.set("carFollowModel", vtype['carFollowModel'])
        xml_vtype.set("accel", vtype['accel'])
        xml_vtype.set("decel", vtype['decel'])
        xml_vtype.set("delta", vtype['delta'])
        
        xml_vtypes.append(xml_vtype)
        
    xml_flows = []
    for route in tree.findall("route"):
        for xml_vtype in xml_vtypes:
            xml_vtype_penetration = float([vt['penetration'] for vt in scheme['vtypes'] if vt['id'] == xml_vtype.get('id')][0])
            route_cph = scheme['route_cars_per_hour']['override'][route.get('id')]
            if route_cph is None:
                route_cph = scheme['route_cars_per_hour']['default']
            vph = int(xml_vtype_penetration * float(route_cph))
            xml_flow = ET.Element("flow",
            attrib={
                "id": route.get('id') + xml_vtype.get('id'),
                "type": xml_vtype.get('id'),
                "begin": "0.00",
                "end": "3600.00",
                "departSpeed": "max",
                "arrivalLane": "random",
                "route": route.get('id'),
                "vehsPerHour" : str(vph),
            })
            xml_flows.append(xml_flow)

    # Vehicle types must be added before.
    for xml_vtype in xml_vtypes:
        add_elem_to_tree_root(tree, xml_vtype)

    for xml_flow in xml_flows:
        add_elem_to_tree_root(tree, xml_flow)
    
    return tree