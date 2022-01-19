def fileModification():

    input_file = "Genomes\\Plants\\embryophyta"
    output_file = "Genomes\\Plants\\embryophyta_mod"
    genome_length = 10**9

    with open(input_file, "r") as fhr:
        read_list = list(fhr)

    with open(output_file, "w") as frw:
        for line in read_list:
            temp_line = line.split("\t")
            if int(temp_line[-1]) <= genome_length:
                frw.write(f"{temp_line[-2]}\t{temp_line[-1]}")

    print(f"Assembly id in file {output_file} done.")            
    pass

if __name__ == "__main__":
    fileModification()