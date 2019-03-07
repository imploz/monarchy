from . import monarch


def parse_years(years: str):
    if years.isdigit():
        return [int(years)]*2
    if years[-1] == '-':
        since = years[0:-1]
        return int(since), None
    else:
        return map(int, years.split('-'))


def from_dict(d: dict):
    since, to = parse_years(d['yrs'])
    return monarch.Monarch(id=d['id'], name=d['nm'], country=d['cty'], house=d['hse'], since=since, to=to)
