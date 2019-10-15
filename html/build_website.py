""" Build index from directory listing

python build_website.py </path/to/directory> [--header <header text>]
e.g., python build_website.py ./ --header "Analyzing Opioid Data"
"""

INDEX_TEMPLATE = r"""
<html>
<body>
<h2>${header}</h2>
<p>
% for name in names:
    <li><a href="${name}">${name}</a></li>
% endfor
</p>
</body>
</html>
"""

EXCLUDED = ['index.html', 'build_website.py', 'build_website.sh']

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--header")
    args = parser.parse_args()

    out_html = os.path.join(args.directory, "index.html")

    fnames = [fname for fname in sorted(os.listdir(args.directory))
    # fnames = [fname for fname in sorted(os.listdir(html_dir))
              if fname not in EXCLUDED]
    header = (args.header if args.header else os.path.basename(args.directory))
    # header = (args.header if args.header else os.path.basename(html_dir))
    lines = Template(INDEX_TEMPLATE).render(names=fnames, header=header)
    print(lines)

    with open(out_html, 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    main()
    # print(os.getcwd())