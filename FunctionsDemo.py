"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main1():
    print()
    print("Happy birthday to you!" )
    print("Happy birthday to you!" )
    print("Happy birthday, dear Fred...")
    print("Happy birthday to you!")
    print()


def happy():
    print("happy birthday to you!")


""" IPO happy()
Input(s): none
Process: prints redundant parts of happy birthday song
Output: prints to terminal screen
"""

def main2():
    print()
    happy()
    happy()
    print("happy birthday dear Fred...")
    happy()
    print()


#generalize for any person

""" IPO happyBday()
Input(s): name
Process: prints verses of bday song
Output: prints to terminal screen
"""
def happyBday(name):
    print("Happy birthday, dear ", name, "...", sep="")

def main3():  
    print()
    happy()
    happy()
    happyBday("Joe")
    happy()
    print()

# combine song into function
""" IPO bdaySong()
Input(s): name
Process: prints bday song
Output: prints to terminal screen
"""
def bdaySong(name):
    happy()
    happy()
    happyBday(name)
    happy()
    print()

def main4():
    print()
    bdaySong("Fred")
    bdaySong("Joe")
    bdaySong("abe")
    print()


main4()    