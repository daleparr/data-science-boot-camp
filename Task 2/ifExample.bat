@echo off
REM Check if 'new_folder' exists and create 'if_folder' if it does
if exist new_folder (
    mkdir if_folder
) 

REM Check if 'if_folder' exists and create 'hyperionDev'; otherwise, create 'new-projects'
if exist if_folder (
    mkdir hyperionDev
) else (
    mkdir new-projects
)
