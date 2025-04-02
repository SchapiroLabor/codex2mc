import pandas as pd


def extract(cycle_info,method="propagate"):
    '''
    two methods to select best channel: 

    propagate: selects the plane with highest contrast in the reference channel, i.e. nuclear marker (CH1), at each tile.
    then it selects the median plane index from all the tiles and it propagates this index across all other channels and tiles.
    per_channel: selects the plane with highest contrast for each channel and each tile.  Not recommended. 
    '''
    if method=="propagate":
        aux_df=cycle_info.loc[cycle_info["channel"]==1,["tile","plane","contrast_median"]]
        focused_plane=aux_df.loc[aux_df.groupby(["tile"])["contrast_median"].idxmax()]["plane"].median()
        cycle_info=cycle_info.loc[cycle_info["plane"]==int(focused_plane)]

    elif method=="per_channel":

        cycle_info=cycle_info.loc[cycle_info.groupby(["channel", "tile"])["contrast_median"].idxmax()]

    return cycle_info

