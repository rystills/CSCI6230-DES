# Ryan Stillings Cryptography and Network Security I - Homework Assignment 1  
## Project Files  
	This project consists of a few different files, all of which contain python 3 code. The main file, DES.py, is where the main DES algorithm and supporting code are located. This file cannot be run on its own. encryptFile.py provides a command line interface through which to encrypt or decrypt a file using our toy DES implementation. It can be run by entering *python3 encryptFile.py inputFileName outputFileName [options]*, where [options] is either a -e to encrypt the file, or a -d to decrypt the file. Finally, server.py and client.py provide a simple TCP server to demonstrate encrypting a file, sending the encrypted file across a network, and then decrypting the file and printing its contents. These files can be run by entering *python3 server.py* and *python3 client.py* into two separate terminals. After that, server.py will enter a busyloop, and client.py will ask for the name of a text file to send to server.py. The file sampleInput.txt has been provided for testing this functionality.  
## DES Implementation Overview  
	My DES implementation follows the discussed format quite closely, with minor differences resulting from my method of implementation in Python 3. To that end, a few helper methods were included to simplify the process of storing and manipulating bits as lists of booleans. The methods tobits and frombits are responsible for converting from a string to a list of bits and vice versa. The method xor provides a standard exclusive or operation on two lists of bits. Finally, the methods encrypt and decrypt serve as entry points to the main DES algorithm, feeding the provided data to the algorithm 8 bits at a time.  
	As for the main DES method, each step in the algorithm is denoted by a numbered comment explaining the step that we are performing, each separated by a blank line. the first thing we are greeted with here is a number of constants containing the permutation orders used at various points in the algorithm, as well as the s-boxes S0 and S1. Moving on we have the F function, which is stored as an internal method as it will never be used outside of the context of DES. Most of the instructions in F are simple to follow, with the exception of step 4. In step 4, we index into S0 and S1 by concatenating bits 1 and 4 and bits 2 and 3 to get our index values. As we are storing our bits in lists for the sake of simplicity, we simulate 2-bit concatenation by multiplying the value of the first bit by 2. The value stored in the S-box is then converted from an integer to a binary value, with padding applied to convert 0 into 00, and 1 into 01. Finally, this value is turned back into a 2-value list to be used during the proceeding recombination step. It should be noted that in step 5 we perform recombination and permutation at the same time, which is why we see an in-line ternary conditional and 1/2 array length index offsetting. This pattern is a bit confusing at first, but simplifies our work overall and is used throughout this DES implementation. Not much needs to be said about the DES algorithm itself; as mentioned previously, the code closely follows the format covered in our notes, with each action numbered and commented to improve readability.  
## Areas of Potential Improvement  
	As Python is a language with which I am quite comfortable, it was a good choice for this task. However, there are undoubtedly areas where this code could be improved in the future. The most obvious performance loss comes from using lists to represent bit arrays. I made the choice to use lists for this as they are easy to manipulate and convert to/from other data structures. However, it would be more efficient to use a closer to the metal data structure which directly operates on bits / supports bit manipulation operators. That would also eliminate the need to manually define exclusive or, bit shifting, etc.. Also, I made the decision to store permutations as they were defined in our notes; while this minimized the risk of a difficult to spot type, it also meant that I had to manually offset these index lookups by 1 in my code. If this code was to be expanded on in the future, those lists should probably be 0 indexed to simplify things, and remove a number of -1's from my code. 