# Async File Sorter

## Description
This Python script asynchronously sorts files from a source directory into subdirectories in a destination folder based on their extensions. It efficiently processes large numbers of files using asynchronous execution.

## Features
- Reads all files in a source directory (including subdirectories).
- Copies files to subdirectories in the destination folder based on their file extensions.
- Uses asynchronous operations for efficient execution.
- Logs progress and errors.

## Installation
No additional dependencies are required. Ensure you have Python installed.

## Usage
Run the script from the command line:

```sh
python script.py /path/to/source /path/to/destination
```

### Arguments
- `source_folder`: Path to the folder containing files to be sorted.
- `output_folder`: Path to the destination folder where sorted files will be stored.

