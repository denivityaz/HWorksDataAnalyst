from pathlib import Path


for file in Path('./station_data').iterdir():
    station_id = str(file).split('_')[-1].split('.')[0]
    with open(file, mode='r', encoding='utf-8') as fp:
        content = fp.readlines()

    for row in content:
        print(f'{station_id}, {row}', end='')

