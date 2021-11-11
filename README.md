# citybes-cityffd

## Data Hierachy

- `scene_json` is the folder to store static and runtime JSON files for data exchanges
- `SF_100` is the working folder to store and run EnergyPlus IDF models.
- `EnergyPlus-9-5-0` is copied directly from EnergyPlus installation folder.

## Generate "Red Node" static JSON file from CityBES input

1. District IDF files download from CityBES should be upgraded to E+ 9.4 and above, and saved in the hierachy as `district_work_folder/building_folder/model.idf` (e.g. `SF_100/bldg_3981157_1172/model.idf`). 

2. CityBES exported `x_shift` and `y_shift` information to translate the relative coordinates in IDF files to absolute coordinates should be saved in `scene_json/meta/cityffd_case_info.csv`. 

3. Running `0_write-scene` will generate the initial CityBES static JSON file (red nodes) in `scene_json/meta`.


## Generate static mapping file

1. Save the static "Blue Node" JSON file (e.g. `blue_nodes_97_new.json`) in the same folder with the red node (`scene_json/meta`).

2. Running `0_mapping` will generate the static mapping file in the same folder (e.g. `scene_json/meta/sf_dt_97_mapping.json`)


## Runtime co-simulation

1. For initialization round without CityFFD input, first run the "Write Baseline IDF" chunk of code `1_write-local-idf` to modify IDF files to change run period and add reportable varialbes required for heat emission reports.

2. Run "run.py" or "run_eplus_all.py" to run all EnergyPlus models. Modify the `model_name` and `model_id` (for result suffix) according to different iteration number. For example, if the IDF model name is "model-1.idf" for the initial iteration, and model ID is assigned as "1", the result for this round can be found in each building simulation folder as "eplusout-1.csv".

3. Save CityFFD runtime JSON files collected at each round in a separate folder under `scene-json` (e.g. `scene-json\2-cityffd-97` for the second round of the 97 building case). Run `scene-json\2-cityffd-97\fix.py` to fix JSON format and namings.

4. Run `2_write_json_file_to_csv` to parse JSON to EnergyPlus readable CSV schedules. Results are saved in `scene-json\run_time_inputs`.

5. For intermediate runs taking CityFFD input, we need to generate new IDFs to add local air nodes and link schedules to them. Running `3_write-local-idf` will read the static geometry and mapping file to help us find the mapping from IDF surface name to CityFFD cell ID, and the schedule file name and column number for this CityFFD cell. Please make sure to change the file and folder names accordingly for different rounds of iterations.

6. Run new local IDFs following step 2.

7. Run `4_write_csv_results_to_json` to parse and aggregation CSV results to generate run time red node JSON files. The results should be saved in a separate folder in `scene-json` (e.g. `scene-json\2-eplus` for the second round of the 97 building case).

