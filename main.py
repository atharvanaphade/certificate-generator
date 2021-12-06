from read_data import *

def main():
    print("Support and contribute to this repository on : https://github.com/atharvanaphade/certificate-generator")
    print("Instructions : ")
    print("Place the certificates in the root of this directory, and name them as 'first.png', 'second.png', 'third.png', 'participation.png'")
    print("Place the csv file with columns, index, name, rank in the root of this directory")
    print("Enter the name of the csv file : ", end='')
    csv_file = input()
    print("Place the font file in the root of this directory")
    print("Enter font_file name : ", end='')
    font_file = input()
    print("Enter the coordinates of the start of the text : ")
    print("Enter x : ", end='')
    start_x = input()
    print("Enter y : ", end='')
    start_y = input()
    print("Enter font size : ", end='')
    font_size = input()
    write_data(select_csv(csv_file), start_x, start_y, font_file, font_size)
    

if __name__ == "__main__":
    main()