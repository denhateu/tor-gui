@echo off
rem Disables programms output in console

rem Variables
set "project_name=verborgen"
set "project_version=v0.0.1-alpha"
set "project_full_name=%project_name%_%project_version%"

set "scripts_folder=src"
set "bin_folder=bin"
set "libs_folder=tor"

rem Clears build directory
echo [ Clear build ]
rmdir /S /Q %bin_folder%\

mkdir %bin_folder%
mkdir %bin_folder%\%project_full_name%
echo [ Cleared ]

rem Empty string
echo.

rem Compiling program to exe file
echo [ Compiling... ]

rem With icon: pyinstaller %scripts_folder%\main.py --name %project_name% --onefile --windowed --icon=assets\img\favicon.ico
uv run pyinstaller %scripts_folder%\main.py --name %project_name% --onefile --windowed

echo.

rem Copy builded program and some it components to bin\ directory
copy dist\%project_name%.exe %bin_folder%\%project_full_name%

mkdir %bin_folder%\%project_full_name%\%libs_folder%\
xcopy %libs_folder% %bin_folder%\%project_full_name%\%libs_folder%\ /E /H /C /I

echo.

rem Creates zip file from compiled project
echo [ Packaging to zip... ]

cd %bin_folder%\

7z a %project_full_name%.zip %project_full_name%\

cd ..

echo.

echo [ Packed! ]

echo.

echo   +----------------------+
echo  /  Compiled finished!  /
echo +----------------------+
