# OSCP-machine-generator
A simple python script that will generate 2-6 machine names from the now infamous "Lainkusanagi PEN-200 practice list".

This basic program will run with ```python3 mockexam.py``` and present you with a few choices. First, which platform would you like to use:

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

Finally the terminal will output the selected machines for practice and :
```
Selected items:
**NAME OF MACHINE** (Difficulty: **EASY,MEDIUM,HARD**, Trait: **WINDOWS,LINUX,ACTIVE DIRECTORY**)
```
## Screenshot:
![image](https://github.com/user-attachments/assets/c7818b90-be15-4aa0-bc6f-0b531917a977)

Known issues:
##### NOTE: ProvingGrounds Play is only Linux and will error if you select Windows or Active Directory.
##### NOTE: Virtual Hacking Labs is only Linux and Windows and will error if you select Active Directory.
