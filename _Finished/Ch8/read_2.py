import random
import os

# Answers
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
    'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
    'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
    'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
    'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for n in range(35):
    # Opretter ny dictionary der kan pilles ved
    states = list(capitals.keys())
    # Rækkefølgen bliver ændret så den er unik for hver af de 35 gange.
    random.shuffle(states)
    # Opretter fil som hedder "capitalquiz[N's værdi + 1].txt"
    with open("capitalquiz%s.txt" % (n + 1), "w") as quest_txt:
        quest_txt.write("Name:\nDate:\nPeriod:\n")
        quest_txt.write((" " * 20) + "State Capitals Quiz (Form %s)" % (n + 1))
        quest_txt.write("\n\n")
        # Alle stater
        for state_numb in range(50):
            # Ny liste bliver lavet baseret på capitals, men hvor vi får 1 værdi
            correct_answer = capitals[states[state_numb]]
            # Ny liste der kun indeholder values
            wrong_answers = list(capitals.values())
            # Rigtige svar bliver fjernet
            del wrong_answers[wrong_answers.index(correct_answer)]
            # Vi får 3 tilfældige værdier fra listen
            wrong_answers = random.sample(wrong_answers, 3)
            # Vi har nu 4 værdier, 3 forkerte og 1 rigtig, som bliver blandet bagefter
            answer_options = wrong_answers + [correct_answer]
            random.shuffle(answer_options)
            quest_txt.write("%s. What is the capital of %s?\n" % (state_numb + 1, states[state_numb]))
            for i in range(4):
                quest_txt.write("     %s. %s\n" % ("ABCD"[i], answer_options[i]))
                quest_txt.write("\n")
            #### Valgt ikke at lave et answer sheet af ren dovenskab.
            # Write the answer key to a file.
            # answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
