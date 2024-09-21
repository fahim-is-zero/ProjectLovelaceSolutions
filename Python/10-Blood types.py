# Input: The person's blood type as a string, and a list of strings with available blood types.
# Output: True if the person can be saved, and false otherwise.


donor = {"O-" : ['O-'],
         "O+" : ['O+', 'O-'],
         "A-" : ['A-', 'O-'],
         "A+" : ['A+', 'A-', 'O+', 'O-'],
         "B-" : ['O-', 'B-'],
         "B+" : ['O+', 'O-', 'B+', 'B-'],
         "AB-" : ['O-', 'AB-', 'A-', 'B-'],
         "AB+" : ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
}


def survive(blood_type, donated_blood):
    needed_blood = donor[blood_type]
    found_match = False
    for blood in donated_blood:
        if blood in needed_blood:
            found_match = True
            break
    return found_match

available_blood = ["O+"]

print("survive : ",survive("AB+", available_blood))
