"""!
Many examples of finding patterns with REGEX
"""

import re

def basic_regex():
    """
    Hurtig simpel regex
    """
    phonenumber_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    phonenumb = phonenumber_regex.search("My number is 415-555-4242.")
    print(f"Phone number found: '{phonenumb.group()}'")

def regex_grouping():
    """
    Gruppering af data der bliver fanget i regex
    """
    grouping_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = grouping_regex.search("My number is 415-555-4242.")
    print(mo.group(1))
    print(mo.group(2))
    print(mo.group(0))

def piping_regex():
    """
    Matching multiple groups with the pipe
    """
    pipe_regex = re.compile(r'Batman|Jared Leto')
    mo1 = pipe_regex.search("Batman and Jered Leto")
    print(mo1.group())
    mo2 = pipe_regex.search("Jared Leto and Batman")
    print(mo2.group())
    bat_regex = re.compile(r'Bat(man|mobile|copter|bat|parents)')
    mo3 = bat_regex.search(f"Batman losts his Batparents.")
    print(mo3.group())
    print(mo3.group(1))

def optional_matching():
    """
    Optional Matching with the Question Mark
    """
    question_mark = re.compile(r"Bat(wo)?man")
    qm1 = question_mark.search("The adventures of Batman")
    qm2 = question_mark.search("The adventures of Batwoman")
    print(qm1.group(), qm2.group()) 

def repeating_regex():
    """
    Matching one or more with the plus
    """
    plus_regex = re.compile(r"Bat(wo)+man")
    pl1 = plus_regex.search("The adventures of Batwowowowowowowowowowowowowoman")
    print(pl1.group())

def repetition_regex():
    """
    Matchin specific repetitions with curly brackets
    """
    haha_regex = re.compile(r'(Ha){3}') # Finder "HaHaHa"
    haha_regex = re.compile(r'(Ha){,3}') # Finder 'Ha', 'HaHa,' 'HaHaHa'
    haha_regex = re.compile(r'(Ha){3,}') # Finder 'HaHaHa', 'HaHaHaHa', osv.
    haha_regex = re.compile(r'(Ha){3,5}') # Finder HaHaHa, HaHaHaHa, og HaHaHaHaHa 

def greedy_regex():
    """
    Greedy and nongreedy matching
    """
    greedy_ha_regex = re.compile(r"(Ha){3,5}")
    gh1 = greedy_ha_regex.search("HaHaHaHaHa")  # Output HaHaHaHaHa
    print(gh1.group())
    nongreedy_ha_regex = re.compile(r"(Ha){3,5}?")
    gh2 = nongreedy_ha_regex.search("HaHaHaHaHa") # Output HaHaHa
    print(gh2.group())

def findall_regex():
    phonenumber_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
    print(phonenumber_regex.findall("Cell: 415-555-9999 work: 212-555-0000"))

def character_class():
    """
    Character classes
    """
    # any numeric digit+, space characters, word characters
    xmas_regex = re.compile(r'\d+\s\w+')
    print(xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, \
                            6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

def my_character_class():
    """
    Making your own character classes
    """
    vowel_regex = re.compile(r'[aeiouAEIOU]')
    print(vowel_regex.findall("Robocop eats baby food. BABY GOOD!"))
    consonant_regex = re.compile(r'[^aeiouAEIOU]') # ^ er det samme som !=
    print(consonant_regex.findall("Robocop eats baby food. BABY GOOD!"))

def caret_and_dollar_regex():
    """
    ^ is for beginning, $ is for end
    """
    hello_regex = re.compile(r"^Hello")
    print(hello_regex.search("Hello world"))
    ending_number_regex = re.compile(r"\d$")
    print(ending_number_regex.search("I am glad to be alive"))
    print(ending_number_regex.search("I am glad to be deadmau5"))

    all_numbers_regex = re.compile(r'^\d+$')
    print(all_numbers_regex.search("12345678910"))
    print(all_numbers_regex.search("123456aaaaAAAA78910"))

def wildcard_regex():
    """Getting everything that matches.
    period (.) is used instead of the asterisk (*)
    """
    at_regex = re.compile(r'.at')
    print(at_regex.findall("That cat in the hat sat on the flat mat."))

def dot_star_regex():
    """
    Everything, but stops at newline 
    """
    name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
    mo = name_regex.search("First Name: Dwayne The Last Name: Rock Johnson")
    print(mo.group(1))
    print(mo.group(2))
    def non_greedy_regex():
        """
        Non-greedy

        Returns:
            <To serve man>
        """
        nongreedy_regex = re.compile(r'<.*?>')
        mo = nongreedy_regex.search("<To serve man> for dinner.>")
        print(mo.group())
    def greedy_regex():
        """Output = <To serve man> for dinner>
        """
        greedy_regex = re.compile(r'<.*>')
        mo = greedy_regex.search("<To serve man> for dinner.>")
        print(mo.group())
    non_greedy_regex()
    greedy_regex()

def newline_regex():
    """
    Matches everything BUT newline
    
    Returns:
        Output is "I thought what I'd do was\nI'd pretend to be one\nof those deaf-mutes"
    """
    newline_regex = re.compile('.*', re.DOTALL)
    print(newline_regex.search("I thought what I'd do was\nI'd pretend to be one\nof those deaf-mutes").group())
    def no_newline_regex():
        """Output = "I thought what I'd do was"
        """
        no_newline_regex = re.compile('.*')
        print(no_newline_regex.search("I thought what I'd do was\nI'd pretend to be one\nof those deaf-mutes"))
    no_newline_regex()

def case_insensitive_regex():
    """only looks for the characters, not if they match in case
    """
    robo_regex = re.compile(r'robocop', re.I)
    print(robo_regex.findall("RoBoCop, rooooobert, Robocop, roboacab, robocop, rObOcoP"))

def substitute_strings():
    """Matches are changed
    """
    regex = re.compile(r'Agent \w+')
    print(regex.sub('REDACTED', 'Agent Smith met with Agent Doe to beat up a minority.'))
    agent_name = re.compile(r'Agent (\w)\w*')
    print(agent_name.sub(r'\1****', 'Agent Smith met with Agent Doe to beat up a minority.'))

substitute_strings()