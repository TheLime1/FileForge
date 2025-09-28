<div align="center">
  <img src="logo.png" alt="FileForge Logo" width="200" height="200">
  
  # FileForge
  
  *A modern GUI-based file generator that creates random files with specified parameters.*
</div>

## Features

- **User-friendly GUI interface** with intuitive controls
- **Customizable file generation** with configurable names and extensions
- **Smart file sizing** based on file type:
  - **Code files**: 1KB - 10KB (suitable for source code, text files, etc.)
  - **Other files**: 1MB - 10MB (suitable for images, archives, binaries, etc.)
- **Flexible output** with selectable output directory
- **Progress feedback** with status updates
- **Input validation** with error handling

## Usage

### Running from Python

1. Install Python 3.7 or higher
2. Run the application:
   ```bash
   python fileforge.py
   ```

### Building Executable

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the build script:
   ```bash
   build.bat
   ```

3. The executable will be created in the `dist` folder as `FileForge.exe`

### Manual Build (Alternative)

```bash
pyinstaller --onefile --windowed --name="FileForge" fileforge.py
```

## Interface Guide

- **File Name**: Base name for generated files (e.g., "document")
- **File Extension**: Extension for files (e.g., "txt", "jpg", "zip")
- **Number of Files**: How many files to generate
- **File Type**: 
  - **Code**: Generates smaller files (1KB-10KB) suitable for text/code
  - **Other**: Generates larger files (1MB-10MB) suitable for media/binaries
- **Output Directory**: Where to save the generated files (defaults to "gen")

## Examples

- Generate 5 text files: Name="document", Extension="txt", Type="code", Count=5
- Generate 3 image files: Name="photo", Extension="jpg", Type="other", Count=3
- Generate 1 archive: Name="backup", Extension="zip", Type="other", Count=1

## Output

Files are generated with random binary content in the specified size ranges. If generating multiple files, they will be numbered (e.g., document_1.txt, document_2.txt, etc.).

## Requirements

- Python 3.7+
- tkinter (usually included with Python)
- pyinstaller (for building executable)

## License

This project is open source and available under the MIT License.