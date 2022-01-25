"""Class to init variables of whole project"""
class InitValues():

    path = "Genomes\\Test\\" # data input file path
    file_name = "access_id" # data input file name
    file_name_long = "access_id_long" # data input file name
    
    dbname = file_name + ".sqlite3" # sqlite db name with extention
    dbtable = "dinuctbl" # sqlite db table name

    shuffle_mono = 0 # times to shuffle seq by mononucs 
    shuffle_di = 3 # times to shuffle seq by dinucs
    shuffle_tri = 0 #times to shuffle seq by trinucs 
    shuffle_quantity = shuffle_mono + shuffle_di + shuffle_tri # all shuffles
