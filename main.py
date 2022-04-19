import requests


def get_new_lib():
    ML_Endpoint = "http://madlibz.herokuapp.com/api/random"
    mad_params = {
        'minlength': 3,
        'maxlength': 5
    }    
    response = requests.get(ML_Endpoint, params=mad_params)
    lib = response.json()
    print(lib)
    blanks = lib["blanks"]
    title = lib["title"]
    story = lib["value"]
    mad_lib = { 
        'title': title,
        'blanks': blanks,
        'story': story
    }
    return mad_lib

def fill_in_blanks(blank_lst):
    entries = []
    req_usr = "Please Enter a/an:"
    for lib in blank_lst:
        entry = input(f"{lib}: ")
        entries.append(entry)
    return entries
    
        
def display_fin_lib():
    s = []
    i = 0
    for line in madlib['story']:
        s.append(f"{line} {entries[i]}")
        i += 1
        
    print(s)
    
# GET MadLib from API
madlib = get_new_lib()
# get input from user (fill in blanks)
entries = fill_in_blanks(madlib['blanks'])
#print(len(madlib['blanks'])
# Show final story
display_fin_lib()

#print(type(madlib['story']))