import re

def parse_all(string):
    regex = re.compile(r"((?P<add>\+\d+)|(?P<multiply>x\d+)|(?P<divide>\/\d+)|(?P<balance>\(\d+\))|(?P<subtract>\-\d+)|(?P<delete_last>\<\<)|(?P<first_digit_to_second>(\d+)\=\>(\d+))|(?P<insert_number>\d))")
    match = regex.match(string)
    groups = match.groupdict()
    return [(a[0],only_numbers(a[1])) for a in groups.items() if a[1] != None][-1]

def only_numbers(string):
    all_nums = [int(a) for a in re.sub('[^0-9]+',",", string).split(",") if a]
    return all_nums

if __name__ == "__main__":
    pass