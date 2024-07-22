# OSCP-machine-generator
A simple python script that will generate 2-6 machine names from the now infamous "Lainkusanagi PEN-200 practice list". This is just for fun. I was finding myself constantly going back to or seareching for the google doc to lookup practice machines and I though this would be a fun project. Please reach out with tips, comments, concerns. I will try to update the machines lists as well. Thanks and enjoy!

1. Clone the repo: ```git clone https://github.com/MAX-P0W3R/OSCP-machine-generator```
2. Move to the dir ```cd OSCP-machine-generator```
3. This basic program will run with ```python3 mockexam.py``` and present you with a few choices. First, which platform would you like to use:

```
Choose a platform: 
1. ProvingGrounds Practice
2. HackTheBox
3. TryHackMe
4. Virtual Hacking Labs
5. ProvingGrounds Play
Enter a number (1-5):
```

Then you will be able to choose how many machines to generate:
```
How many machines would you like to attempt? (2-6):
```

Next you can select OS or ALL for a random selection:  
```
Which trait do you want to filter by? (Linux, Windows, Active Directory, all):
```

Finally the terminal will output the selected machines for practice, Difficulty, OS, and average difficulty:

```NAME OF MACHINE (Difficulty: EASY,MEDIUM,HARD, Trait: WINDOWS,LINUX,ACTIVE DIRECTORY)```

The last line will show an average difficulty for the machines selected based on 1-3 (1=Easy, 2=Intermediate, 3=Hard)

```Average Difficulty Level:____ ```


## Screenshot:
![image](https://github.com/user-attachments/assets/80fbe593-1623-4e67-ba80-03aa146394b4)

Known issues:
##### NOTE: ProvingGrounds Play is only Linux and will error if you select Windows or Active Directory.
##### NOTE: Virtual Hacking Labs is only Linux and Windows and will error if you select Active Directory.
