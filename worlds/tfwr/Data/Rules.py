class RuleNames:
    """Custom rules to be manually resolved"""
    AnyHatItems = "AnyHatItems"
    """the player has any hats"""
    ReallyBigFarm = "Really Big Farm"
    """the player has all of the expansions"""
    CropsThatCanProduceWeirdSubstance = "Crops that can produce Weird Substance"
    """the player has a crop that produces multiple items"""
    Rules: list[str] = [AnyHatItems, ReallyBigFarm, CropsThatCanProduceWeirdSubstance]
