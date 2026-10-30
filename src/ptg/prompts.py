"""Story openings. Part 3 covers the five required themes; Part 4 holds the Plot-Twist Challenge."""

PROMPTS = [
    # Part 3: decoding-strategy comparison (theme required by the brief in brackets)
    {"id": "P3_mystery", "group": "part3", "theme": "a mystery",
     "text": "The detective entered the abandoned house and noticed that every clock had stopped at "
             "exactly midnight. Suddenly, the telephone rang..."},
    {"id": "P3_discovery", "group": "part3", "theme": "a surprising discovery",
     "text": "While digging in the garden, Ben found an old wooden box. When he opened it, he could "
             "not believe his eyes."},
    {"id": "P3_unusual_character", "group": "part3", "theme": "an unusual character",
     "text": "There once was a little cat who could talk, but she only spoke when it was raining."},
    {"id": "P3_problem", "group": "part3", "theme": "a problem that needs solving",
     "text": "The bridge to the town broke in the storm, and the children could not get to school. "
             "Lily had an idea."},
    {"id": "P3_unexpected_ending", "group": "part3", "theme": "an unexpected ending",
     "text": "Max worked all day to build the biggest sand castle on the beach. He was very proud "
             "of it, but when he came back the next morning,"},
    # Part 4: Plot-Twist Challenge (openings from the brief)
    {"id": "P4_exam", "group": "part4", "theme": "exam paper with tomorrow's answers",
     "text": "A student opened her examination paper and saw that it already contained the answers "
             "to tomorrow's questions."},
    {"id": "P4_robot", "group": "part4", "theme": "robot message from the future",
     "text": "An old robot lived alone in a quiet shed. One morning, it received a message from its "
             "future version."},
    {"id": "P4_detective", "group": "part4", "theme": "detective solves a murder before it happens",
     "text": "The detective solved the murder before the crime had even happened."},
    {"id": "P4_village", "group": "part4", "theme": "village forgets the previous day",
     "text": "One morning, the whole village woke up and discovered that nobody could remember the "
             "previous day."},
    {"id": "P4_letter", "group": "part4", "theme": "letter from 100 years in the future",
     "text": "Sam received a letter addressed to him from one hundred years in the future."},
]


def get_prompts(group=None):
    return [p for p in PROMPTS if group is None or p["group"] == group]
