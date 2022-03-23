
class InitValues():
    """Class to init variables of whole project

    Enterobacteria path and files
    path = "Genomes\\Enterobacteria\\" # data input file path
    file_name = "enterobacteria" # data input file name
    file_name_long = "enterobacteria_long" # data input file name

    path = "Genomes\\Plants\\"
    file_name = "embryophyta"
    file_name_long = "embryophyta_long"
    """
    path = "Genomes\\Procaryote\\"
    db_file_name = "procaryote"

    dbname = path + db_file_name + ".sqlite3" # sqlite db name with extention
    dbtable = "dinuctbl" # sqlite db table name

    shuffle_mono = 6 # times to shuffle seq by mononucs 
    shuffle_di = 6 # times to shuffle seq by dinucs
    shuffle_tri = 6 #times to shuffle seq by trinucs 
    shuffle_quantity = shuffle_mono + shuffle_di + shuffle_tri # all shuffles
