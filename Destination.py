import csv
import Companies

myFile = input('Enter the filename here: ')

with open(myFile, 'r') as file1:
    with open('PDS_Destination.txt', 'w') as file2:
        file_reader = csv.reader(file1)
        line_count = 0
        for row in file_reader:
            player = Companies.Company(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                       row[8], row[9], row[10], row[11], row[12], row[13])

            print(player.print_nme(), player.print_lastName(), player.print_firstName(), player.print_adr(),
                  player.print_cit(), player.print_stt(), player.print_zipc(), player.print_phne(),
                  player.print_altphne(), player.print_keycd1(), player.print_keycd2(), player.print_rgn(),
                  player.print_cmpcd(), player.print_ctype(), player.print_lmt(), player.print_cid(), file=file2)

            line_count += 1
        print("The number of rows equals", line_count, file=file2)