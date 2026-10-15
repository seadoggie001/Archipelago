import dataclasses
import os
import sys

import json

from worlds.tfwr.Data.Crops import Crops, ALL_CROPS
from worlds.tfwr.Data.Location import ALL_LOCATION_DATA, Requirement, LocationData
from worlds.tfwr.Data.Item import ALL_ITEM_DATA, ItemData
from worlds.tfwr.Data.Region import ALL_REGION_DATA, RegionData


# I copied this class from a stackoverflow answer about how to easily export dataclasses to json
class DataclassWithoutNoneJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dict((key, value) for key, value in o.__dict__.items() if value)
        return super().default(o)


def dump_data(data, filename: str) -> None:
    filepath = os.path.join(folder_path, filename)
    with open(filepath, "w") as file:
        json.dump(data, file, cls=DataclassWithoutNoneJSONEncoder)
    print("Created: ", filepath)


def normalize_requirements(things: list[LocationData | RegionData]) -> list[LocationData | RegionData]:
    for thing in things:
        if thing.requirements is None: continue
        requirements: list[Requirement] = []
        while len(thing.requirements) > 0:
            req = thing.requirements.pop()
            if isinstance(req, str):
                req = Requirement(req, 1)
            requirements.append(req)
        thing.requirements = requirements
    return things


@dataclasses.dataclass
class Data:
    locations: list[LocationData]
    regions: list[RegionData]
    items: list[ItemData]
    crops: list[Crops]


if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: python worlds/tfwr/Data/exportJson.py")
        exit()

    print("Generating JSON output. . .")
    folder_path = os.path.join("worlds", "tfwr", "Data")

    data = Data(normalize_requirements(ALL_LOCATION_DATA), normalize_requirements(ALL_REGION_DATA), ALL_ITEM_DATA,
                ALL_CROPS)

    dump_data(data, "data.json")
