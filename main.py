import asyncio
import shutil
import argparse
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def copy_file(file_path: Path, output_folder: Path):
    """Copies a file to the appropriate subfolder based on its extension."""
    ext = file_path.suffix.lstrip('.').lower() or 'unknown'
    target_dir = output_folder / ext
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / file_path.name

    try:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, shutil.copy2, file_path, target_path)
        logging.info(f'File {file_path} copied to {target_path}')
    except Exception as e:
        logging.error(f'Error copying {file_path}: {e}')


async def read_folder(source_folder: Path, output_folder: Path):
    """Reads all files in the source folder and sends them for copying."""
    tasks = []
    for file_path in source_folder.rglob('*'):
        if file_path.is_file():
            tasks.append(copy_file(file_path, output_folder))

    await asyncio.gather(*tasks)


async def main():
    parser = argparse.ArgumentParser(description='Asynchronous file sorting by extension.')
    parser.add_argument('source_folder', type=Path, help='Path to the source folder')
    parser.add_argument('output_folder', type=Path, help='Path to the destination folder')
    args = parser.parse_args()

    if not args.source_folder.exists() or not args.source_folder.is_dir():
        logging.error(f'Source folder {args.source_folder} does not exist or is not a directory.')
        return

    args.output_folder.mkdir(parents=True, exist_ok=True)
    await read_folder(args.source_folder, args.output_folder)


if __name__ == '__main__':
    asyncio.run(main())
