# # Think of a documentary, a drama, a comedy, and a dramedy.
# Store the titles of these films in variables.
# Ask the user if they enjoy 1. documentaries 2. dramas 3. comedies.
# If they answer yes to documentaries, display a message recommending the documentary to them.
# If they answer no to documentaries but yes to dramas and comedies, recommend the dramedy.
# If they answer yes to only dramas, recommend the drama.
# If they say yes to only comedies, recommend the comedy.
# If they answer no to all three, recommend a good book instead.

documentary = 'Supersize Me'
drama = 'Prison Break'
comedy = 'Big Bang Theory'
dramedy = 'Friends'

print("1. Do you enjoy documentaries? (yes/no)")

user_preference_doc = input()

print("2. Do you enjoy dramas? (yes/no)")

user_preference_drama = input()

print("3. Do you enjoy comedies? (yes/no)")

user_preference_com = input()


if user_preference_doc == 'yes':
    print("A recommended documentary is {}".format(documentary))
elif user_preference_doc == 'no' and user_preference_drama == 'yes' and user_preference_com == 'yes':
    print("A recommended dramedy is {}".format(dramedy))
elif user_preference_doc == 'no' and user_preference_drama == 'yes' and user_preference_com == 'no':
    print("A recommended drama is {}".format(drama))
elif user_preference_doc == 'no' and user_preference_drama == 'no' and user_preference_com == 'yes':
    print("A recommended comedy is {}".format(comedy))
else:
    print("You may want to read Harry Potter.")
