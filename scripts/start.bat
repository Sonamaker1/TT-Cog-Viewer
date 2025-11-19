@echo off
cd ..

set /P PYTHON_PATH=<PYTHON_PATH

cd src

%PYTHON_PATH% -m main
pause
