import dataclasses
import os
import sys

import json
from worlds.tfwr.Data.Location import ALL_LOCATION_DATA, Requirement
from worlds.tfwr.Data.Item import ALL_ITEM_DATA
from worlds.tfwr.Data.Region import ALL_REGION_DATA


# I copied this class from a stackoverflow answer about how to easily export dataclasses to json
class DataclassWithoutNoneJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dict((key, value) for key, value in o.__dict__.items() if value)
        return super().default(o)


def dump_data(data, filename: str) -> None:
    filepath = os.path.join(folder_path, filename)
    with open(filepath, "w") as file:
        json.dump(data, file, indent=2, cls=DataclassWithoutNoneJSONEncoder)
    print("Created: ", filepath)


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python worlds/tfwr/Data/exportJson.py")
        exit()

    print("Generating JSON output. . .")
    folder_path = os.path.join("worlds", "tfwr", "Data")

    for location in ALL_LOCATION_DATA:
        if location.requirements is None: continue
        requirements: list[Requirement] = []
        while len(location.requirements) > 0:
            req = location.requirements.pop()
            if isinstance(req, str):
                req = Requirement(req, 1)
            requirements.append(req)
        location.requirements = requirements

    dump_data(ALL_LOCATION_DATA, "locations.json")
    dump_data(ALL_REGION_DATA, "regions.json")
    dump_data(ALL_ITEM_DATA, "items.json")
