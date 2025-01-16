# $ python main.py "track.csv"

import csv
from typing import Dict, List
import click

class Entry():
    def __init__(self, desc:str, time:int, tags:str):
        self.desc = desc
        self.time = time
        self.tags = tags.split()

    def __str__(self):
        return f"{self.time:6}  {self.tags} {self.desc}"
    
    def __repr__(self):
        return f"Entry(desc={self.desc!r}, time={self.time!r}, tags={self.tags!r})"

def crating_Entry_from_dict(row:Dict[str, str]) -> Entry:
    return Entry(
        time=int(row['time']),
        tags=row['tags'],
        desc=row['desc']
    )

    
def read_track(filename:str) -> List[Entry]:
    with open(filename, encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        tracks = [crating_Entry_from_dict(row) for row in reader]
    return tracks

def calculate_time_by_tag(entries:List[Entry]) -> Dict[int, str]:
    time_by_tag = {}
    for entry in entries:
        for tag in entry.tags:
            if tag in time_by_tag:
                time_by_tag[tag] += entry.time
            else:
                time_by_tag[tag] = entry.time
    return time_by_tag

def print_raport(time_by_tag:Dict[int, str]) -> None:
    print("TOTAL-TIME   TAG")
    print("----------   ----")
    for tag, total_time in sorted(time_by_tag.items(), key=lambda x: x[1], reverse=True):
        print(f"{total_time:10}   #{tag}")

@click.command()
@click.argument('filename')

def main(filename:str) -> None:
    entries = read_track(filename)
    time_by_tag = calculate_time_by_tag(entries)
    print_raport(time_by_tag)


if __name__ == '__main__':
    main()
