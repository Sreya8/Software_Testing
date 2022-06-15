# Software_Testing
Software Engineering Assignment 5: Coverage and Differential Testing

## Tools
1. Platform : Pycharm
2. Language : Python2.7 , Python3.7
3. Dependencies : unittest

## Note: Target Project 1 uses python2 and Target projects 2 and 3 uses python3

## Execution
>````git clone https://github.com/Sreya8/Software_Testing.git````

Navigate to the ````Software_Testing```` directory.

## Target Project 1
https://github.com/thomdixon/pysha2/tree/master/sha2:
1. From the ````Software_Testing```` directory navigate to the ````pysha2```` directory.
2. Run the command ````python2 -m unittest sha256_Test_1````
3. Please Note: Do not add the .py extension. python2 does not support the .py extension in the terminal.

## Target Project 2
https://github.com/keanemind/python-sha-256:
1. From the ````Software_Testing```` directory navigate to the ````python-sha-256```` directory.
2. Run the command ````python3 -m unittest sha256_Test_2.py````

## Target Project 3
https://github.com/Akif-G/sha256/blob/master/sha256.py:
1. From the ````Software_Testing```` directory navigate to the ````sha256```` directory.
2. Run the command ````python3 -m unittest sha256_Test_3.py````

# Results
## Target Project 1
Target project 1
https://github.com/thomdixon/pysha2/tree/master/sha2
<b><i>Python Version 2.7</i> </b></br>

### Test Cases

Test Case 1: First we initialize a new sha256 object with the String ````My Obj````. 
This test case tries to update the value of the object with a new String value ````New String````
>````Coverage : 44%````
</br>

Test Case 2: Here we pass an empty String as the value to be updated. The function must just return without updating the value.
>````Coverage : 45%````
</br>

Test Case 3: Here we pass an integer value to be updated. If the input parameter is not a String we must get a Type Error.
>````Coverage : 47%````
</br>

Test Case 4: Here we try to copy one sha256 object into a new object.
>````Coverage : 97%````
</br>

<img width="390" alt="1_2" src="https://user-images.githubusercontent.com/54528672/173066528-857008d4-d43a-47e5-9825-822c5cc3247c.png">

## Testing Result 2
Target Project 2
https://github.com/keanemind/python-sha-256

### Test Cases
Case 1 Checks whether the generated hash value for a string is equivalent to the given hash value
>````Coverage 94%````
</br>

Case 2 check the equality between the given hash value and generated hash value for a given Byte input  
>````Coverage 96%````
</br>

Case 3 Checks for TypeError  when input other than string and byte is passed
>````Coverage 98%````
</br>

<b><i>Python Version 3.7</i> </b></br>

<img width="430" alt="2_1" src="https://user-images.githubusercontent.com/54528672/173066553-31a674b2-ef47-435e-90e1-74bb27e01a5d.png">

## Testing Result 3
Target Project 3
https://github.com/Akif-G/sha256/blob/master/sha256.py
### Tests Cases
Case 1 Checks whether the generated hash value is not equal to TypeError
</br>

Case 2 Checks for the Type Error raised when input other than String is passed
</br>

<b><i>Python Version 3.7</i> </b></br>

<img width="437" alt="3_1" src="https://user-images.githubusercontent.com/54528672/173066616-1d6d67c4-b527-4940-8d81-3fa6cd6211b9.png">
