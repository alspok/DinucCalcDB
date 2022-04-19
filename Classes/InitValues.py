
class InitValues():
    """ Class to init variables of whole project """
    
    path = "Genomes\\Test\\Small_Large\\"
    split_path = path.split('\\')
    last_path = split_path[-2]
    name = "bacteria_small"
    file_name = path + name + ".acc"
    db_name = path + name + ".sqlite3"
    db_table = "dinuctbl" # sqlite db table name

    shuffle_mono = 6 # times to shuffle seq by mononucs 
    shuffle_di = 6 # times to shuffle seq by dinucs
    shuffle_tri = 6 #times to shuffle seq by trinucs 
    shuffle_quantity = shuffle_mono + shuffle_di + shuffle_tri # all shuffles
