# Problem Set 4A
# Name: Facundo Frau
# Collaborators: -
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    else:
        permutations = get_permutations(sequence[1:])
        char = sequence[0]
        all_perms = []
        for p in permutations:
            for i in range(len(p) + 1):
                letters = list(p)
                new_letters = letters[:]
                new_letters.insert(i, char)
                all_perms.append(''.join(new_letters))
        return all_perms

if __name__ == '__main__':
   # EXAMPLE 1
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

   # EXAMPLE 2
   example_input = 'xyz'
   print('Input:', example_input)
   print('Expected Output:', ['xyz', 'xzy', 'zxy', 'zyx', 'yxz', 'yzx'])
   print('Actual Output:', get_permutations(example_input))

   # EXAMPLE 3
   example_input = 'qt'
   print('Input:', example_input)
   print('Expected Output:', ['qt', 'tq'])
   print('Actual Output:', get_permutations(example_input))

   # EXAMPLE 4
   example_input = 'k'
   print('Input:', example_input)
   print('Expected Output:', ['k'])
   print('Actual Output:', get_permutations(example_input))