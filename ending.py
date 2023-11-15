def get_initials(name):
     
    name_string = ""


    name_list = name.split()
    for item in name_list:
        first = item[0].upper()
        name_string += first

    return name_string

          
