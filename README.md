# Surveying Bycatch Incidents: UAE Dugong Conservation

## Project Overview
This project focuses on assessing bycatch incidents involving dugongs in the UAE. It aims to gather data on bycatch occurrences, analyse their impacts on dugong populations, and provide recommendations for effective conservation and management strategies.

## Project Dependencies
- R:  statistical analysis and data visualisation.
- GIS Software:spatial analysis and mapping of bycatch incidents.

## How to Run the Project

To streamline the execution of analysis, create a master script. This script will automate the process by running all necessary scripts and commands in sequence when executed.

#1. Setting Up the Master Script:
   - Create an R script (e.g., `master_script.R`) that calls all the analysis scripts in the desired order.
   - Example structure of the master script:
     ```R
     source("data_preparation.R")
     source("statistical_analysis.R")
     source("visualization.R")
     ```
   - Ensure that each script is properly configured and tested.

#2. Run the Master Script:
   - Open R and execute the master script:
     ```R
     source("path/to/your/master_script.R")
     ```

#3. Use GIS Software and NVivo:
   - After running the master script, use GIS software for spatial analysis and mapping as required.
   - Open NVivo to conduct qualitative analysis on interview data.


## The data directory

Is where you will put all of your data. For bioinformatics projects, we won't want to store all of the raw data here becuase it would take up too much disk space. If you are using public sequencing data, add a text file of all of your accession ID's or data sources you used. Really, this directory is for storing the data you will make your analysis and plots from. They will usually be tabular files (`csv` or `tsv` or similar).

## The source directory

The `./src` directory is where you will put all your code. This should be anything from large scripts in python or R, to tiny BASH scripts where you are executing single commands. Put everything in here so you don't forget what you have done. Be sure to tell me (and your future self) what each of these code files do. Make **lots** of comments in your code please.

## .gitignore file

This file is useful if you want to keep files local on your machine, but want to ignore them when using `git`. For example, if you have very large sequencing files you use for analysis and want them on your laptop, but do not want to upload them to GitHub (GitHub has a single file size limit of 150Mb anyway).

## Getting started

To use this repository for your work, fork this repository. There's a button on the top right for 'forking' this repository. In doing so, you will have a copy of this repository in your personal account which you can then work on. After forking, `git clone` your copy of the repository and edit the README, add your data and code!



