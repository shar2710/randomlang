import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    num_rows, num_cols = players.shape
    return [num_rows, num_cols]

