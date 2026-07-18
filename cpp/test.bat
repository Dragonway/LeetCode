@echo off
setlocal

cd /d "%~dp0"

if "%~1"=="" (
    echo Usage:
    echo test.bat ^<problem^>   - build and run tests for a particular problem
    echo test.bat --all       - build and run ALL tests
    exit /b 1
)

if not exist "build\CMakeCache.txt" (
    echo [test] Build dir not configured, running configure...
    call configure.bat
    if errorlevel 1 exit /b 1
)

if /i "%~1"=="--all" goto run_all

echo [test] Building target: %~1
cmake --build build --config Debug --target %~1
if errorlevel 1 (
    echo [test] Build FAILED for target "%~1"
    exit /b 1
)

echo [test] Running tests for '%~1'
ctest --test-dir build -C Debug -R "^%~1$" --output-on-failure
exit /b %errorlevel%

:run_all
echo [test] Building ALL targets...
cmake --build build --config Debug
if errorlevel 1 (
    echo [test] Build FAILED
    exit /b 1
)

echo [test] Running ALL tests
ctest --test-dir build -C Debug --output-on-failure
exit /b %errorlevel%
