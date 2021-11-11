import argparse
import os
import subprocess


# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

# Required positional argument

parser.add_argument('model_name', type=str,
                    help='Building EnergyPlus model name')

parser.add_argument('work_folder', type=str,
                    help='Building EnergyPlus work folder')

parser.add_argument('epw_name', type=str,
                    help='Weather file name')

parser.add_argument('model_id', type=str,
                    help='Result prefix')

args = parser.parse_args()

model_name = args.model_name
work_folder = args.work_folder

model_id = args.model_id
idf_name = os.path.join(work_folder, model_name + ".idf")
epw_name =  args.epw_name
print(work_folder, idf_name)


if os.path.isdir(work_folder) and os.path.exists(idf_name):
    subprocess.run(['./EnergyPlus-9-5-0/energyplus-9.5.0', '-w', epw_name, '-d', work_folder, idf_name])
    os.chdir(work_folder)
    subprocess.run(['cp', 'eplusout.csv', 'eplusout-' + model_id + '.csv'])
    