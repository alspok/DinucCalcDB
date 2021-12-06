import sqlite3
import scipy
from scipy.stats import sem


def dinucDB():
    db_file = "F:\\ArchaeaDinuc.sqlite3"
    row_list = []
    
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("select di_diff, di_shuffle_diff from dinuctblcomp where description like '%methano%'")
    tbl = cursor.fetchall()
    
    [print(f'{i+1}\t{row[0]}\t{row[1:]}') for i, row in zip(range(len(tbl)), tbl)]
    
    diff_row_list = []
    row_list = []
    for row in tbl:
        diff_row_list.append(float(row[0]))
        row_str = ','.join(row[1:])
        row_list.append([float(j) for j in row_str.split(',')])

    # for item in row_list:        
    #     print(item)
    
    #plot list of lists
    x = []
    [x.append(i) for i in range(len(tbl) + 1)]
    print(row_list[0])
    x = x[:10]
    row_plot = row_list[:10]
    
    print(f'{len(x)}\t{len(row_plot)}')
    
    # x = np.linspace()
    # data = np.array(row_list[0])
    # y = np.std(data, ddof=2) / np.sqrt(np.size(data))
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.stats as stat
    
    mean = []
    stderr = []
    mean_diff = []
    x = np.linspace(0, 10, 106)
    mean = [np.mean(row) for row in row_list[:106]]
    y = [[mean_diff] for dm, row in zip(diff_row_list, row_list)]
    # mean_diff = [for drow in zip(mean,)]
    stderr = [stat.sem(row) for row in row_list[:106]]
    
    plt.figure(figsize=(16, 6))
    plt.ylim(0.05, 0.2)
    plt.errorbar(x, mean, yerr=stderr, fmt='.k')
    
    plt.show()
    
    
    pass
    
if __name__ == '__main__':
    dinucDB()