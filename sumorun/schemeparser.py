import yaml
import sys

default_schemefile = """
files:
    sumo_configuration: "simulation.sumocfg"
    routes_file: "routes.rou.xml"
iterations: 5
attributes: ["arrived"]
aggressive_clean: true
vtypes:
    - 
        id: "HUMAN_DRIVER"
        minGap: "2.00"
        speedFactor: "normc(1.00,0.10,0.40,5.00)"
        impatience: "5.00"
        carFollowModel: "EIDM"
        accel: "0.73"
        decel: "1.67"
        delta: "4"
        penetration: "0.6"
    -
        id: "AUTONOMOUS_DRIVER"
        minGap: "1.00"
        speedFactor: "normc(1.00,0.10,0.40,1.00)"
        impatience: "3.00"
        carFollowModel: "EIDM"
        accel: "0.73"
        decel: "1.67"
        delta: "4"
        penetration: "0.3"
route_cars_per_hour:
    default: "1600"
    # Use this array to specify override values for routes specific to your network. 
    override: { }
"""

def create_schemefile():
    print("Writing default schemefile...")
    with open("./scheme.yaml", "w") as f:
        f.writelines(default_schemefile)
        f.close()
    print("Done.")
    
def read_schemefile(file_location):
    try:
        with open(file_location, "r") as schemefile:
            scheme = yaml.safe_load(schemefile)
            return scheme
    except FileNotFoundError:
        print("Could not find {}.".format(file_location), file=sys.stderr)
        exit(1)
    except yaml.YAMLError as e:
        print(e)
        exit(1)
