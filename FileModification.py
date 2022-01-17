def fileModification():

    input_file = "GenomeTable\\embryophyta"
    output_file = "GenomeTable\\embryophyta.mdf"

    with open(input_file, "r") as fhr:
        read_list = list(fhr)

    with open(output_file, "w") as frw:
        for line in read_list:
            temp_line = line.split("\t")
            frw.write(temp_line[-1])

    print(f"Assembly id in file {output_file} done.")            
    pass

if __name__ == "__main__":
    fileModification()