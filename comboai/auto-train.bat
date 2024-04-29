@echo off
setlocal

rem Set the number of times you want to run the command
set "iterations=10"

rem Replace with path to your DIAMBRA roms folder
set "yourCommand=diambra run -r C:\Users\Asus\.diambra\roms python test.py"

rem Loop through the specified number of iterations
for /l %%i in (1,1,%iterations%) do (
    echo Running iteration %%i
    %yourCommand%
)

endlocal