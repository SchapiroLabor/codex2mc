import tifffile as tifff
from pathlib import Path
import pandas as pd
#import os
import argparse


#---CLI-BLOCK---#
parser=argparse.ArgumentParser()

#Mandatory arguments

parser.add_argument('-i',
                    '--input',
                    required=True,
                    help='parent directory where  multi-image file (stack) is located'
                    )

parser.add_argument('-o',
                    '--output',
                    required=True,
                    help='directory where the images of the extracted channels will be saved'
                    )

parser.add_argument('-f',
                    '--file',
                    required=True,
                    help='path to csv file containing two columns: 1) index of the channels to be extracted (0-based index) and 2) channel name '
                    )

args=parser.parse_args()

#---END_CLI-BLOCK---#
stack_path=Path(args.input)
chann_list=pd.read_csv(Path(args.file),sep=";")
output_dir=Path(args.output)

#img=list(filter( lambda x: x.endswith('.tif'), os.listdir(work_dir) ) )[0]

with tifff.TiffFile(stack_path) as tif:

    Path(output_dir).mkdir(parents=False, exist_ok=True)

    for index,name in zip( chann_list['index'].values , chann_list['ch_name'].values ):

        tifff.imwrite(output_dir/'{ch_name}.tif'.format(ch_name=name)  ,tif.pages[index].asarray(),photometric='minisblack')

print("channel extraction completed")
