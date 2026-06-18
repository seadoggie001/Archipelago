import dataclasses

from .Resources import Resources


class CropNames:
    Hay = "Hay"
    Bush = "Bush"
    Tree = "Tree"
    Carrot = "Carrot"
    Pumpkin = "Pumpkin"
    Sunflower = "Sunflower"
    Cactus = "Cactus"
    Dinosaur = "Dinosaur"

@dataclasses.dataclass
class Crops:
    name: str
    '''Name of the crop'''
    cost: list[str]
    '''The cost to plant'''
    result: str | None
    '''The result of harvesting the crop'''
    starting_crop: bool = False
    '''Should the costs for this not be randomized?'''
    
ALL_CROPS = [
    Crops(CropNames.Hay, [], Resources.Hay, True),
    Crops(CropNames.Bush, [], Resources.Wood, True),
    Crops(CropNames.Tree, [], Resources.Wood),
    Crops(CropNames.Carrot, [Resources.Wood, Resources.Hay], Resources.Carrot),
    Crops(CropNames.Pumpkin, [Resources.Carrot], Resources.Pumpkin),
    Crops(CropNames.Sunflower, [Resources.Carrot], None),
    # Sunflowers produce nothing... not enough power gets produced
    Crops(CropNames.Cactus, [Resources.Pumpkin], Resources.Cactus),
    Crops(CropNames.Dinosaur, [Resources.Cactus], Resources.Bone),
]