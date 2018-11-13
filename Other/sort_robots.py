import re
import os
import getopt
import sys


"""Takes .robot files and creates sorted copies"""


def return_output_file_name(inpt, mark="s"):
    #returns full path of given file with added output directory and filename marker
    fn = os.path.basename(inpt)
    dn = os.path.dirname(inpt)
    return dn+output_dirname+"\\" + mark + fn


def get_lines(fl):
    #returns content line by line of given file
    lines = []
    try:
        with open(fl, 'rb') as f:
            for line in f.readlines():
                lines.append(line)
    except IOError as e:
        print "get_linesError", e
    return lines


def add_tc_dict(tc):
    #divides lines into blocks of testcase/keyword def and components
    blocks = {}
    block = []
    for i in tc:
        #if there is no whitespace at start of line
        if re.search(r"^\S", i):
            #it's a title/block
            block.append(i)
            #append as empty keyword
            blocks[block[-1]] = ""
        #if whitespace it belongs to last title/block added
        elif re.search(r"^\s", i):
            blocks[block[-1]] += i
    return blocks


def write_output(nf, st, blocks):
    #creates a new file where keywords/testcases are sorted alphabetically
    try:
        with open(nf, "wb+") as f:
            #Settings don't need to be sorted
            for i in st:
                f.write(i)
            #keywords/testcases get sorted
            for k, v in sorted(blocks.items()):
                f.write(k+v)
    except IOError as e:
        print "writeError:", e


def create_sorted_robot(fl):
    #get content of given file
    lines = get_lines(fl)
    #generate output full path for file
    nf = return_output_file_name(fl)
    #look for occurence of *** TestCases/Keywords ***
    pmatch = re.search(pattern, "".join(lines))
    ind = pmatch.group(1) + "\r\n"
    #split into settings part and keywords/testcases part
    st = lines[:lines.index(ind) + 1]
    tc = lines[lines.index(ind) + 1:]
    #create dict of titles and components
    blks = add_tc_dict(tc)
    #create file and write to it
    write_output(nf, st, blks)


def create_output_directory(o_path):
    #create output folder if it doesn't already exist
    if not os.path.exists(o_path):
        try:
            os.makedirs(o_path)
        except OSError as e:
            print e


def parse_directoy(path):
    #check if file in dir endswith .robot and add to list
    d = [os.path.join(path, f) for f in os.listdir(path) if ".robot" in os.path.join(path, f)]
    for f in d:
        print f
        create_sorted_robot(f)


def parse_single_file(path):
    create_sorted_robot(path)


if __name__ == "__main__":
    #Defaults
    pattern = re.compile(r"(\*{3} (Test Cases|Keywords) \*{3})")
    inp = os.getcwd()
    #path = "C:\\Users\\SchmidtC\\sortRobots\\"
    #fle = "U:\\scripte\\Python\\AuditMngr_UI_Chrome.robot"
    output_dirname = "\\op"
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:")
    except getopt.GetoptError:
        print "sort_robots.py -p <file|path>"

    for opt, arg in opts:
        if opt == '-p':
            inp = arg

    print inp

    if os.path.isdir(inp):
        output_path = inp + output_dirname
        create_output_directory(output_path)
        parse_directoy(inp)
    elif os.path.isfile(inp):
        #strip file name and append output folder name<
        output_path = os.path.dirname(inp) + output_dirname
        create_output_directory(output_path)
        parse_single_file(inp)