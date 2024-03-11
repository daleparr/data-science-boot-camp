@echo off
REM Create three new folders
mkdir folder1
mkdir folder2
mkdir folder3

REM Navigate into one of the folders and create three new folders inside it
cd folder1
mkdir subfolder1
mkdir subfolder2
mkdir subfolder3

REM Remove two of the folders created
rmdir subfolder1
rmdir subfolder2

cd ..
