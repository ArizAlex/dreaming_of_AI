import collections
import math

############################################################
# Problem 3a

def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return sorted(text.split())[-1]
    # END_YOUR_CODE

############################################################
# Problem 3b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt((loc1[1]-loc2[1])**2+(loc1[0]-loc2[0])**2)
    # END_YOUR_CODE

############################################################
# Problem 3c

def mutateSentences(st):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the orignal sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    done, length = [], len(st.split())
    def alike(num):
        return [i for i,w in enumerate(st.split()) if st.split()[num] == w]
    def fun(i,branch_at_i):
        if len(branch_at_i) == length:
            done.append(branch_at_i)
            return ''
        if i == length-1:
            return ''
        al = alike(i)
        if len(al)>1:
            for j in al:
                fun(j+1,branch_at_i+f'{j+1}')
            return ''
        fun(i+1,branch_at_i+f'{i+1}')
    [fun(i,f'{i}') for i in range(length)]
    return list({' '.join(st.split()[int(i)] for i in comb) for comb in done})

############################################################
# Problem 3d

def sparseVectorDotProduct(a, b):
    """
    Given two sparse vectors |a| and |b|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    ref = a if len(a)>len(b) else b
    return sum(a[key]*b[key] for key in ref)
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(a, scale, b):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    ref = a if len(a)>len(b) else b
    for key in ref:
        a[key] += scale*b[key]
    # END_YOUR_CODE

############################################################
# Problem 3f

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    return {w for w in text.split() if text.count(w) == 1}
    # END_YOUR_CODE

############################################################
# Problem 3g

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama'.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 19 lines of code, but don't worry if you deviate from this)
    def isPal(t):
        if len(t) == 1:
            return True
        if t[0] == t[-1] and isPal(t[1:-1]):
            return True
        return False
    for size in range(len(text),0,-1):
        for c in combinations(s,size):
            if isPal(''.join(l for l in c)):
                return ''.join(l for l in c)
    # END_YOUR_CODE
