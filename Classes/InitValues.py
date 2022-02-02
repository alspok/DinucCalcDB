"""Class to init variables of whole project"""
class InitValues():

    path = "Genomes\\Archaea\\" # data input file path
    file_name = "archaea" # data input file name
    file_name_long = "archaea_long" # data input file name
    
    dbname = path + file_name + ".sqlite3" # sqlite db name with extention
    dbtable = "dinuctbl" # sqlite db table name

    shuffle_mono = 6 # times to shuffle seq by mononucs 
    shuffle_di = 6 # times to shuffle seq by dinucs
    shuffle_tri = 6 #times to shuffle seq by trinucs 
    shuffle_quantity = shuffle_mono + shuffle_di + shuffle_tri # all shuffles
