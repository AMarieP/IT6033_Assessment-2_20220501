from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

#Check if returned Index is Valid
def IndexIsValid(array, index):
    if index == -1:
        return "No Such Record Exists"
    else:
        return array[index]

#Check if Input is Valid
def InputIsValid(field):
    userInput = Prompt.ask("[bold green]" + field)
    if userInput == '':
        print("[bold green]Please enter a Valid " + field)
        InputIsValid(field)
    else:
        return userInput

#Check if Campus is Valid
def CampusIsValid():
    campusOptions = Text("""Please Choose Campus:
Wellington (W)
Auckland(A)
ChristChurch(C)""", justify='left', style='bold green')
    print(campusOptions)
    choiceCampus = Prompt.ask("[bold green]Input Choice:", choices=['W', 'A', 'C'])
    if choiceCampus == 'W':
        choiceCampus = 'Wellington'
        return choiceCampus
    elif choiceCampus == 'A':
        choiceCampus = 'Auckland'
        return choiceCampus
    elif choiceCampus == 'C':
        choiceCampus = 'ChristChurch'
        return choiceCampus
    else:
        print("Campus Choice was Invalid.")
        CampusIsValid()

#Prompt to ask if user wants to Go Again        
def GoAgain(x, y, z):
    print("[bold magenta]DO YOU WANT TO " + y + " [bold magenta]AGAIN?")
    searchAgain = Prompt.ask("[bold green]Please input Y or N", choices=['Y', 'N'])
    if searchAgain == 'Y':
        x()
    elif searchAgain == 'N':
        z()