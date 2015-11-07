#!/usr/bin/env python

import sys
from datetime import datetime

TEMPLATE = """
{title}
{hashes}

:date: {year}-{month}-{day} {hour}:{minute:02d}
:tags:
:category: {category}
:slug: {slug}
:summary:
:status: draft


"""


def make_entry(category, title):
    today = datetime.today()
    slug = category + "/" + title.lower().strip().replace(' ', '-')
    f_create = "content/{}.rst".format(slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                category=category,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


if __name__ == '__main__':
    if len(sys.argv) > 2:
        make_entry(sys.argv[1], sys.argv[2])
    else:
        print "No title given"
        sys.exit(1)
