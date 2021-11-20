# -*- coding: utf-8 -*-

from __future__ import print_function, division
import argparse
import re
from os.path import join

import subprocess
from urllib.request import Request, urlopen

__author__ = 'Fisher Yu'
__email__ = 'fy@cs.princeton.edu'
__license__ = 'MIT'


def list_categories():
    url = 'http://dl.yf.io/lsun/objects/'
    with urlopen(Request(url)) as response:
        return re.findall(r'href="(.*?)\.zip"',
                response.read().decode())


def download(out_dir, category):
    url = f'http://dl.yf.io/lsun/objects/{category}.zip'
    out_name = f'{category}.zip'
    out_path = join(out_dir, out_name)
    cmd = ['curl', url, '-C', '-', '-o', out_path]
    print('Downloading', category)
    subprocess.call(cmd)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out_dir', default='')
    parser.add_argument('-c', '--category', default=None)
    args = parser.parse_args()

    categories = list_categories()
    if args.category is None:
        print('Downloading', len(categories), 'categories')
        for category in categories:
            download(args.out_dir, category)
    else:
        if args.category not in categories:
            print('Error:', args.category, "doesn't exist in", 'LSUN release')
        else:
            download(args.out_dir, args.category)

if __name__ == '__main__':
    main()
