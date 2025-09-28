@echo off
echo Building FileForge executable...
echo.

REM Install requirements if pyinstaller is not available
python -c "import pyinstaller" 2>nul
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install -r requirements.txt
    echo.
)

REM Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "fileforge.spec" del "fileforge.spec"

REM Build the executable
echo Creating executable...
pyinstaller --onefile --windowed --name="FileForge" --icon=NONE fileforge.py

REM Check if build was successful
if exist "dist\FileForge.exe" (
    echo.
    echo ✓ Build successful!
    echo ✓ Executable created: dist\FileForge.exe
    echo.
    echo You can now run the application by double-clicking FileForge.exe
) else (
    echo.
    echo ✗ Build failed!
    echo Check the output above for errors.
)

pause