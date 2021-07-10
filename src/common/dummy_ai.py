import random
from time import sleep
from typing import TypedDict

IScoredSymbol = TypedDict(
    "IScoredSymbol",
    {
        "id": str,
        "score": float,
    },
)


def getCompanyAttractiveness(companySymbol: str) -> IScoredSymbol:
    """Calculate company attractiveness using a complex algorithm

    Args:
        companySymbol (str): Company symbol

    Returns:
        IScoredSymbol: Dict object containing the company symbol and its score
    """
    sleep(1)
    #print( {"id": companySymbol, "score": round(random.uniform(0, 1), 2)})
    
    return( {"id": companySymbol, "score": round(random.uniform(0, 1), 2)})
