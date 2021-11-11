from subprocess import run
from multiprocessing import Pool
import os, sys, json


scene_folder = 'SF_100'
model_list = os.listdir(scene_folder)

NUM_OF_PROCESS = 4

def run_eplus(model_list):

	for bldg_id in model_list:
	    bldg_id = str(bldg_id)
	    model_name = 'model-1'
	    model_id = '1'
	    work_folder = os.path.join(scene_folder, bldg_id)

	    epw_name = os.path.join('SF_WU_R435S_17.epw')

	    if os.path.isdir(work_folder):
            run(['python', 'run_eplus.py', model_name, work_folder, epw_name, model_id])
	    else:
	    	raise Exception('Error: ' + work_folder + ' is not a directory')

if __name__ == '__main__':
	run_set = list()
	total_size = len(model_list)
	thread_size = int(total_size / NUM_OF_PROCESS) + 1

	end_num = 0
	for set_num in range(NUM_OF_PROCESS - 1):
	    start_num = set_num * thread_size
	    end_num = (set_num + 1) * thread_size
	    run_set.append(model_list[start_num: end_num])
	    
	run_set.append(model_list[end_num: ])

	pool = Pool(NUM_OF_PROCESS) 
	results = pool.map(run_eplus, run_set)

	pool.close() 
	pool.join()

