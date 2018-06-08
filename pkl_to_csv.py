import functools
from pathlib import Path
import numpy as np
from qtlib.types import OpenFilesType
from tweezers import api as tz, get_option
import pandas as pd


def read_pkl(filePath: Path):
    print("reading...", filePath)
    name = str(filePath)[:-4]
    keys = ['time', 'dist', 'force', 'known_trace', 'path', 'fullpath', 'unit', 'info', 'trap_sep']
    tr = tz.trace(filePath)
    h = len(tr.dist) // 2
    df = pd.DataFrame(np.array([tr.time, tr.dist, tr.force]).T, columns=['time', 'dist', 'force'])
    df['unit'] = tr.unit
    df['experiment name'] = tr.path
    return df

def output_csv(filePath: Path):
    assert(filePath.is_dir())
    for x in filePath.iterdir():
        if x.is_file() and x.suffix == '.pkl':
            df = read_pkl(x)
            csv_name = str(filePath) + '/' + x.stem + '.csv'
            df.to_csv(csv_name)
            print("saving...", csv_name)

if __name__ == "__main__":
    import defopt
    defopt.run(output_csv)
