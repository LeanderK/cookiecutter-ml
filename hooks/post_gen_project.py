import re
import sys
import fileinput
import os
from datetime import datetime

organize_experiments_folder_by = '{{ cookiecutter.organize_experiments_folder_by }}'

#experiments folder organization
if organize_experiments_folder_by is "dataset":
    input_string = input("Enter your datasets separated by comma: ")
    datasets  = list(filter(lambda str: len(str) != 0,[inp.strip() for inp in input_string.split(",")]))
    escaped_ds = ["`" + ds + "`" for ds in datasets]
    if len(datasets) == 1:
        datasets_readme = "`" + escaped_ds[0] + "`"
    else:
        datasets_readme = ",".join(escaped_ds[:-1])
        datasets_readme = datasets_readme + " or " + escaped_ds[-1]
    
    # Read in the file
    with open('Readme_exp_dataset.md', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('DATASETS', datasets_readme)

    # Write the file out again
    with open('Readme_exp_dataset.md', 'w') as file:
        file.write(filedata)
    
    for incorrect_readme in ['Readme_exp_date.md', 'Readme.md']:
        os.remove(incorrect_readme)

    os.rename('Readme_exp_dataset.md', 'Readme.md')
    os.remove('experiments/.gitkeep')

    for ds in datasets:
        ds_dir = 'experiments/' + ds
        os.mkdir(ds_dir)
        open(ds_dir + '/.gitkeep', 'a').close()
elif organize_experiments_folder_by is "date":
    incorret_inp = True
    organize_by_week = True
    while incorret_inp:
        input_string = input("Do you want to organize your experiments by week of by month [week, month]: ")
        if input_string.strip() == "month":
            organize_by_week = False
            incorret_inp = False
        elif input_string.strip() == "week":
            organize_by_week = True
            incorret_inp = False
    
    if organize_by_week:
        readme_resolution = "week"
    else:
        readme_resolution = "month"
    
    start = datetime.now().strftime('%Y-%m-%d')

    # Read in the file
    with open('Readme_exp_date.md', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('RESOLUTION', readme_resolution)
    filedata = filedata.replace('START', start)

    # Write the file out again
    with open('Readme_exp_date.md', 'w') as file:
        file.write(filedata)
    
    for incorrect_readme in ['Readme_exp_dataset.md', 'Readme.md']:
        os.remove(incorrect_readme)

    os.rename('Readme_exp_date.md', 'Readme.md')
    os.remove('experiments/.gitkeep')

    date_dir = 'experiments/' + readme_resolution + "_1"
    os.mkdir(date_dir)
    open(date_dir + '/.gitkeep', 'a').close()
else:
    for incorrect_readme in ['Readme_exp_date.md', 'Readme_exp_dataset.md']:
        os.remove(incorrect_readme)

use_tensorboard = '{{ cookiecutter.do_you_use_tensorboard }}'

if use_tensorboard == "no":
    os.remove('experiments/tensorboard/.gitkeep')
    os.rmdir('experiments/tensorboard')