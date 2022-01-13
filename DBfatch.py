import sqlite3
import scipy
from scipy.stats import sem


def dinucDB():
    # db_file = "F:\\ArchaeaDinuc.sqlite3"
    db_file = "F:\\VirusesDinuc.sqlite3"
    row_list = []
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    # cursor.execute("select di_diff, di_shuffle_diff from dinuctblcomp where description like '%methano%'")
    cursor.execute("select di_diff, di_shuffle_diff from dinuctbldna")
    tbl = cursor.fetchall()
    data_start, data_end = 400, 600
    
    # [print(f'{i+1}\t{row[0]}\t{row[1:]}') for i, row in zip(range(len(tbl)), tbl)]
    
    diff_row_list = []
    row_list = []
    for row in tbl:
        diff_row_list.append(float(row[0]))
        row_str = ','.join(row[1:])
        row_list.append([float(j) for j in row_str.split(',')])

    '''Plot section'''

    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.stats as stat
    
    mean = []
    stderr = []
    # x = np.linspace(data_start, data_end)
    x = range(data_start, data_end)
    mean = [np.mean(row) for row in row_list[data_start:data_end]]
    stderr = [stat.sem(row) for row in row_list[data_start:data_end]]

    fig, ax = plt.subplots(figsize=(17, 8))
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)
    plt.ylim(-0.01, 0.40)
    ax.scatter(x, diff_row_list[data_start:data_end], s=6, c='red')
    ax.errorbar(x, mean, yerr=stderr, fmt='.k')
    # plt.errorbar(x, mean, yerr=stderr, fmt='.k')
    
    plt.show()
    
if __name__ == '__main__':
    dinucDB()