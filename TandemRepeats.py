# Write a Python program to determine whether or not a DNA sequence consists of
# a (integer) number of (perfect) "tandem" repeats.
#       Test it on sequences:
#           AAAAAAAAAAAAAAAA
#           CACACACACACACAC
#           ATTCGATTCGATTCG
#           GTAGTAGTAGTAGTA
#           TCAGTCACTCACTCAG

# Hint: Is the sequence the same as many (how many?) repetitions of its first
# character? 
# Hint: Is the sequence the same as many (how many?) repetitions of its first
# two characters?


def tandemRepeat(seq):
    length = len(seq)
    #loops through potential repeat lengths
    for i in range(1, length // 2 + 1):
        #checks if length of sequence is divisible by i length of a repeat
        if length % i == 0:
            #saves what is being repeated in the sequence as a new variable
            repeat = seq[:i]
            #repeatedly adds all the repeats together to remake the original sequence
            repeatedSeq = repeat*(length // i)
            #checks to see if the repeats will reamke the sequence or not
            if repeatedSeq == seq:
                #if the repeats remake the sequence, returns True
                return True
    #if the repeats do not remake the sequence, returns False
    return False


# all sequences to check
seq = 'AAAAAAAAAAAAAAAA'
#seq = 'CACACACACACACAC'
#seq = 'ATTCGATTCGATTCG'
#seq = 'GTAGTAGTAGTAGTA'
#seq = 'TCAGTCACTCACTCAG'


# print result
containsRepeats = tandemRepeat(seq)
print('Sequence:', seq, 'Sequence contains tandem repeats:',containsRepeats)
