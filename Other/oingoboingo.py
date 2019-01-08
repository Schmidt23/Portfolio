# -*- coding: utf-8 -*-
"""
Creates randomized bingo boards
"""
import random
import math
import argparse
import pandas as pd


CSS = """<head>
<style>
table {  
    color: #333;
    font-family: Helvetica, Arial, sans-serif;
    width: 25em;
    border-collapse: 
    collapse; border-spacing: 50px 0; 
    margin: 10px;
    float: left;
    table-layout: fixed;
    word-wrap: break-word;
    font-size: 70%
}

td, th { border: 1px solid #CCC; height: 4em;width: 4em;} 

th {  
    background: #F3F3F3; 
    font-weight: bold; 
}

td {  
    background: #FAFAFA;
    text-align: center;
    layout: fixed;
}
</style>
</head>
"""

def write_css(out_path, css):
    """create/overwrite file and fill with defined CSS header"""
    with open(out_path, 'w') as file_out:
        file_out.write(css)

def get_words(file_path):
    """read input file"""
    with open(file_path, 'r') as file_in:
        #one word per line; strip newline marker
        wordlist = [word.strip("\n") for word in file_in.readlines()]
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
    with open(fp, 'a') as file_out:
        file_out.write(html)

if __name__ == "__main__":
    #default constants
    fp = "t.html"
    inp_path = "input.txt"
    words = get_words(inp_path)
    columns = int(math.sqrt(len(words)))
    rows = int(len(words)/columns)

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

    write_css(fp, CSS)

    #append given number of boards to file
    for n in range(num_boards):
        create_board(words)
