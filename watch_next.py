"""
SE T38 - Semantic Similarity (NLP)
Thomas Siu - TS22110004677
Compulsory Task 2
"""

# Import spacy and load en_core_web_md model as 'nlp'
import spacy

nlp = spacy.load('en_core_web_md')


# Read in the 'movies.txt' file and save to a dictionary with tiles and descriptions
with open('movies.txt', 'r') as file:
    
    #movies_list = []
    #for movies in file:
    #    movies_list.append(movies)
    movies_dict = {}
    for movies in file:
        title, description = movies.split(':')
        movies_dict[title] = description

# As required by the task, we try to suggest moveis a user would watch after 'Planet Hulk' and its associated description
# We apply the nlp model to the search phrase
search = nlp('''Planet Hulk :Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle amd launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk land on the planet Sakaar where he is sold into vlavery and trained as a gladiator.''')

# For each movie in the list, apply the nlp model and compare against the search phrase
# The variables 'rank' and 'suggestion' is for recording the movie with the highest similarity score when compare to the search phrase
rank = 0
suggestion = ''

for movies in movies_dict:
    description = movies_dict[movies]
    description_nlp = nlp(description)
    result = search.similarity(description_nlp)
    print(f'{movies}: Similarity score when compare to the search phrase {result}')

    # Compare result similarity score to existing rank score; update suggestion if the score is higher.
    if result > rank:
        rank = result
        suggestion = movies

# Print suggestion after the search
print(f'\nBased on the search, you would be interest in watching {suggestion}next!\n')