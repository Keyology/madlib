
# Acepts noun plural input and saves it in to variable
noun_plural = input('Please enter a Noun (Plural)')

# Acepts Occupation input and saves it in to variable 
Occupation = input('Please enter an occupation')

# Acepts Animal Plural input and saves it in to variable 
Animal_Plural = input('Please enter a Animal (Plural)')

# Acepts place input and saves it in to variable 
place = input('Please enter a place')

# Acepts verb input and saves it in to variable 
verb = input('Please enter a verb')

# Acepts noun  input and saves it in to variable 
noun = input('Please enter a noun')

# result variable stores string that will concatenate user input
result = "In the book War of the {}, the main character is an anonymous {} who records the arrival of {} in {}. Needless to say, havoc reigns as the {} continue to {} everything in sight, until they are killed by the common ?."

# prints final result to user
print(result.format(noun_plural, Occupation, Animal_Plural, place, verb, noun))
