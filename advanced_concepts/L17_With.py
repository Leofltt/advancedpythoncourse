
# DOES NOT WORK
# file = open('advanced_concepts/dummy.txt', 'r')
# data = file.readline()
# new_data = data + 2
# file.close()

# try except version
# try: 
#     file = open('advanced_concepts/dummy.txt', 'r')
#     data = file.readline()
#     new_data = data + 2
# except TypeError as error:
#     print(error)
# finally:
#     print('Safely closing file')
#     file.close()

# with version (much nicer :D)
with open('advanced_concepts/dummy.txt', 'r') as file:
    data = file.readline()
    new_data = join(data, '\n 2')
    file.write(new_data)