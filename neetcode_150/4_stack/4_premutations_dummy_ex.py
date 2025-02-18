def generate_permutations(s):
    # Base case: if the string has one character, return it as the only permutation
    if len(s) == 1:
        return [s]

    # List to store all permutations
    permutations = []

    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Generate permutations of the substring without the current character
        remaining = s[:i] + s[i+1:]
        for perm in generate_permutations(remaining):
            # Add the current character to the beginning of each permutation
            permutations.append(char + perm)

    return list(set(permutations))


def generate_permutations_iteratively(s):
    # Start with an empty permutation
    permutations = ['']

    # Iterate over each character in the string
    for char in s:
        new_permutations = []
        # For each existing permutation, insert the current character into all possible positions
        for perm in permutations:
            for i in range(len(perm) + 1):  # Insert at every position
                new_permutations.append(perm[:i] + char + perm[i:])
        permutations = new_permutations  # Update the permutations

    return list(set(permutations))


# Example usage:
string = "ABC"
print(generate_permutations_iteratively(string))

string = "AAB"
print(generate_permutations_iteratively(string))

