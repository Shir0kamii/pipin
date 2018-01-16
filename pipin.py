from io import StringIO

from clize import run
from sh import pip


def get_package_versions():
    buf = StringIO()
    pip.freeze(_out=buf)
    output = buf.getvalue()
    lines = output.split("\n")
    lines = lines[:-1]  # Remove empty line at the end
    rv = {}
    for line in lines:
        index = line.find("==")
        package = line[:index]
        rv.update({package: line})
    return rv


def pin_versions(lines, table):
    for i in range(len(lines)):
        line = lines[i]
        if line in table:
            lines[i] = table[line]
    return lines


def process_one_file(requirements_file):
    table = get_package_versions()
    with open(requirements_file) as reqfile:
        lines = list(map(str.strip, reqfile))
    fixed_lines = pin_versions(lines, table)
    rv = "\n".join(fixed_lines)
    with open(requirements_file, 'w') as reqfile:
        reqfile.write(rv)


def main(*requirements_file):
    """Pin version in your requirements file

    :parm requirements_file: The requirements files to fix
    """
    for file in requirements_file:
        process_one_file(file)


def entry_point():
    run(main)


if __name__ == '__main__':
    entry_point()
