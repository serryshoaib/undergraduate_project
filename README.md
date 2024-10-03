# ARU undergraduate project template

This is a template to get you started for your projects. Below is a description of the template:

```text
-- undergraduate_template // this is the home directory for your project
  |
  -- README.md            // this file you are currently reading
  -- /data                // data directory to store your data
  -- /src                 // source code directory to put your code here
  -- .gitignore           // a list of files for git to ignore
```

## The README file

Is a file which renders nicely on GitHub and tells the user (and your future selves) what you did. Include details like:

- Title of your project (replace the "ARU undergraduate project template" at the top)
- What your project is about
- What your project depends on (e.g. python3, bioinformatic software etc.)
- How to run your project
  - I like to set up a 'master script' which will run everything when you execute that command
  - Some options include:
    - Running a python script (e.g. `python3 ./src/main.py`)
    - Running a BASH script (e.g. `bash ./src/main.bash`)
    - Telling the user which script to run when (a descriptive version of the pipeline)

## The data directory

Is where you will put all of your data. For bioinformatics projects, we won't want to store all of the raw data here becuase it would take up too much disk space. If you are using public sequencing data, add a text file of all of your accession ID's or data sources you used. Really, this directory is for storing the data you will make your analysis and plots from. They will usually be tabular files (`csv` or `tsv` or similar).

## The source directory

The `./src` directory is where you will put all your code. This should be anything from large scripts in python or R, to tiny BASH scripts where you are executing single commands. Put everything in here so you don't forget what you have done. Be sure to tell me (and your future self) what each of these code files do. Make **lots** of comments in your code please.

## .gitignore file

This file is useful if you want to keep files local on your machine, but want to ignore them when using `git`. For example, if you have very large sequencing files you use for analysis and want them on your laptop, but do not want to upload them to GitHub (GitHub has a single file size limit of 150Mb anyway).

## Getting started

To use this repository for your work, fork this repository. There's a button on the top right for 'forking' this repository. In doing so, you will have a copy of this repository in your personal account which you can then work on. After forking, `git clone` your copy of the repository and edit the README, add your data and code!
