import subprocess
import os, sys, json


scene_folder = 'SF_100'
model_list = os.listdir(scene_folder)


# note: model_name and model_id (as result prefix should be modified between scenes)
def run_eplus(model_list):

	for bldg_id in model_list:
	    bldg_id = str(bldg_id)
	    model_name = 'model-wrf-2' ## todo
	    model_id = 'r2'  ## todo
	    work_folder = os.path.join(scene_folder, bldg_id)

	    epw_name = os.path.join('SF_WU_R435S_17.epw')

	    if os.path.isdir(work_folder):
	    	subprocess.run(['python3', 'run_eplus.py', model_name, work_folder, epw_name, model_id])
	    else:
	    	print('Error: ' + work_folder + ' is not a directory')
run_eplus(model_list)