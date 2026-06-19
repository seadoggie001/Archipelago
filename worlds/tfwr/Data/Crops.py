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
    tier: int
    '''How many are you expected to obtain? 1=1B 2=100M 3=100K'''
    cost: list[str]
    '''The cost to plant'''
    result: str | None
    '''The result of harvesting the crop'''
    starting_crop: bool = False
    '''Should the costs for this not be randomized?'''
    used_for_cost: bool = True
    '''Can the results of this crop be used as a cost?'''
    randomized_cost: bool = True
    '''Should the costs be randomized?'''


ALL_CROPS = [
    Crops(CropNames.Hay, 1, [], Resources.Hay, starting_crop=True, randomized_cost=False),
    Crops(CropNames.Bush, 1, [], Resources.Wood, randomized_cost=False),
    Crops(CropNames.Tree, 1, [], Resources.Wood),
    Crops(CropNames.Carrot, 1, [Resources.Wood, Resources.Hay], Resources.Carrot),
    Crops(CropNames.Pumpkin, 2, [Resources.Carrot], Resources.Pumpkin),
    Crops(CropNames.Sunflower, 3, [Resources.Carrot], Resources.Power, used_for_cost=False),
    Crops(CropNames.Cactus, 3, [Resources.Pumpkin], Resources.Cactus),
    Crops(CropNames.Dinosaur, 2, [Resources.Cactus], Resources.Bone),
]
