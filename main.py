import requests
from logo import logo, story_head

def get_users_words():
    """
    Function that iterates through each type of blank, and returns a list '
    of the users input.
    """
    users_words = [] 
    for item in madlib['blanks']:
        word = input(f"Please enter a/n [{item}]: ")
        users_words.append(word)
        
    return users_words
    
    
def put_madlib_together(usr_input, story):
    """
    Function that takes the list of users input and the story, and pieces 
    it together, returning the final story
    """
    final_story = ""
    for i in range(len(usr_input)):
            final_story += str(story[i])
            final_story += str(usr_input[i])
    
    return final_story
    
    
# Getting Madlib from API
ML_Endpoint = "http://madlibz.herokuapp.com/api/random"
mad_params = {
  'minlength': 2,
  'maxlength': 17
}
response = requests.get(url=ML_Endpoint, params=mad_params)
lib = response.json()

title = lib['title']
blanks = lib['blanks']
story = lib['value']

madlib = {
  'title': title,
  'blanks': blanks,
  'story': story
}

print(logo)
print(f"\n{madlib['title']}\n")
users_input = get_users_words()
final = put_madlib_together(users_input, madlib['story'])
print(f"\n{story_head}\n    {final}")
