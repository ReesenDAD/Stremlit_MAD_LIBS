#Note: Code to run in terminal is "python -m streamlit run Streamlit_Demo.py" from Desktop

# Importing the necessary libraries
import streamlit as st
import json

st.title('Mad Libs - Make Your Own Story')

mad_libs = []

# Opening the json file
with open('train-polichecked.json', 'r', encoding='utf-8') as file:
    mad_libs = json.load(file)

# Finding all stories from the Microsoft Mad Libs dataset
stories = list(mad_libs)

# generation_button = st.button("Click me to generate a story")

# if generation_button:
#     # Randomly selecting one of the stories
#     n = random.randint(0,29)
#     story = stories[n]
# else:
#     story = 'Little Red Riding Hood'

# Allowing the user to choose the story
story = st.segmented_control(
    "Choose an story:",
    options=["Little Red Riding Hood", "Spider-Man", "Kim Kardashian", "Kangaroos", "The Large Hadron Collider"],
    default="Little Red Riding Hood"
)

# Opening the raw text of the story 
file = mad_libs[story]
raw_text = file['text']

# Determining the indeces of < and > (to find number of words needed)
indices = [index for index, char in enumerate(raw_text) if char == '<' or char == '>']

# determining the number of words that must be provided
num_words = len(indices)/2

# drawing out each "blank" and the associated word
inputs_with_given = []
for i in range(0,int(len(indices)/2)):
    inputs_with_given.append(raw_text[indices[2*i]:(indices[2*i+1]+1)])

# Creating a placeholder list to hold the responses
inputs = []

# creating a word index to keep inputs unique
word_index = 1

# Creating a submission 
with st.form(key='responses'):

    # isolating the blank-filling instructions
    for request in inputs_with_given:
        # Finding what's betweeen the last ':' and the '>'
        colon_index = request.rfind(':')
        instruction = request[(colon_index+1):(len(request)-1)]

        # Creating a placeholder for the response
        answer = ''

        # Requesting the corresponding word
        if instruction == 'animal/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide the name of an anmial')
        elif instruction == 'animal_plural/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide the plural name of a group of chosen anmials')
        elif instruction == 'body/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide the name of a body part')
        elif instruction == 'body_plural/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide the name of a group of body parts')
        elif instruction == 'food/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide a type of food')
        elif instruction == 'food_plural/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide the plural name of a type of food')
        elif instruction == 'jj/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide an adjective')
        elif instruction == 'liquid/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide a type of liquid')
        elif instruction == 'nn/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide a noun')
        elif instruction == 'nns/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide a plural noun')
        elif instruction == 'rb/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide an adverb')
        elif instruction == 'vb/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide a verb')
        elif instruction == 'vbd/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide a verb in the past tense')
        elif instruction == 'vbg/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide a verb ending in \'-ing\'')
        elif instruction == 'vbn/':
            answer = st.text_input('Word ' + str(word_index) + ': Please provide a verb in past participle')
        else:
            answer = st.text_input('Word ' + str(word_index) + ': Please provide a verb in 3rd person singular (ends in \'s\')')

        word_index += 1
        inputs.append(answer)

    submit_button = st.form_submit_button(label="Submit Words") # Creating a submission button

# Merging the words back into the Mad Libs story

story_text = [] # Creating a placeholder to hold plain story text

story_text.append(raw_text[0:indices[0]]) # Saving the first snippet

for i in range(1,int(len(indices)/2)): # Using the '<' and '>' indices to isolate other snippets
    story_text.append(raw_text[(indices[2*i-1]+1):indices[2*i]])

story_text.append(raw_text[indices[-1]+1:]) # Gethring the final snippet

# Creating the final story string
final = '<p style="font-size:26px;">'
snippet_index = 0 # Placeholder index for the snippets

# Incrementally adding snippets and inputs
for input in inputs:
    final = final + story_text[snippet_index] + '<b style=\'color: #21CFDB;\'>' + input + '</b>'
    snippet_index += 1

final = final + story_text[-1] + '</p>' # Completing the story

if submit_button:
    if answer:
        st.markdown(final,unsafe_allow_html=True)

