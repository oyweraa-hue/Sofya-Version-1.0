# What is Sofya?
Sofya is a very simple programming language (that was developed from December 2023 and released on 7th October 2025) that was named after a female mathematician called Sofya Kovalevskaya. Sofya was made by Timothy Oywera using another programming language called Python. Sofya was made to enable people to program computers to solve mathematical and scientific problems in a very simple way.

# Why use Sofya?
The answer is quite simple, _Sofya is simpler than most of the other programming languages out there today_. To demonstrate this, let us say that we want to make a simple program that asks the computer user to enter two numbers then the computer should calculate the sum and difference of the two numbers. We can compare how this program looks in _C_, _Python_ and _Sofya_.

# _The C Program_
  #include <stdio.h>
  int main()
  {
    int x, y, sum, difference;
    printf("Input two numbers:\n");
    scanf("%i %i", &x, &y);
    sum = x + y;
    difference = x - y;
    printf("The sum is %i and the difference is %i", sum, difference);
    return 0;
  }

# _The Python Program_
  x = int(input("Input the first number: "))
  y = int(input("Input the second number: "))
  sum = x + y
  difference = x - y
  print(f"The sum is {sum} and the difference is {difference}")

# _The Sofya Program_
  Start
    AskComputerUser "Input the first number:" store the answer in Variable[x]
    AskComputerUser "Input the second number:" store the answer in Variable[y]
    Variable Sum is Variable[x] + Variable[y]
    Variable Difference is Variable[x] - Variable[y]
    Say "The sum is" also say Variable[Sum]
    Say "The difference is" also say Variable[Difference]
  Stop

# How to Set Up Sofya Version 1.0
1. You will need to download the latest version of Python (because Sofya was made using Python). You can access the Python website through this link: https://www.python.org/downloads/
2. On your computer, make a new folder and give it an appropriate name.
3. Put the Sofya 1.0 Interpreter and the Sofya 1.0 User Manual inside the new folder that you created in step 2 (The Sofya 1.0 Interpreter and the Sofya 1.0 User Manual are available in this repository).
4. Make a new Notepad file (if you are using Windows) or a new Text Editor file (if you are using Mac or Macintosh) inside that folder that you created in step 2, and give it an appropriate name.
5. The Notepad file or the Text Editor File, that you made in step 4, is where you will be writing your Sofya code. You can create more Notepad or Text Editor files (in the same folder) if you want to write different Sofya programs. More details about writing Sofya programs is in the Sofya 1.0 User Manual.
6. When you have written a Sofya program, and you are ready to run it, you should go to the Python IDLE (that you downloaded in step 1) and open the Sofya 1.0 Interpreter (from the IDLE) then you can run the Sofya 1.0 Interpreter so that you can run your Sofya program. More details about running Sofya programs is in the Sofya 1.0 User Manual.
7. If you have managed to do all this, you have successfully set up Sofya Version 1.0! You can now refer to the Sofya 1.0 User Manual to start using Sofya.

# Important Notes
1. Sofya is not a case sensitive language.
2. Sofya is designed for people who are beginners in programming, so it is very simple to use.
