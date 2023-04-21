#Teaching Module to Add a Student to Course
#Rich is used to Style things in Terminal
from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
console = Console()

def Teaching():
        student = Prompt.ask("[bold green]Please input the ID of the Student to Add:  ")
        studentIndex = LinearSearch(students, len(students)-1, Student.GetStudentID, searchTarget)

        course = Prompt.ask("[bold green]Please input the name of the Course:  ")
