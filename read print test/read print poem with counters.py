
name_of_mydocument = 'tuesdayafternoon.txt'







file_input = open(name_of_mydocument, 'r')     #open file for reading







total_lines_in_file = 0







                                     #read the first few lines







line = file_input.readline()

print(line)

total_lines_in_file = total_lines_in_file + 1



#line = file_input.readline()







line = file_input.readline()

print(line)
total_lines_in_file = total_lines_in_file + 1




#line = file_input.readline()







#line = file_input.readline()







line = file_input.readline()







                                     # This reads the first paragraph



line = file_input.readline()



stanza_counter = 0







                                     # \n - indicates blank line







while line != '':                  # while not a blank line



  if line == "\n":



    stanza_counter = stanza_counter + 1

    print()

    line = file_input.readline()

  else:

    total_lines_in_file = total_lines_in_file + 1               

    
      
    if total_lines_in_file < 10:
        print(str(total_lines_in_file)+ ')   ', line, end = '')
    else:
      print(str(total_lines_in_file) + ')  ', line, end = '')


    line = file_input.readline()
line = file_input.readline()
print ("\n\n-- End of Song ---")
print ("Total number of stanzas in this poem are: " + str(stanza_counter) + ".")
print ("Total number of lines in this file are: " + str(total_lines_in_file) + ".")
print ("This song first appeared in the album 'Days of Future Passed' in 1968")
print ("The Moody Blues members are Mike Lodge, Graeme Edge, Justin Hayward, Ray Thomas, and John Lodge.")