# -*- coding: utf-8 -*-
"""
creates randomized bingo boards
"""

import random
import math
import argparse
import os
import sys
import webbrowser
import pandas as pd


def_css = """<head>
<style>
@media all{
page {
  size: A4;
  margin: 0;
}
table {  
    color: #333; /* Lighten up font color */
    font-family: Helvetica, Arial, sans-serif; /* Nicer font */
    width: 45%;
    border-collapse: collapse;
    border-spacing: 25px 0; 
    margin: 5px;
    float: left;
    table-layout: fixed;
    word-wrap: break-word;
    font-size: 50%;
    page-break-inside: avoid;
}

td, th { 
    border: 1px solid #CCC;
    height: 4em;
    width: 4em;
    layout: fixed;
    font-size: 1em;


} /* Make cells a bit taller */

th {  
    background: #F3F3F3; /* Light grey background */m7z
    font-weight: bold; /* Make sure they're bold */
    layout: fixed;
}

td {  
    background: #FAFAFA; /* Lighter grey background */
    text-align: center; /* Center our text */
    layout: fixed;
}
}
</style>
</head>
"""

def write_css(out_path, css):
    """create/overwrite file and fill with defined CSS header"""
    try:
        with open(out_path, 'w') as file_out:
            file_out.write(css)
    except IOError as e:
        print(e)
        sys.exit(1)


def get_words(file_path):
    """read input file"""
    try:
        with open(file_path, 'r') as file_in:
            #one word/item per line; strip newline marker
            wordlist = [word.strip("\n") for word in file_in.readlines()]
    except IOError as e:
        print(e)
        sys.exit(1)

    return wordlist


def fill_board(inp, ro, co):
    """put words into matrix; fill row by row"""
    board = []
    for _ in range(ro):
        #cut words from word list, count= columns
        for j in range(co+1):
            smpl = inp[:j]
        #word for word as list of lists
        board.append([item for item in smpl])
        #slice taken words from list and continue
        inp = inp[co:]
    return board


def create_board(board):
    """append finished board to output file"""
    #shuffle wordlist
    board = random.sample(board, len(board))
    #create Dataframe from created board
    df = pd.DataFrame(fill_board(board, rows, columns))

    #convert Dataframe to html
    html = df.to_html(header=False, col_space=2, index=False, bold_rows=True,
                      float_format="right", justify="match-parent")

    #write html to output_path
    try:
        with open(fp, 'a') as file_out:
            file_out.write(html)
    except IOError as e:
        print(e)
        sys.exit(1)



if __name__ == "__main__":
    #default constants
    HOME = os.path.expanduser("~")
    fp = "{}/My Documents/t.html".format(HOME)
    inp_path = "{}/My Documents/input.txt".format(HOME)
    words = get_words(inp_path)
    columns = int(math.sqrt(len(words)))
    rows = int(len(words)/columns)
    info = "{} words {} used".format(len(words), columns*rows)

    med = []
    num_boards = 10


    #parse optional system args
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--columns", type=int,
                        help="choose columns count")
    parser.add_argument("-r", "--rows", type=int,
                        help="choose rows count")
    parser.add_argument("-o", "--output",
                        help="choose output path")
    parser.add_argument("-i", "--input",
                        help="choose input path")
    parser.add_argument("-n", "--number",
                        type=int, help="choose number of boards")
    parser.add_argument("-w", "--width", type=int,
                        help="change relational width of tables in percent  \
                        default=45")
    parser.add_argument("-b", "--browser", action="store_true",
                        help="open output directly in browser")

    args = parser.parse_args()

    if args.columns:
        columns = args.columns
    if args.rows:
        rows = args.rows
    if args.output:
        fp = args.output
    if args.input:
        inp_path = args.input
    if args.number:
        num_boards = args.number
    if args.width:
        new_width = "width: {}".format(args.width)
        def_css = def_css.replace("width: 45", new_width)

    # open and write css into file
    write_css(fp, def_css)

    # print info about words
    info = "{} words {} used".format(len(words), columns*rows)
    print(info)

    #append given number of boards to file
    for n in range(num_boards):
        create_board(words)

    # open output in browser if option is selected
    if args.browser:
        webbrowser.open(fp)
