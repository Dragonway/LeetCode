@echo off
setlocal

cd /d "%~dp0"

cmake -S . -B build %*
if errorlevel 1 (
    echo.
    echo [configure] FAILED
    exit /b 1
)

echo [configure] OK
endlocal
