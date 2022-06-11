# Software_Testing
Software Engineering Assignment 5: Coverage and Differential Testing

## Testing Result 1

### Test Cases
Case 1 checks whether the update function recieves input value as string using assertEqual 
>````Coverage : 44%````
</br>

Case 2  checks whether an empty string is passed to update function using
assertEquals 
>````Coverage : 45%````
</br>

Case 3 Checks whether a TyperError is raised when an input other than string is passed or not
>````Coverage : 47%````
</br>

Case 4 Checks for equality between object copied using deepcopy and the object
>````Coverage : 97%````
</br>

<b><i>Python Version 2.7</i> </b></br>

<img width="390" alt="1_2" src="https://user-images.githubusercontent.com/54528672/173066528-857008d4-d43a-47e5-9825-822c5cc3247c.png">

## Testing Result 2

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

### Tests Cases
Case 1 Checks whether the generated hash value is not equal to TypeError
</br>

Case 2 Checks for the Type Error raised when input other than String is passed
</br>

<b><i>Python Version 3.7</i> </b></br>

<img width="437" alt="3_1" src="https://user-images.githubusercontent.com/54528672/173066616-1d6d67c4-b527-4940-8d81-3fa6cd6211b9.png">
