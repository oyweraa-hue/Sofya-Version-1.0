# Sofya was first created by Timothy Oywera on December 2023 and the official first version of Sofya was released on February 2026

'''
============================================
Important things to note about this program
============================================
--> In this program, there is a function called "lexer()". The lexer is a function that gets words from a Sofya file, and it is able to know the meaning of each word.
--> After the lexer does this, those words are put in another function called "parser()". The parser is the function that does the instructions that the Sofya Programmer has given the computer.
--> When this program was being made for the first time, there were some mistakes that were not noticed but those errors were fixed (but they were not fixed completely, but they were only fixed in a way so that the program can still be able to run).
--> However, even if the program can still run properly, you will notice that some things are a bit unusual in this program, for example:

      * When you make an If Statement range in Sofya like, "If Variable[a] is from 10 to 50 then", the lexer will arrange it like this: "If Variable[a] is from 10 then 50" (So, the lexer will ignore the word "to" and it will rearrange some things).
      * When you make an If Statement range in Sofya like, "If Variable[a] is between 10 and 50 then", the lexer will arrange it like this: "If Variable[a] is between 10 then 50" (So, the lexer will ignore the word "and" and it will rearrange some things).
      * When you make an If Statement in Sofya like, "If Variable[a] > 40 then" (Comparing a variable and a number), the lexer will arrange it like this: "If Variable[a] > then 40" (So, the lexer will rearrange some things).
      * When you make an If Statement in Sofya like, "If Variable[a] > 1/3 then" (Comparing a variable and an expression), the lexer will arrange it like this: "If Variable[a] > then 1/3" (So, the lexer will rearrange some things).
      * There could also be some other areas in the program where the lexer rearranges some words.

--> If you would like, you can fix these small errors, but it is advisable that since these bugs are in many places in the program (and the program is very big) it would be very hard to remove these bugs, so it would be better to just leave the code the way it is.
--> Apart from those small bugs the rest of the program is okay.

'''

import tkinter
import tkinter.font as TkFont
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import sys, os

def find_resource_path(path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, path)
    else:
        return path


IDLE = Tk()
DesiredFont = TkFont.Font(family="Courier New", size=10)
IDLE.title("Sofya Version 1.0 IDLE")
icon_photo_path = find_resource_path("Sofya IDLE Logo.png")
IDLE.iconphoto(True, PhotoImage(file=icon_photo_path))
file_path = ""
tokens = []
symbol_table = {}
user_input = ""
wait_var = tkinter.IntVar()


def read_file(filename):
    data = open(filename, "r").read()
    return data


def evalExpression(expression):
    return eval(str(expression))


def doASSIGN(varname, varvalue):
    try:
        symbol_table[varname[4:]] = varvalue.strip()
    except AttributeError:
        symbol_table[varname[4:]] = varvalue


def getVARIABLE(varname):
    varname = varname[4:]
    if varname in symbol_table:
        return symbol_table[varname]
    else:
        return f">>> Variable Error: {varname} is a variable that does not exist!"


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    try:
        path = askopenfilename(filetypes=[("Sofya Files", "*.sofya")])
        with open(path, "r") as file:
            code = file.read()
            editor.delete("1.0", END)
            editor.insert("1.0", code)
            set_file_path(path)
            file_name_bar.delete("1.0", END)
            file_name_bar.insert("1.0", f"Name of Current File: {file_name_extracter(file_path)}")
            code_output.delete("1.0", END)
    except FileNotFoundError:
        print("The error was handled successfully!")

def create_new_file():
    if file_path != "":
        with open(file_path, "w") as file:
            code = editor.get("1.0", END)
            file.write(code)
            editor.delete("1.0", END)
            code_output.delete("1.0", END)
    else:
        code_output.delete("1.0", END)
        messagebox.showinfo(title = "New File Error", message = "You are already using a new file!")
    set_file_path("")
    file_name_bar.delete("1.0", END)
    file_name_bar.insert("1.0", f"Name of Current File: {file_name_extracter(file_path)}")


def save_file():
    try:
        if file_path == "":
            path = asksaveasfilename(filetypes=[("Sofya Files", "*.sofya")])
        else:
            path = file_path
        with open(path, "w") as file:
            code = editor.get("1.0", END)
            file.write(code)
            set_file_path(path)
            file_name_bar.delete("1.0", END)
            file_name_bar.insert("1.0", f"Name of Current File: {file_name_extracter(file_path)}")
            code_output.delete("1.0", END)
    except FileNotFoundError:
        print("The error was handled successfully!")


def static_variable_increment(static_variable_name, increment_value):
    static_variable_name = static_variable_name[4:]
    if static_variable_name in symbol_table:
        symbol_table[static_variable_name] = float(float(symbol_table[static_variable_name]) + increment_value)
        return "Successfully incremented"
    else:
        code_output.insert(END, f">>> Variable Error: {static_variable_name} is a variable that does not exist!\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED")
        return "Increment not successful"


def static_variable_decrement(static_variable_name, decrement_value):
    static_variable_name = static_variable_name[4:]
    if static_variable_name in symbol_table:
        symbol_table[static_variable_name] = float(float(symbol_table[static_variable_name]) - decrement_value)
        return "Successfully decremented"
    else:
        code_output.insert(END, f">>> Variable Error: {static_variable_name} is a variable that does not exist!\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED")
        return "Decrement not successful"


def static_variable_multiplication(static_variable_name, multiplication_value):
    static_variable_name = static_variable_name[4:]
    if static_variable_name in symbol_table:
        symbol_table[static_variable_name] = float(float(symbol_table[static_variable_name]) * multiplication_value)
        return "Successfully multiplied"
    else:
        code_output.insert(END, f">>> Variable Error: {static_variable_name} is a variable that does not exist!\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED")
        return "Multiplication not successful"


def static_variable_division(static_variable_name, division_value):
    static_variable_name = static_variable_name[4:]
    if static_variable_name in symbol_table:
        symbol_table[static_variable_name] = float(float(symbol_table[static_variable_name]) / division_value)
        return "Successfully divided"
    else:
        code_output.insert(END, f">>> Variable Error: {static_variable_name} is a variable that does not exist!\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED")
        return "Division not successful"


def static_variable_exponentiation(static_variable_name, exponent_value):
    static_variable_name = static_variable_name[4:]
    if static_variable_name in symbol_table:
        symbol_table[static_variable_name] = float(float(symbol_table[static_variable_name]) ** exponent_value)
        return "Successfully exponentiated"
    else:
        code_output.insert(END, f">>> Variable Error: {static_variable_name} is a variable that does not exist!\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED")
        return "Exponentiation not successful"


def static_variable_flooring(static_variable_name, floor_value):
    static_variable_name = static_variable_name[4:]
    if static_variable_name in symbol_table:
        symbol_table[static_variable_name] = float(float(symbol_table[static_variable_name]) // floor_value)
        return "Successfully floored"
    else:
        code_output.insert(END, f">>> Variable Error: {static_variable_name} is a variable that does not exist!\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED")
        return "Flooring not successful"


def static_variable_modulation(static_variable_name, modulation_value):
    static_variable_name = static_variable_name[4:]
    if static_variable_name in symbol_table:
        symbol_table[static_variable_name] = float(float(symbol_table[static_variable_name]) % modulation_value)
        return "Successfully modulated"
    else:
        code_output.insert(END, f">>> Variable Error: {static_variable_name} is a variable that does not exist!\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED")
        return "Modulation not successful"


def gui_input(prompt):
    code_output.insert(END, prompt + " {Please answer this question in the input box}\n")
    wait_var.set(0)
    code_output.wait_variable(wait_var)
    user_input = input_box.get("1.0", END).strip()
    input_box.delete("1.0", END)
    user_input = user_input.replace("\n", "")
    user_input = user_input.replace("\t", "")
    code_output.insert(END, f"> What you typed in the input box is: {user_input}\n\n")
    user_input = user_input.replace(",", "")
    user_input = user_input.upper()
    return user_input


def on_enter(event):
    wait_var.set(1)


def file_name_extracter(FilePath):
    FilePath = str(FilePath)
    if FilePath == "":
        return "**File is not named yet**"
    else:
        index = -1
        while FilePath[index] != "/":
            index = index - 1
            if FilePath[index] == "/":
                return FilePath[index + 1:]


def exit_IDLE():
    exit()


def lexer(filecontents):
    token = ""
    state = 0
    string = ""
    isexpr = 0
    expr = ""
    varstarted = 0
    var = ""
    var_recall = 0
    comment_recall = 0
    comparison_sign = ""
    comparison_sign_started = False
    variable_line = False
    writting_line = False
    curly_brace_index_list = []

    filecontents = list(filecontents)
    #print(filecontents)
    for character in filecontents:
        token = token + character
        token = token.upper()
        if token == "START THIS PROGRAM" and state == 0:
            tokens.append("START")
            token = ""
        elif token == " " and comparison_sign_started == False:
            if varstarted == 1:
                tokens.append("VAR:" + var)
                varstarted = 0
                var = ""
                token = ""
            elif state == 0:
                token = ""
            elif state == 1:
                token = " "
        elif token == "\t":
            token = ""
        elif token == "\n" or token == "TO" or token == "AND" and state == 0:
            if expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                if token == "\n":
                    if variable_line == True:
                        tokens.append("<<new line character>>")
                        variable_line = False
                    elif writting_line == True:
                        tokens.append("<<new line character>>")
                        writting_line = False
                isexpr = 0
                expr = ""
            elif expr != "" and isexpr == 0:
                tokens.append("NUM:" + expr)
                if token == "\n":
                    if variable_line == True:
                        tokens.append("<<new line character>>")
                        variable_line = False
                    elif writting_line == True:
                        tokens.append("<<new line character>>")
                        writting_line = False
                expr = ""
            elif expr == "" and token == "TO":
                tokens.append("TO")
            elif expr == "" and token == "AND":
                tokens.append("AND")
            elif expr == "" and token == "\n" and writting_line == True:
                tokens.append("<<new line character>>")
                writting_line = False
            elif expr == "" and token == "\n" and variable_line == True:
                tokens.append("<<new line character>>")
                variable_line = False
            token = ""
        elif token == "IS" and state == 0:
            tokens.append("EQUALS")
            token = ""
        elif token == "VARIABLE " and state == 0:
            variable_line = True
            if varstarted == 0:
                varstarted = 1
            token = ""
        elif varstarted == 1:
            var = var + token
            token = ""
        elif token == "WRITE" and state == 0:
            writting_line = True
            tokens.append("WRITE")
            token = ""
        elif token == "ON THE SCREEN" and state == 0:
            token = "" # Here, the words "On the screen" have been ignored to make the program less complicated
        elif tokens != [] and tokens[-1] == "AND" and token == "ALSO WRITE" and state == 0:
            del tokens[-1]
            tokens.append("&")
            token = ""
        elif token == "BETWEEN" and state == 0:
            tokens.append("BETWEEN")
            token = ""
        elif token == "FROM" and state == 0:
            tokens.append("FROM")
            token = ""
        elif token == "=" and state == 0 and comparison_sign_started == False:
            comparison_sign_started = True
            comparison_sign = comparison_sign + token
            token = ""
        elif token == ">" and state == 0 and comparison_sign_started == False:
            comparison_sign_started = True
            comparison_sign = comparison_sign + token
            token = ""
        elif token == "<" and state == 0 and comparison_sign_started == False:
            comparison_sign_started = True
            comparison_sign = comparison_sign + token
            token = ""
        elif comparison_sign_started == True:
            if token == "/" or token == "=" or token == "O" or token == "R":
                comparison_sign = comparison_sign + token
                token = ""
            elif token == " ":
                token = ""
            elif token == "0" or token == "1" or token == "2" or token == "3" or token == "4" or token == "5" or token == "6" or token == "7" or token == "8" or token == "9" or token == ".":
                expr = expr + token
                token = ""
                if comparison_sign == "=":
                    tokens.append("IS_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "=/=":
                    tokens.append("IS_NOT_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == ">":
                    tokens.append("IS_GREATER_THAN")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "<":
                    tokens.append("IS_LESS_THAN")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == ">OR=":
                    tokens.append("IS_GREATER_THAN_OR_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "<OR=":
                    tokens.append("IS_LESS_THAN_OR_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
            elif token == "+" or token == "-" or token == "(":
                isexpr = 1
                expr = expr + token
                token = ""
                if comparison_sign == "=":
                    tokens.append("IS_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "=/=":
                    tokens.append("IS_NOT_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == ">":
                    tokens.append("IS_GREATER_THAN")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "<":
                    tokens.append("IS_LESS_THAN")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == ">OR=":
                    tokens.append("IS_GREATER_THAN_OR_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "<OR=":
                    tokens.append("IS_LESS_THAN_OR_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
            elif token == "\"" or token == " \"":
                token = ""
                state = 1
                if comparison_sign == "=":
                    tokens.append("IS_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "=/=":
                    tokens.append("IS_NOT_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == ">":
                    tokens.append("IS_GREATER_THAN")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "<":
                    tokens.append("IS_LESS_THAN")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == ">OR=":
                    tokens.append("IS_GREATER_THAN_OR_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "<OR=":
                    tokens.append("IS_LESS_THAN_OR_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
            else:
                if comparison_sign == "=":
                    tokens.append("IS_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "=/=":
                    tokens.append("IS_NOT_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == ">":
                    tokens.append("IS_GREATER_THAN")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "<":
                    tokens.append("IS_LESS_THAN")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == ">OR=":
                    tokens.append("IS_GREATER_THAN_OR_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
                elif comparison_sign == "<OR=":
                    tokens.append("IS_LESS_THAN_OR_EQUAL_TO")
                    comparison_sign_started = False
                    comparison_sign = ""
        elif token == "END THIS IF STATEMENT" and state == 0:
            tokens.append("ENDIF")
            token = ""
        elif token == "IF" and state == 0:
            tokens.append("IF")
            token = ""
        elif token == "OTHERWISE" and state == 0:
            token = ""  # Here, the word "otherwise" has been ignored to make the program less complicated
        elif token == "GET OUT OF THE LOOP" and state == 0:
            tokens.append("BREAK_THE_LOOP")
            token = ""
        elif token == "ANYTHING" and state == 0:
            tokens.append("ANYTHING")
            token = ""
        elif token == "ELSE" and state == 0:
            tokens.append("ELSE")
            token = ""
        elif token == "AFTER" and state == 0:
            tokens.append("AFTER")
            token = ""
        elif token == "BEFORE" and state == 0:
            tokens.append("BEFORE")
            token = ""
        elif token == "THEN" and state == 0:
            tokens.append("THEN")
            token = ""
        elif token == "ASK THE COMPUTER USER" and state == 0:
            tokens.append("INPUT")
            token = ""
        elif tokens != [] and tokens[-1] == "AND" and token == "STORE THE ANSWER IN" and state == 0:
            del tokens[-1]
            tokens.append("STOREIN")
            token = ""
        elif token == "INCREASE" and state == 0:
            tokens.append("INCREASE")
            token = ""
        elif token == "DECREASE" and state == 0:
            tokens.append("DECREASE")
            token = ""
        elif token == "MULTIPLY" and state == 0:
            tokens.append("MULTIPLY")
            token = ""
        elif token == "DIVIDE" and state == 0:
            tokens.append("DIVIDE")
            token = ""
        elif token == "DO MODULUS FOR" and state == 0:
            tokens.append("MODULATE")
            token = ""
        elif token == "DO FLOORING FOR" and state == 0:
            tokens.append("FLOOR")
            token = ""
        elif token == "DO EXP FOR" and state == 0:
            tokens.append("EXPONENTIATE")
            token = ""
        elif token == "BY" or token == "USING" and state == 0:
            tokens.append("BY")
            token = ""
        elif token == "DO THIS" and state == 0:
            tokens.append("REPEAT")
            curly_brace_index_list.append("START OF A DO THIS UNTIL LOOP")
            token = ""
        elif token == "UNTIL" and state == 0:
            tokens.append("UNTIL")
            token = ""
        elif token == "INFINITY" and state == 0:
            tokens.append("THE")
            tokens.append("LOOP")
            tokens.append("BREAKS")
            token = ""
        elif token == "MAKE THIS NESTED DO THIS UNTIL LOOP" and state == 0:
            curly_brace_index_list.append("NESTED DO THIS UNTIL LOOP")
            token = "" # Here, the words "Make this nested do this until loop" have been ignored to make the program less complicated
        elif token == "MAKE THIS NESTED IF STATEMENT" and state == 0:
            tokens.append("NESTED_IF")
            curly_brace_index_list.append("NESTED IF STATEMENT")
            token = ""
        elif token == "{" and state == 0:
            if curly_brace_index_list != []:
                if curly_brace_index_list[-1] == "START OF A DO THIS UNTIL LOOP":
                    tokens.append("{")
                elif curly_brace_index_list[-1] == "NESTED IF STATEMENT":
                    tokens.append("{")
                elif curly_brace_index_list[-1] == "NESTED DO THIS UNTIL LOOP":
                    token = ""
            else:
                tokens.append("{")
            token = ""
        elif token == "}" and state == 0:
            if curly_brace_index_list != []:
                if curly_brace_index_list[-1] == "START OF A DO THIS UNTIL LOOP":
                    tokens.append("}")
                    del curly_brace_index_list[-1]
                elif curly_brace_index_list[-1] == "NESTED IF STATEMENT":
                    tokens.append("}")
                    del curly_brace_index_list[-1]
                elif curly_brace_index_list[-1] == "NESTED DO THIS UNTIL LOOP":
                    del curly_brace_index_list[-1]
            else:
                tokens.append("}")
            token = ""
        elif token == ";" and state == 0:
            comment_recall = 0
            token = ""
        elif token == "NOTE:" and state == 0:
            if comment_recall == 0:
                comment_recall = 1
            token = ""
        elif comment_recall == 1:
            token = ""
        elif token == "]" and state == 0 and var_recall == 1:
            var = var.strip()
            tokens.append("VAR:" + var)
            var = ""
            var_recall = 0
            token = ""
        elif token == "VARIABLE[" and state == 0:
            if expr != "" and isexpr == 1 and var_recall == 0:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                var_recall = 1
            elif expr == "" and var_recall == 0:
                var_recall = 1
            token = ""
        elif var_recall == 1:
            var = var + token
            token = ""
        elif token == "0" or token == "1" or token == "2" or token == "3" or token == "4" or token == "5" or token == "6" or token == "7" or token == "8" or token == "9" or token == "." and state == 0:
            if state == 1:
                string = string + token
            elif state == 0:
                expr = expr + token
            token = ""
        elif token == "CONSTANT[PI]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(3.14159265358979323846))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(3.14159265358979323846))
            token = ""
        elif token == "CONSTANT[C]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(299792458))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(299792458))
            token = ""
        elif token == "CONSTANT[H]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(evalExpression(str(6.62607015 * 10 ** -34))))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(evalExpression(str(6.62607015 * 10 ** -34))))
            token = ""
        elif token == "CONSTANT[E_O]" or token == "CONSTANT[E_0]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(evalExpression(str(8.854187812813 * 10 ** -12))))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(evalExpression(str(8.854187812813 * 10 ** -12))))
            token = ""
        elif token == "CONSTANT[G]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(evalExpression(str(6.6743015 * 10 ** -11))))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(evalExpression(str(6.6743015 * 10 ** -11))))
            token = ""
        elif token == "CONSTANT[K_E]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(evalExpression(str(8.987551792314 * 10 ** 9))))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(evalExpression(str(8.987551792314 * 10 ** 9))))
            token = ""
        elif token == "CONSTANT[G_E]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(9.80665))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(9.80665))
            token = ""
        elif token == "CONSTANT[ATM]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(101325))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(101325))
            token = ""
        elif token == "CONSTANT[M_E]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(evalExpression(str(9.109383701528 * 10 ** -31))))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(evalExpression(str(9.109383701528 * 10 ** -31))))
            token = ""
        elif token == "CONSTANT[M_P]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(evalExpression(str(1.6726219236951 * 10 ** -27))))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(evalExpression(str(1.6726219236951 * 10 ** -27))))
            token = ""
        elif token == "CONSTANT[M_N]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(evalExpression(str(1.6749274980495 * 10 ** -27))))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(evalExpression(str(1.6749274980495 * 10 ** -27))))
            token = ""
        elif token == "CONSTANT[M_P:M_E]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(1836.1526734311))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(1836.1526734311))
            token = ""
        elif token == "CONSTANT[N_A]" or token == "CONSTANT[L]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(evalExpression(str(6.02214076 * 10 ** 23))))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(evalExpression(str(6.02214076 * 10 ** 23))))
            token = ""
        elif token == "CONSTANT[R]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(8.31446261815324))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(8.31446261815324))
            token = ""
        elif token == "CONSTANT[F]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(96485.3321233100184))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(96485.3321233100184))
            token = ""
        elif token == "CONSTANT[R_E]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(evalExpression(str(2.817940326213 * 10 ** -15))))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(evalExpression(str(2.817940326213 * 10 ** -15))))
            token = ""
        elif token == "CONSTANT[PHI]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(1.61803398874989484820))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(1.61803398874989484820))
            token = ""
        elif token == "CONSTANT[E]" and varstarted == 0 and var_recall == 0 and state == 0:
            if state == 1:
                string = string + token
            elif state == 0 and expr == "":
                tokens.append("CONSTANT:" + str(2.71828182845904523536))
            elif state == 0 and expr != "" and isexpr == 1:
                tokens.append("EXPR:" + expr)
                isexpr = 0
                expr = ""
                tokens.append("CONSTANT:" + str(2.71828182845904523536))
            token = ""
        elif token == "+" or token == "-" or token == "/" or token == "(" or token == ")" and state == 0:
            if state == 1:
                string = string + token
            elif state == 0:
                isexpr = 1
                expr = expr + token
            token = ""
        elif token == "X" and state == 0:
            token = "*"
            isexpr = 1
            expr = expr + token
            token = ""
        elif token == "EXP" and state == 0:
            token = "**"
            isexpr = 1
            expr = expr + token
            token = ""
        elif token == "FLOOR" and state == 0:
            token = "//"
            isexpr = 1
            expr = expr + token
            token = ""
        elif token == "MODULUS" and state == 0:
            token = "%"
            isexpr = 1
            expr = expr + token
            token = ""
        elif token == "\"" or token == " \"":
            token = ""
            if state == 0:
                state = 1
            elif state == 1:
                string = string.strip()
                tokens.append("STRING:" + string)
                string = ""
                state = 0
                token = ""
        elif state == 1:
            string = string + token
            token = ""
        elif token == "STOP THIS PROGRAM" and state == 0:
            tokens.append("STOP")
            token = ""
    return tokens


def parse_checker(tokens_list):
    if "START" in tokens_list and "STOP" in tokens_list:
        return tokens_list
    elif "START" not in tokens_list and "STOP" in tokens_list:
        tokens_list.insert(0, "START")
        return tokens_list
    elif "START" in tokens_list and "STOP" not in tokens_list:
        tokens_list.append("STOP")
        return tokens_list
    else:
        tokens_list.insert(0, "START")
        tokens_list.append("STOP")
        return tokens_list

def array_filler(array, array_instructions): # This function is used to prevent an array from having an Index Error
    instruction_length_array = []

    for instruction in array_instructions:
        instruction_length = len(instruction)
        instruction_length_array.append(instruction_length)

    longest_instruction_length = max(instruction_length_array)

    for counter in range(0, longest_instruction_length, 1):
        array.append("<<place holder>>")

    #print(f"The longest instruction is {longest_instruction_length} words")
    #print(array)
    return array


def get_constant_name(constant_value):
    constant_value = float(evalExpression(constant_value))
    constant_table = {
        3.14159265358979323846: "Pi",
        299792458: "c",
        6.62607015 * 10 ** -34: "h",
        8.854187812813 * 10 ** -12: "E_o",
        6.6743015 * 10 ** -11: "G",
        8.987551792314 * 10 ** 9: "K_e",
        9.80665: "G_E",
        101325: "atm",
        9.109383701528 * 10 ** -31: "M_e",
        1.6726219236951 * 10 ** -27: "M_p",
        1.6749274980495 * 10 ** -27: "M_n",
        1836.1526734311: "M_p:M_e",
        6.02214076 * 10 ** 23: "N_a or L",
        8.31446261815324: "R",
        96485.3321233100184: "F",
        2.817940326213 * 10 ** -15: "R_e",
        1.61803398874989484820: "Phi",
        2.71828182845904523536: "e"
    }
    constant_name = constant_table[constant_value]
    return constant_name


def check_string(string):
    string = str(string)
    index = 0
    string_array = []

    while index < len(string):
        item = string[index]
        item = item.upper()
        if item != " ":
            string_array.append(item)
        index = index + 1
    #print(string_array)

    if "X" in string_array and "1" in string_array and "0" in string_array and "E" in string_array and "P" in string_array:
        index = -1
        try:
            while index >= (-1 * len(string_array)):
                if string_array[index] == "P" and string_array[index - 1] == "X" and string_array[index - 2] == "E" and string_array[index - 3] == "0" and string_array[index - 4] == "1" and string_array[index - 5] == "X":
                    #print("The loop condition is true")
                    return "Standard Form"
                index = index - 1
        except IndexError:
            #print("There was an Index error")
            return "Normal String"
    else:
        #print("The condition is false")
        return "Normal String"


#'''
def parse(toks):
    i = 0  # "i" means "index"
    total_conditions = 0
    false_conditions = 0
    total_conditions_list = [0]
    false_conditions_list = [0]
    extra_curly_braces = 0
    n_list = []  # n_list is a list of all the indexes where all the different Do This...Until loops start from
    total_loops = 0
    continue_looping = True
    big_expression = ""
    simple_data_item = ""
    end_program = False
    long_sentence = ""
    error_line_information = ""
    error_array= []

    parser_instructions = [
        ["START"],
        ["STOP"],
        ["<<place holder>>"],
        ["ENDIF"],
        ["<<new line character>>"],
        ["{"],
        ["}"],
        ["REPEAT"],
        ["BREAK_THE_LOOP"],
        ["WRITE", "STRING"],
        ["WRITE", "NUM"],
        ["WRITE", "EXPR"],
        ["WRITE", "VAR"],
        ["WRITE", "CONSTANT"],
        ["WRITE", "STOP"],
        ["WRITE", "STRING", "&"],
        ["WRITE", "VAR", "&"],
        ["WRITE", "CONSTANT", "&"],
        ["INPUT", "STRING", "STOREIN", "VAR"],
        ["IF", "VAR", "IS_EQUAL_TO", "VAR", "THEN"],
        ["IF", "VAR", "IS_GREATER_THAN", "VAR", "THEN"],
        ["IF", "VAR", "IS_LESS_THAN", "VAR", "THEN"],
        ["IF", "VAR", "IS_GREATER_THAN_OR_EQUAL_TO", "VAR", "THEN"],
        ["IF", "VAR", "IS_LESS_THAN_OR_EQUAL_TO", "VAR", "THEN"],
        ["IF", "VAR", "IS_NOT_EQUAL_TO", "VAR", "THEN"],
        ["IF", "VAR", "IS_EQUAL_TO", "THEN", "NUM"],
        ["IF", "VAR", "IS_NOT_EQUAL_TO", "THEN", "NUM"],
        ["IF", "VAR", "IS_GREATER_THAN", "THEN", "NUM"],
        ["IF", "VAR", "IS_LESS_THAN", "THEN", "NUM"],
        ["IF", "VAR", "IS_GREATER_THAN_OR_EQUAL_TO", "THEN", "NUM"],
        ["IF", "VAR", "IS_LESS_THAN_OR_EQUAL_TO", "THEN", "NUM"],
        ["IF", "VAR", "IS_EQUAL_TO", "THEN", "EXPR"],
        ["IF", "VAR", "IS_NOT_EQUAL_TO", "THEN", "EXPR"],
        ["IF", "VAR", "IS_GREATER_THAN", "THEN", "EXPR"],
        ["IF", "VAR", "IS_LESS_THAN", "THEN", "EXPR"],
        ["IF", "VAR", "IS_GREATER_THAN_OR_EQUAL_TO", "THEN", "EXPR"],
        ["IF", "VAR", "IS_LESS_THAN_OR_EQUAL_TO", "THEN", "EXPR"],
        ["IF", "VAR", "IS_EQUAL_TO", "STRING", "THEN"],
        ["IF", "VAR", "IS_NOT_EQUAL_TO", "STRING", "THEN"],
        ["IF", "VAR", "EQUALS", "FROM", "NUM", "THEN", "NUM"],
        ["IF", "VAR", "EQUALS", "FROM", "EXPR", "THEN", "NUM"],
        ["IF", "VAR", "EQUALS", "FROM", "NUM", "THEN", "EXPR"],
        ["IF", "VAR", "EQUALS", "FROM", "EXPR", "THEN", "EXPR"],
        ["IF", "VAR", "EQUALS", "FROM", "AFTER", "NUM", "THEN", "NUM"],
        ["IF", "VAR", "EQUALS", "FROM", "AFTER", "EXPR", "THEN", "NUM"],
        ["IF", "VAR", "EQUALS", "FROM", "AFTER", "NUM", "THEN", "EXPR"],
        ["IF", "VAR", "EQUALS", "FROM", "AFTER", "EXPR", "THEN", "EXPR"],
        ["IF", "VAR", "EQUALS", "FROM", "NUM", "BEFORE", "THEN", "NUM"],
        ["IF", "VAR", "EQUALS", "FROM", "EXPR", "BEFORE", "THEN", "NUM"],
        ["IF", "VAR", "EQUALS", "FROM", "NUM", "BEFORE", "THEN", "EXPR"],
        ["IF", "VAR", "EQUALS", "FROM", "EXPR", "BEFORE", "THEN", "EXPR"],
        ["IF", "VAR", "EQUALS", "BETWEEN", "NUM", "THEN", "NUM"],
        ["IF", "VAR", "EQUALS", "BETWEEN", "EXPR", "THEN", "NUM"],
        ["IF", "VAR", "EQUALS", "BETWEEN", "NUM", "THEN", "EXPR"],
        ["IF", "VAR", "EQUALS", "BETWEEN", "EXPR", "THEN", "EXPR"],
        ["IF", "VAR", "EQUALS", "ANYTHING", "ELSE", "THEN"],
        ["INCREASE", "VAR", "BY", "VAR"],
        ["INCREASE", "VAR", "BY", "NUM"],
        ["INCREASE", "VAR", "BY", "EXPR"],
        ["DECREASE", "VAR", "BY", "VAR"],
        ["DECREASE", "VAR", "BY", "NUM"],
        ["DECREASE", "VAR", "BY", "EXPR"],
        ["MULTIPLY", "VAR", "BY", "VAR"],
        ["MULTIPLY", "VAR", "BY", "NUM"],
        ["MULTIPLY", "VAR", "BY", "EXPR"],
        ["DIVIDE", "VAR", "BY", "VAR"],
        ["DIVIDE", "VAR", "BY", "NUM"],
        ["DIVIDE", "VAR", "BY", "EXPR"],
        ["EXPONENTIATE", "VAR", "BY", "VAR"],
        ["EXPONENTIATE", "VAR", "BY", "NUM"],
        ["EXPONENTIATE", "VAR", "BY", "EXPR"],
        ["MODULATE", "VAR", "BY", "VAR"],
        ["MODULATE", "VAR", "BY", "NUM"],
        ["MODULATE", "VAR", "BY", "EXPR"],
        ["FLOOR", "VAR", "BY", "VAR"],
        ["FLOOR", "VAR", "BY", "NUM"],
        ["FLOOR", "VAR", "BY", "EXPR"],
        ["UNTIL", "VAR", "IS_EQUAL_TO", "VAR"],
        ["UNTIL", "VAR", "IS_NOT_EQUAL_TO", "VAR"],
        ["UNTIL", "VAR", "IS_GREATER_THAN", "VAR"],
        ["UNTIL", "VAR", "IS_LESS_THAN", "VAR"],
        ["UNTIL", "VAR", "IS_GREATER_THAN_OR_EQUAL_TO", "VAR"],
        ["UNTIL", "VAR", "IS_LESS_THAN_OR_EQUAL_TO", "VAR"],
        ["UNTIL", "VAR", "IS_EQUAL_TO", "NUM"],
        ["UNTIL", "VAR", "IS_NOT_EQUAL_TO", "NUM"],
        ["UNTIL", "VAR", "IS_GREATER_THAN", "NUM"],
        ["UNTIL", "VAR", "IS_LESS_THAN", "NUM"],
        ["UNTIL", "VAR", "IS_GREATER_THAN_OR_EQUAL_TO", "NUM"],
        ["UNTIL", "VAR", "IS_LESS_THAN_OR_EQUAL_TO", "NUM"],
        ["UNTIL", "VAR", "IS_EQUAL_TO", "EXPR"],
        ["UNTIL", "VAR", "IS_NOT_EQUAL_TO", "EXPR"],
        ["UNTIL", "VAR", "IS_GREATER_THAN", "EXPR"],
        ["UNTIL", "VAR", "IS_LESS_THAN", "EXPR"],
        ["UNTIL", "VAR", "IS_GREATER_THAN_OR_EQUAL_TO", "EXPR"],
        ["UNTIL", "VAR", "IS_LESS_THAN_OR_EQUAL_TO", "EXPR"],
        ["UNTIL", "VAR", "IS_EQUAL_TO", "STRING"],
        ["UNTIL", "VAR", "IS_NOT_EQUAL_TO", "STRING"],
        ["UNTIL", "THE", "LOOP", "BREAKS"],
        ["VAR", "EQUALS"]
        ]

    toks = array_filler(toks, parser_instructions)

    try:
        while i < len(toks):
            error_array.append(error_line_information)
            #print(f"In token {toks[i]}, the total conditions list is {total_conditions_list}")
            #print(f"In token {toks[i]}, the false conditions list is {false_conditions_list}")
            if toks[i] == "START":
                code_output.insert(END, "\n>>> THE PROGRAM HAS STARTED...\n\n")
                error_line_information = "START THIS PROGRAM (\"Start this Program\" is at the beginning of the program)"
                i = i + 1
            elif toks[i] == "STOP" and toks[i-1] != "START":
                code_output.insert(END, ">>> THE PROGRAM HAS ENDED")
                i = i + 1
            elif toks[i] == "STOP" and toks[i-1] == "START":
                code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                code_output.insert(END, f">>> The Syntax Error is on the 1st or 2nd line of your program\n\n")
                code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                i = i + 1
            elif toks[i] == "<<place holder>>":
                i = i + 1
            elif toks[i] == "ENDIF":
                error_line_information = error_array[-1] + " End the If Statement"
                try:
                    total_conditions = total_conditions_list[-2]
                    false_conditions = false_conditions_list[-2]
                    del total_conditions_list[-1]
                    del false_conditions_list[-1]
                except IndexError:
                    del total_conditions_list[-1]
                    del false_conditions_list[-1]
                    total_conditions_list.append(0)
                    false_conditions_list.append(0)
                    total_conditions = 0
                    false_conditions = 0
                i = i + 1
            elif toks[i] == "<<new line character>>":
                i = i + 1
            elif toks[i] == "{" and toks[i-1] == "REPEAT":
                error_line_information = error_array[-1] + " {"
                i = i + 1
            elif toks[i] == "{" and toks[i-1] == "NESTED_IF":
                total_conditions_list.append(0)
                false_conditions_list.append(0)
                total_conditions = 0
                false_conditions = 0
                i = i + 1
            elif toks[i] == "}":
                error_line_information = error_array[-1] + " }"
                i = i + 1
            elif toks[i] == "NESTED_IF":
                error_line_information = error_array[-1] + " Make this nested if statement"
                i = i + 1
            elif toks[i] == "REPEAT":
                error_line_information = error_array[-1] + " Do This"
                i = i + 1
                n_list.append(i)
                total_loops = total_loops + 1
            elif toks[i] == "BREAK_THE_LOOP":
                while i < len(toks) and toks[i] != "UNTIL" and continue_looping != False:
                    i = i + 1
                    if toks[i] == "UNTIL":
                        i = i + 4
                        if n_list != []:
                            del n_list[-1]
                            total_loops = total_loops - 1
                            break
                        else:
                            continue_looping = False
                if continue_looping == False:
                    code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i+1][0:6] == "WRITE STRING" or toks[i] + " " + toks[i + 1][0:3] == "WRITE NUM" or toks[i] + " " + toks[i + 1][0:4] == "WRITE EXPR" or toks[i] + " " + toks[i + 1][0:3] == "WRITE VAR" or toks[i] + " " + toks[i + 1][0:8] == "WRITE CONSTANT" or toks[i] + " " + toks[i + 1] == "WRITE STOP" or toks[i] + " " + toks[i + 1][0:6] + " " + toks[i + 2] == "WRITE STRING &" or toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] == "WRITE VAR &" or toks[i] + " " + toks[i + 1][0:8] + " " + toks[i + 2] == "WRITE CONSTANT &":
                if toks[i+1] == "STOP":
                    code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                    code_output.insert(END, f">>> The Syntax Error comes after the line (or it is on the line): {error_line_information}\n\n")
                    code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                    break
                elif toks[i + 1][0:6] == "STRING" and toks[i+2] != "&":
                    error_line_information = toks[i] + " " + "\"" + toks[i+1][7:] + "\" on the screen"
                    code_output.insert(END, toks[i + 1][7:] + "\n\n")
                    i = i + 2
                elif toks[i + 1][0:3] == "NUM":
                    error_line_information = toks[i] + " " + toks[i+1][4:] + " on the screen"
                    number = float(toks[i + 1][4:])
                    code_output.insert(END, f"{number:,}" + "\n\n")
                    i = i + 2
                elif toks[i + 1][0:4] == "EXPR":
                    expression = toks[i+1][5:]
                    expression = expression.replace("**", " Exp ")
                    expression = expression.replace("*", " x ")
                    expression = expression.replace("//", " Floor ")
                    expression = expression.replace("%", " Modulus ")
                    error_line_information = toks[i] + " " + expression + " on the screen"
                    answer = evalExpression(toks[i+1][5:])
                    answer = float(answer)
                    code_output.insert(END, f"{answer:,}" + "\n\n")
                    i = i + 2
                elif toks[i + 1][0:3] == "VAR" and toks[i+2] != "&":
                    error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "] on the screen"
                    variable = getVARIABLE(toks[i+1])
                    try:
                        variable = float(variable)
                        code_output.insert(END, f"{variable:,}" + "\n\n")
                        i = i + 2
                    except ValueError:
                        code_output.insert(END, str(variable) + "\n\n")
                        i = i + 2
                elif toks[i + 1][0:8] == "CONSTANT" and toks[i+2] != "&":
                    error_line_information = toks[i] + " " + "Constant[" + get_constant_name(toks[i + 1][9:]) + "] on the screen"
                    constant = toks[i+1][9:]
                    constant = float(constant)
                    code_output.insert(END, f"{constant:,}" + "\n\n")
                    i = i + 2
                elif toks[i + 1][0:6] == "STRING" and toks[i+2] == "&":
                    error_line_information = f"Write \"{toks[i+1][7:]}\" and also write "
                    long_sentence = long_sentence + toks[i+1][7:] + " "
                    i = i + 2
                    while i < len(toks):
                        i = i + 1
                        if toks[i] == "STOP":
                            code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                            code_output.insert(END, f">>> The Syntax Error is in the line: {error_line_information}\n\n")
                            code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                            end_program = True
                            break
                        elif toks[i] == "&":
                            error_line_information = error_line_information + "and also write "
                        elif toks[i][0:6] == "STRING":
                            error_line_information = error_line_information + f"\"{toks[i][7:]}\" "
                            long_sentence = long_sentence + toks[i][7:] + " "
                        elif toks[i][0:8] == "CONSTANT":
                            error_line_information = error_line_information + f"Constant[{get_constant_name(toks[i][9:])}] "
                            constant = float(toks[i][9:])
                            long_sentence = long_sentence + f"{constant:,}" + " "
                        elif toks[i][0:3] == "VAR":
                            if toks[i][4:] in symbol_table:
                                error_line_information = error_line_information + f"Variable[{toks[i][4:]}] "
                                try:
                                    variable = float(getVARIABLE(toks[i]))
                                    long_sentence = long_sentence + f"{variable:,}" + " "
                                except ValueError:
                                    string = getVARIABLE(toks[i])
                                    long_sentence = long_sentence + string + " "
                            else:
                                code_output.insert(END, f">>> Variable Error: {toks[i][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                                end_program = True
                                break
                        elif toks[i] == "<<new line character>>":
                            error_line_information = error_line_information + "on the screen"
                            code_output.insert(END, long_sentence + "\n\n")
                            long_sentence = ""
                            i = i + 1
                            break
                    if end_program == True:
                        break
                elif toks[i + 1][0:8] == "CONSTANT" and toks[i+2] == "&":
                    error_line_information = f"Write Constant[{get_constant_name(toks[i + 1][9:])}] and also write "
                    constant_holder = float(toks[i+1][9:])
                    long_sentence = long_sentence + f"{constant_holder:,}" + " "
                    i = i + 2
                    while i < len(toks):
                        i = i + 1
                        if toks[i] == "STOP":
                            code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                            code_output.insert(END, f">>> The Syntax Error is in the line: {error_line_information}\n\n")
                            code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                            end_program = True
                            break
                        elif toks[i] == "&":
                            error_line_information = error_line_information + "and also write "
                        elif toks[i][0:6] == "STRING":
                            error_line_information = error_line_information + f"\"{toks[i][7:]}\" "
                            long_sentence = long_sentence + toks[i][7:] + " "
                        elif toks[i][0:8] == "CONSTANT":
                            error_line_information = error_line_information + f"Constant[{get_constant_name(toks[i][9:])}] "
                            constant = float(toks[i][9:])
                            long_sentence = long_sentence + f"{constant:,}" + " "
                        elif toks[i][0:3] == "VAR":
                            if toks[i][4:] in symbol_table:
                                error_line_information = error_line_information + f"Variable[{toks[i][4:]}] "
                                try:
                                    variable = float(getVARIABLE(toks[i]))
                                    long_sentence = long_sentence + f"{variable:,}" + " "
                                except ValueError:
                                    string = getVARIABLE(toks[i])
                                    long_sentence = long_sentence + string + " "
                            else:
                                code_output.insert(END, f">>> Variable Error: {toks[i][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                                end_program = True
                                break
                        elif toks[i] == "<<new line character>>":
                            error_line_information = error_line_information + "on the screen"
                            code_output.insert(END, long_sentence + "\n\n")
                            long_sentence = ""
                            i = i + 1
                            break
                    if end_program == True:
                        break
                elif toks[i + 1][0:3] == "VAR" and toks[i+2] == "&":
                    error_line_information = f"Write Variable[{toks[i + 1][4:]}] and also write "
                    try:
                        variable_holder = float(getVARIABLE(toks[i+1]))
                        long_sentence = long_sentence + f"{variable_holder:,}" + " "
                        i = i + 2
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "STOP":
                                code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                                code_output.insert(END, f">>> The Syntax Error is in the line: {error_line_information}\n\n")
                                code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                                end_program = True
                                break
                            elif toks[i] == "&":
                                error_line_information = error_line_information + "and also write "
                            elif toks[i][0:6] == "STRING":
                                error_line_information = error_line_information + f"\"{toks[i][7:]}\" "
                                long_sentence = long_sentence + toks[i][7:] + " "
                            elif toks[i][0:8] == "CONSTANT":
                                error_line_information = error_line_information + f"Constant[{get_constant_name(toks[i][9:])}] "
                                constant = float(toks[i][9:])
                                long_sentence = long_sentence + f"{constant:,}" + " "
                            elif toks[i][0:3] == "VAR":
                                if toks[i][4:] in symbol_table:
                                    error_line_information = error_line_information + f"Variable[{toks[i][4:]}] "
                                    try:
                                        variable = float(getVARIABLE(toks[i]))
                                        long_sentence = long_sentence + f"{variable:,}" + " "
                                    except ValueError:
                                        string = getVARIABLE(toks[i])
                                        long_sentence = long_sentence + string + " "
                                else:
                                    code_output.insert(END, f">>> Variable Error: {toks[i][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                                    end_program = True
                                    break
                            elif toks[i] == "<<new line character>>":
                                error_line_information = error_line_information + "on the screen"
                                code_output.insert(END, long_sentence + "\n\n")
                                long_sentence = ""
                                i = i + 1
                                break
                        if end_program == True:
                            break
                    except ValueError:
                        long_sentence = long_sentence + getVARIABLE(toks[i+1]) + " "
                        i = i + 2
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "STOP":
                                code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                                code_output.insert(END, f">>> The Syntax Error is in the line: {error_line_information}\n\n")
                                code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                                end_program = True
                                break
                            elif toks[i] == "&":
                                error_line_information = error_line_information + "and also write "
                            elif toks[i][0:6] == "STRING":
                                error_line_information = error_line_information + f"\"{toks[i][7:]}\" "
                                long_sentence = long_sentence + toks[i][7:] + " "
                            elif toks[i][0:8] == "CONSTANT":
                                error_line_information = error_line_information + f"Constant[{get_constant_name(toks[i][9:])}] "
                                constant = float(toks[i][9:])
                                long_sentence = long_sentence + f"{constant:,}" + " "
                            elif toks[i][0:3] == "VAR":
                                if toks[i][4:] in symbol_table:
                                    error_line_information = error_line_information + f"Variable[{toks[i][4:]}] "
                                    try:
                                        variable = float(getVARIABLE(toks[i]))
                                        long_sentence = long_sentence + f"{variable:,}" + " "
                                    except ValueError:
                                        string = getVARIABLE(toks[i])
                                        long_sentence = long_sentence + string + " "
                                else:
                                    code_output.insert(END,
                                                       f">>> Variable Error: {toks[i][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                                    end_program = True
                                    break
                            elif toks[i] == "<<new line character>>":
                                error_line_information = error_line_information + "on the screen"
                                code_output.insert(END, long_sentence + "\n\n")
                                long_sentence = ""
                                i = i + 1
                                break
                        if end_program == True:
                            break
            elif toks[i][0:3] + " " + toks[i + 1] == "VAR EQUALS":
                error_line_information = f"Variable {toks[i][4:]} is "
                new_variable_name = toks[i]
                i = i + 1
                while i < len(toks):
                    i = i + 1
                    if toks[i] == "STOP":
                        code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                        code_output.insert(END, f">>> The Syntax Error is in the line: {error_line_information}\n\n")
                        code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                        end_program = True
                        break
                    elif toks[i][0:6] == "STRING":
                        error_line_information = error_line_information + f"\"{toks[i][7:]}\" "
                        simple_data_item = simple_data_item + toks[i][7:]
                    elif toks[i][0:3] == "NUM":
                        error_line_information = error_line_information + f"{toks[i][4:]} "
                        simple_data_item = simple_data_item + toks[i][4:]
                    elif toks[i][0:4] == "EXPR":
                        expression = toks[i][5:]
                        expression = expression.replace("**", " Exp ")
                        expression = expression.replace("*", " x ")
                        expression = expression.replace("//", " Floor ")
                        expression = expression.replace("%", " Modulus ")
                        error_line_information = error_line_information + f"{expression} "
                        big_expression = big_expression + toks[i][5:]
                    elif toks[i][0:8] == "CONSTANT":
                        error_line_information = error_line_information + f"Constant[{get_constant_name(toks[i][9:])}] "
                        big_expression = big_expression + "(" + toks[i][9:] + ")"
                    elif toks[i][0:3] == "VAR":
                        if toks[i][4:] in symbol_table:
                            error_line_information = error_line_information + f"Variable[{toks[i][4:]}] "
                            try:
                                variable = float(getVARIABLE(toks[i]))
                                big_expression = big_expression + "(" + str(variable) + ")"
                            except ValueError:
                                string = getVARIABLE(toks[i])
                                simple_data_item = simple_data_item + str(string)
                        else:
                            code_output.insert(END, f">>> Variable Error: {toks[i][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                            end_program = True
                            break
                    elif toks[i] == "<<new line character>>":
                        if simple_data_item != "" and big_expression == "":
                            doASSIGN(new_variable_name, simple_data_item)
                            simple_data_item = ""
                            i = i + 1
                            break
                        elif simple_data_item == "" and big_expression != "":
                            doASSIGN(new_variable_name, evalExpression(big_expression))
                            big_expression = ""
                            i = i + 1
                            break
                        elif simple_data_item != "" and big_expression != "":
                            code_output.insert(END, ">>> Variable Storage Error: In the Sofya Program you have not stored things in a variable correctly!\n\n")
                            code_output.insert(END, f">>> The Variable Storage Error is in the line: {error_line_information}\n\n")
                            code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                            end_program = True
                            break
                        elif simple_data_item == "" and big_expression == "":
                            code_output.insert(END, ">>> Empty Variable Error: In the Sofya Program you have not stored anything in a certain variable!\n\n")
                            code_output.insert(END, f">>> The Empty Variable Error is in the line: {error_line_information}\n\n")
                            code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                            end_program = True
                            break
                if end_program == True:
                    break
            elif toks[i] + " " + toks[i + 1][0:6] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "INPUT STRING STOREIN VAR":
                error_line_information = "Ask the Computer User" + " " + "\"" + toks[i + 1][7:] + "\"" + " " + "and store the answer in" + " " + "Variable[" + toks[i + 3][4:] + "]"
                string = toks[i+1][7:]
                varname = toks[i+3]
                input_box.bind("<Return>", on_enter)
                user_input = gui_input(string)
                string_type = check_string(user_input)
                if string_type == "Standard Form":
                    expression = user_input
                    expression = expression.replace("EXP", "**")
                    expression = expression.replace("X", "*")
                    try:
                        expression = evalExpression(expression)
                        doASSIGN(varname, expression)
                    except SyntaxError:
                        code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                        code_output.insert(END, f">>> The Syntax Error happened when you typed {user_input} in the input box\n\n")
                        code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                        break
                else:
                    try:
                        user_input = float(user_input)
                        doASSIGN(varname, str(user_input))
                    except ValueError:
                        try:
                            if "/" in user_input and "AND" not in user_input:
                                doASSIGN(varname, evalExpression(user_input))
                            elif "/" in user_input and "AND" in user_input:
                                user_input = user_input.replace("AND", "+")
                                doASSIGN(varname, evalExpression(user_input))
                            else:
                                doASSIGN(varname, user_input)
                        except SyntaxError:
                            code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                            code_output.insert(END, f">>> The Syntax Error happened when you typed {user_input} in the input box\n\n")
                            code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                            break
                        except ZeroDivisionError:
                            code_output.insert(END, ">>> Division by Zero Error: In the Sofya Program there is a place where a number is being divided by zero!\n\n")
                            code_output.insert(END, f">>> The Division by Zero Error happened when you typed {user_input} in the input box\n\n")
                            code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                            break
                i = i + 4
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] + " " + toks[i + 4] == "IF VAR IS_EQUAL_TO VAR THEN":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=" + " " + "Variable[" + toks[i + 3][4:] + "]" + " " + toks[i + 4]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] and toks[i+3][4:] in symbol_table:
                    try:
                        if float(evalExpression(str(getVARIABLE(toks[i + 1])))) == float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                            i = i + 5
                        else:
                            false_conditions = false_conditions + 1
                            false_conditions_list[-1] = false_conditions
                            while i < len(toks):
                                i = i + 1
                                if toks[i] == "ENDIF":
                                    try:
                                        if total_conditions_list[-1] == false_conditions_list[-1]:
                                            false_conditions_list[-2] = false_conditions_list[-2] + 1
                                            total_conditions = total_conditions_list[-2]
                                            false_conditions = false_conditions_list[-2]
                                            del total_conditions_list[-1]
                                            del false_conditions_list[-1]
                                            i = i + 1
                                            break
                                        else:
                                            total_conditions = total_conditions_list[-2]
                                            false_conditions = false_conditions_list[-2]
                                            del total_conditions_list[-1]
                                            del false_conditions_list[-1]
                                            i = i + 1
                                            break
                                    except IndexError:
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        total_conditions_list.append(0)
                                        false_conditions_list.append(0)
                                        total_conditions = 0
                                        false_conditions = 0
                                        i = i + 1
                                        break
                                elif toks[i] == "{":
                                    while i < len(toks):
                                        i = i + 1
                                        if toks[i] == "{":
                                            extra_curly_braces = extra_curly_braces + 1
                                        elif toks[i] == "}" and extra_curly_braces > 0:
                                            extra_curly_braces = extra_curly_braces - 1
                                        elif toks[i] == "}" and extra_curly_braces == 0:
                                            break
                                elif toks[i] == "IF":
                                    break
                    except ValueError:
                        variable_1 = getVARIABLE(toks[i+1])
                        variable_1 = variable_1.upper()
                        variable_2 = getVARIABLE(toks[i+3])
                        variable_2 = variable_2.upper()
                        if str(variable_1) == str(variable_2):
                            i = i + 5
                        else:
                            false_conditions = false_conditions + 1
                            false_conditions_list[-1] = false_conditions
                            while i < len(toks):
                                i = i + 1
                                if toks[i] == "ENDIF":
                                    try:
                                        if total_conditions_list[-1] == false_conditions_list[-1]:
                                            false_conditions_list[-2] = false_conditions_list[-2] + 1
                                            total_conditions = total_conditions_list[-2]
                                            false_conditions = false_conditions_list[-2]
                                            del total_conditions_list[-1]
                                            del false_conditions_list[-1]
                                            i = i + 1
                                            break
                                        else:
                                            total_conditions = total_conditions_list[-2]
                                            false_conditions = false_conditions_list[-2]
                                            del total_conditions_list[-1]
                                            del false_conditions_list[-1]
                                            i = i + 1
                                            break
                                    except IndexError:
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        total_conditions_list.append(0)
                                        false_conditions_list.append(0)
                                        total_conditions = 0
                                        false_conditions = 0
                                        i = i + 1
                                        break
                                elif toks[i] == "{":
                                    while i < len(toks):
                                        i = i + 1
                                        if toks[i] == "{":
                                            extra_curly_braces = extra_curly_braces + 1
                                        elif toks[i] == "}" and extra_curly_braces > 0:
                                            extra_curly_braces = extra_curly_braces - 1
                                        elif toks[i] == "}" and extra_curly_braces == 0:
                                            break
                                elif toks[i] == "IF":
                                    break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] + " " + toks[i + 4] == "IF VAR IS_GREATER_THAN VAR THEN":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + ">" + " " + "Variable[" + toks[i + 3][4:] + "]" + " " + toks[i + 4]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] and toks[i+3][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] + " " + toks[i + 4] == "IF VAR IS_LESS_THAN VAR THEN":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "<" + " " + "Variable[" + toks[i + 3][4:] + "]" + " " + toks[i + 4]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] and toks[i+3][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] + " " + toks[i + 4] == "IF VAR IS_GREATER_THAN_OR_EQUAL_TO VAR THEN":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "> or =" + " " + "Variable[" + toks[i + 3][4:] + "]" + " " + toks[i + 4]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] and toks[i+3][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] + " " + toks[i + 4] == "IF VAR IS_LESS_THAN_OR_EQUAL_TO VAR THEN":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "< or =" + " " + "Variable[" + toks[i + 3][4:] + "]" + " " + toks[i + 4]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] and toks[i+3][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] + " " + toks[i + 4] == "IF VAR IS_NOT_EQUAL_TO VAR THEN":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=/=" + " " + "Variable[" + toks[i + 3][4:] + "]" + " " + toks[i + 4]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] and toks[i+3][4:] in symbol_table:
                    try:
                        if float(evalExpression(str(getVARIABLE(toks[i + 1])))) != float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                            i = i + 5
                        else:
                            false_conditions = false_conditions + 1
                            false_conditions_list[-1] = false_conditions
                            while i < len(toks):
                                i = i + 1
                                if toks[i] == "ENDIF":
                                    try:
                                        if total_conditions_list[-1] == false_conditions_list[-1]:
                                            false_conditions_list[-2] = false_conditions_list[-2] + 1
                                            total_conditions = total_conditions_list[-2]
                                            false_conditions = false_conditions_list[-2]
                                            del total_conditions_list[-1]
                                            del false_conditions_list[-1]
                                            i = i + 1
                                            break
                                        else:
                                            total_conditions = total_conditions_list[-2]
                                            false_conditions = false_conditions_list[-2]
                                            del total_conditions_list[-1]
                                            del false_conditions_list[-1]
                                            i = i + 1
                                            break
                                    except IndexError:
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        total_conditions_list.append(0)
                                        false_conditions_list.append(0)
                                        total_conditions = 0
                                        false_conditions = 0
                                        i = i + 1
                                        break
                                elif toks[i] == "{":
                                    while i < len(toks):
                                        i = i + 1
                                        if toks[i] == "{":
                                            extra_curly_braces = extra_curly_braces + 1
                                        elif toks[i] == "}" and extra_curly_braces > 0:
                                            extra_curly_braces = extra_curly_braces - 1
                                        elif toks[i] == "}" and extra_curly_braces == 0:
                                            break
                                elif toks[i] == "IF":
                                    break
                    except ValueError:
                        variable_1 = getVARIABLE(toks[i+1])
                        variable_1 = variable_1.upper()
                        variable_2 = getVARIABLE(toks[i+3])
                        variable_2 = variable_2.upper()
                        if str(variable_1) != str(variable_2):
                            i = i + 5
                        else:
                            false_conditions = false_conditions + 1
                            false_conditions_list[-1] = false_conditions
                            while i < len(toks):
                                i = i + 1
                                if toks[i] == "ENDIF":
                                    try:
                                        if total_conditions_list[-1] == false_conditions_list[-1]:
                                            false_conditions_list[-2] = false_conditions_list[-2] + 1
                                            total_conditions = total_conditions_list[-2]
                                            false_conditions = false_conditions_list[-2]
                                            del total_conditions_list[-1]
                                            del false_conditions_list[-1]
                                            i = i + 1
                                            break
                                        else:
                                            total_conditions = total_conditions_list[-2]
                                            false_conditions = false_conditions_list[-2]
                                            del total_conditions_list[-1]
                                            del false_conditions_list[-1]
                                            i = i + 1
                                            break
                                    except IndexError:
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        total_conditions_list.append(0)
                                        false_conditions_list.append(0)
                                        total_conditions = 0
                                        false_conditions = 0
                                        i = i + 1
                                        break
                                elif toks[i] == "{":
                                    while i < len(toks):
                                        i = i + 1
                                        if toks[i] == "{":
                                            extra_curly_braces = extra_curly_braces + 1
                                        elif toks[i] == "}" and extra_curly_braces > 0:
                                            extra_curly_braces = extra_curly_braces - 1
                                        elif toks[i] == "}" and extra_curly_braces == 0:
                                            break
                                elif toks[i] == "IF":
                                    break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] == "IF VAR IS_EQUAL_TO THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=" + " " + toks[i + 4][4:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) == float(toks[i+4][4:]):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] == "IF VAR IS_NOT_EQUAL_TO THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=/=" + " " + toks[i + 4][4:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) != float(toks[i+4][4:]):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] == "IF VAR IS_GREATER_THAN THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + ">" + " " + toks[i + 4][4:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(toks[i+4][4:]):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] == "IF VAR IS_LESS_THAN THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "<" + " " + toks[i + 4][4:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(toks[i+4][4:]):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] == "IF VAR IS_GREATER_THAN_OR_EQUAL_TO THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "> or =" + " " + toks[i + 4][4:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(toks[i+4][4:]):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] == "IF VAR IS_LESS_THAN_OR_EQUAL_TO THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "< or =" + " " + toks[i + 4][4:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(toks[i+4][4:]):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] == "IF VAR IS_EQUAL_TO THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=" + " " + toks[i + 4][5:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) == float(evalExpression(str(toks[i+4][5:]))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] == "IF VAR IS_NOT_EQUAL_TO THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=/=" + " " + toks[i + 4][5:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) != float(evalExpression(str(toks[i+4][5:]))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] == "IF VAR IS_GREATER_THAN THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + ">" + " " + toks[i + 4][5:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(evalExpression(str(toks[i+4][5:]))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] == "IF VAR IS_LESS_THAN THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "<" + " " + toks[i + 4][5:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(evalExpression(str(toks[i+4][5:]))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] == "IF VAR IS_GREATER_THAN_OR_EQUAL_TO THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "> or =" + " " + toks[i + 4][5:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(evalExpression(str(toks[i+4][5:]))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] == "IF VAR IS_LESS_THAN_OR_EQUAL_TO THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "< or =" + " " + toks[i + 4][5:] + " " + toks[i + 3]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(evalExpression(str(toks[i+4][5:]))):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:6] + " " + toks[i + 4] == "IF VAR IS_EQUAL_TO STRING THEN":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=" + " " + "\"" + toks[i + 3][7:] + "\"" + " " + toks[i + 4]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if str(getVARIABLE(toks[i + 1])) == str(toks[i+3][7:]):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:6] + " " + toks[i + 4] == "IF VAR IS_NOT_EQUAL_TO STRING THEN":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=/=" + " " + "\"" + toks[i + 3][7:] + "\"" + " " + toks[i + 4]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if str(getVARIABLE(toks[i + 1])) != str(toks[i+3][7:]):
                        i = i + 5
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] + " " + toks[i + 5] + " " + toks[i + 6][0:3] == "IF VAR EQUALS FROM NUM THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][4:] + " " + "to" + " " + toks[i + 6][4:] + " " + toks[i + 5]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(toks[i + 4][4:]) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(toks[i + 6][4:]):
                        i = i + 7
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] + " " + toks[i + 5] + " " + toks[i + 6][0:3] == "IF VAR EQUALS FROM EXPR THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][5:] + " " + "to" + " " + toks[i + 6][4:] + " " + toks[i + 5]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(evalExpression(str(toks[i + 4][5:]))) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(toks[i + 6][4:]):
                        i = i + 7
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] + " " + toks[i + 5] + " " + toks[i + 6][0:4] == "IF VAR EQUALS FROM NUM THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][4:] + " " + "to" + " " + toks[i + 6][5:] + " " + toks[i + 5]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(toks[i + 4][4:]) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(evalExpression(str(toks[i + 6][5:]))):
                        i = i + 7
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] + " " + toks[i + 5] + " " + toks[i + 6][0:4] == "IF VAR EQUALS FROM EXPR THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][5:] + " " + "to" + " " + toks[i + 6][5:] + " " + toks[i + 5]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(evalExpression(str(toks[i + 4][5:]))) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(evalExpression(str(toks[i + 6][5:]))):
                        i = i + 7
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5][0:3] + " " + toks[i + 6] + " " + toks[i + 7][0:3] == "IF VAR EQUALS FROM AFTER NUM THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5][4:] + " " + "to" + " " + toks[i + 7][4:] + " " + toks[i + 6]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(toks[i + 5][4:]) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(toks[i + 7][4:]):
                        i = i + 8
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5][0:4] + " " + toks[i + 6] + " " + toks[i + 7][0:3] == "IF VAR EQUALS FROM AFTER EXPR THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5][5:] + " " + "to" + " " + toks[i + 7][4:] + " " + toks[i + 6]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(evalExpression(str(toks[i + 5][5:]))) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(toks[i + 7][4:]):
                        i = i + 8
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5][0:3] + " " + toks[i + 6] + " " + toks[i + 7][0:4] == "IF VAR EQUALS FROM AFTER NUM THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5][4:] + " " + "to" + " " + toks[i + 7][5:] + " " + toks[i + 6]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(toks[i + 5][4:]) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(evalExpression(str(toks[i + 7][5:]))):
                        i = i + 8
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5][0:4] + " " + toks[i + 6] + " " + toks[i + 7][0:4] == "IF VAR EQUALS FROM AFTER EXPR THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5][5:] + " " + "to" + " " + toks[i + 7][5:] + " " + toks[i + 6]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(evalExpression(str(toks[i + 5][5:]))) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(evalExpression(str(toks[i + 7][5:]))):
                        i = i + 8
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] + " " + toks[i + 5] + " " + toks[i + 6] + " " + toks[i + 7][0:3] == "IF VAR EQUALS FROM NUM BEFORE THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][4:] + " " + "to" + toks[i + 5] + " " + toks[i + 7][4:] + " " + toks[i + 6]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(toks[i + 4][4:]) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(toks[i + 7][4:]):
                        i = i + 8
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] + " " + toks[i + 5] + " " + toks[i + 6] + " " + toks[i + 7][0:3] == "IF VAR EQUALS FROM EXPR BEFORE THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][5:] + " " + "to" + toks[i + 5] + " " + toks[i + 7][4:] + " " + toks[i + 6]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(evalExpression(str(toks[i + 4][5:]))) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(toks[i + 7][4:]):
                        i = i + 8
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] + " " + toks[i + 5] + " " + toks[i + 6] + " " + toks[i + 7][0:4] == "IF VAR EQUALS FROM NUM BEFORE THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][4:] + " " + "to" + toks[i + 5] + " " + toks[i + 7][5:] + " " + toks[i + 6]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(toks[i + 4][4:]) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(evalExpression(str(toks[i + 7][5:]))):
                        i = i + 8
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] + " " + toks[i + 5] + " " + toks[i + 6] + " " + toks[i + 7][0:4] == "IF VAR EQUALS FROM EXPR BEFORE THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][5:] + " " + "to" + toks[i + 5] + " " + toks[i + 7][5:] + " " + toks[i + 6]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(evalExpression(str(toks[i + 4][5:]))) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(evalExpression(str(toks[i + 7][5:]))):
                        i = i + 8
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] + " " + toks[i + 5] + " " + toks[i + 6][0:3] == "IF VAR EQUALS BETWEEN NUM THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][4:] + " " + "and" + " " + toks[i + 6][4:] + " " + toks[i + 5]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(toks[i + 4][4:]) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(toks[i + 6][4:]):
                        i = i + 7
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] + " " + toks[i + 5] + " " + toks[i + 6][0:3] == "IF VAR EQUALS BETWEEN EXPR THEN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][5:] + " " + "and" + " " + toks[i + 6][4:] + " " + toks[i + 5]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(evalExpression(str(toks[i + 4][5:]))) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(toks[i + 6][4:]):
                        i = i + 7
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:3] + " " + toks[i + 5] + " " + toks[i + 6][0:4] == "IF VAR EQUALS BETWEEN NUM THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][4:] + " " + "and" + " " + toks[i + 6][5:] + " " + toks[i + 5]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(toks[i + 4][4:]) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(evalExpression(str(toks[i + 6][5:]))):
                        i = i + 7
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4][0:4] + " " + toks[i + 5] + " " + toks[i + 6][0:4] == "IF VAR EQUALS BETWEEN EXPR THEN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4][5:] + " " + "and" + " " + toks[i + 6][5:] + " " + toks[i + 5]
                total_conditions = total_conditions + 1
                total_conditions_list[-1] = total_conditions
                if toks[i+1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(evalExpression(str(toks[i + 4][5:]))) and float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(evalExpression(str(toks[i + 6][5:]))):
                        i = i + 7
                    else:
                        false_conditions = false_conditions + 1
                        false_conditions_list[-1] = false_conditions
                        while i < len(toks):
                            i = i + 1
                            if toks[i] == "ENDIF":
                                try:
                                    if total_conditions_list[-1] == false_conditions_list[-1]:
                                        false_conditions_list[-2] = false_conditions_list[-2] + 1
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                    else:
                                        total_conditions = total_conditions_list[-2]
                                        false_conditions = false_conditions_list[-2]
                                        del total_conditions_list[-1]
                                        del false_conditions_list[-1]
                                        i = i + 1
                                        break
                                except IndexError:
                                    del total_conditions_list[-1]
                                    del false_conditions_list[-1]
                                    total_conditions_list.append(0)
                                    false_conditions_list.append(0)
                                    total_conditions = 0
                                    false_conditions = 0
                                    i = i + 1
                                    break
                            elif toks[i] == "{":
                                while i < len(toks):
                                    i = i + 1
                                    if toks[i] == "{":
                                        extra_curly_braces = extra_curly_braces + 1
                                    elif toks[i] == "}" and extra_curly_braces > 0:
                                        extra_curly_braces = extra_curly_braces - 1
                                    elif toks[i] == "}" and extra_curly_braces == 0:
                                        break
                            elif toks[i] == "IF":
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5] == "IF VAR EQUALS ANYTHING ELSE THEN" and total_conditions_list[-1] == false_conditions_list[-1]:
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5]
                if toks[i+1][4:] in symbol_table:
                    i = i + 6
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5] == "IF VAR EQUALS ANYTHING ELSE THEN" and total_conditions_list[-1] != false_conditions_list[-1]:
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "is" + " " + toks[i + 3] + " " + toks[i + 4] + " " + toks[i + 5]
                if toks[i+1][4:] in symbol_table:
                    i = i + 6
                    while i < len(toks):
                        i = i + 1
                        if toks[i] == "ENDIF":
                            try:
                                total_conditions = total_conditions_list[-2]
                                false_conditions = false_conditions_list[-2]
                                del total_conditions_list[-1]
                                del false_conditions_list[-1]
                                i = i + 1
                                break
                            except IndexError:
                                del total_conditions_list[-1]
                                del false_conditions_list[-1]
                                total_conditions_list.append(0)
                                false_conditions_list.append(0)
                                total_conditions = 0
                                false_conditions = 0
                                i = i + 1
                                break
                        elif toks[i] == "{":
                            while i < len(toks):
                                i = i + 1
                                if toks[i] == "{":
                                    extra_curly_braces = extra_curly_braces + 1
                                elif toks[i] == "}" and extra_curly_braces > 0:
                                    extra_curly_braces = extra_curly_braces - 1
                                elif toks[i] == "}" and extra_curly_braces == 0:
                                    break
                        elif toks[i] == "IF":
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "INCREASE VAR BY VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i+1][4:] + "]" + " " + toks[i+2] + " " + "Variable[" + toks[i+3][4:] + "]"
                if toks[i+3][4:] in symbol_table:
                    result = static_variable_increment(toks[i+1], float(getVARIABLE(toks[i+3])))
                    if result == "Successfully incremented":
                        i = i + 4
                    else:
                        break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "INCREASE VAR BY NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][4:]
                result = static_variable_increment(toks[i+1], float(toks[i+3][4:]))
                if result == "Successfully incremented":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:4] == "INCREASE VAR BY EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][5:]
                result = static_variable_increment(toks[i+1], float(evalExpression(str(toks[i+3][5:]))))
                if result == "Successfully incremented":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "DECREASE VAR BY VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i+3][4:] in symbol_table:
                    result = static_variable_decrement(toks[i+1], float(getVARIABLE(toks[i+3])))
                    if result == "Successfully decremented":
                        i = i + 4
                    else:
                        break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "DECREASE VAR BY NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][4:]
                result = static_variable_decrement(toks[i+1], float(toks[i+3][4:]))
                if result == "Successfully decremented":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:4] == "DECREASE VAR BY EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][5:]
                result = static_variable_decrement(toks[i+1], float(evalExpression(str(toks[i+3][5:]))))
                if result == "Successfully decremented":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "MULTIPLY VAR BY VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i+3][4:] in symbol_table:
                    result = static_variable_multiplication(toks[i+1], float(getVARIABLE(toks[i+3])))
                    if result == "Successfully multiplied":
                        i = i + 4
                    else:
                        break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "MULTIPLY VAR BY NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][4:]
                result = static_variable_multiplication(toks[i+1], float(toks[i+3][4:]))
                if result == "Successfully multiplied":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:4] == "MULTIPLY VAR BY EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][5:]
                result = static_variable_multiplication(toks[i+1], float(evalExpression(str(toks[i+3][5:]))))
                if result == "Successfully multiplied":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "DIVIDE VAR BY VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i+3][4:] in symbol_table:
                    result = static_variable_division(toks[i+1], float(getVARIABLE(toks[i+3])))
                    if result == "Successfully divided":
                        i = i + 4
                    else:
                        break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "DIVIDE VAR BY NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][4:]
                result = static_variable_division(toks[i+1], float(toks[i+3][4:]))
                if result == "Successfully divided":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:4] == "DIVIDE VAR BY EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][5:]
                result = static_variable_division(toks[i+1], float(evalExpression(str(toks[i+3][5:]))))
                if result == "Successfully divided":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "EXPONENTIATE VAR BY VAR":
                error_line_information = "Do Exp for" + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i+3][4:] in symbol_table:
                    result = static_variable_exponentiation(toks[i+1], float(getVARIABLE(toks[i+3])))
                    if result == "Successfully exponentiated":
                        i = i + 4
                    else:
                        break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "EXPONENTIATE VAR BY NUM":
                error_line_information = "Do Exp for" + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][4:]
                result = static_variable_exponentiation(toks[i+1], float(toks[i+3][4:]))
                if result == "Successfully exponentiated":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:4] == "EXPONENTIATE VAR BY EXPR":
                error_line_information = "Do Exp for" + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][5:]
                result = static_variable_exponentiation(toks[i+1], float(evalExpression(str(toks[i+3][5:]))))
                if result == "Successfully exponentiated":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "MODULATE VAR BY VAR":
                error_line_information = "Do Modulus for" + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i+3][4:] in symbol_table:
                    result = static_variable_modulation(toks[i+1], float(getVARIABLE(toks[i+3])))
                    if result == "Successfully modulated":
                        i = i + 4
                    else:
                        break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "MODULATE VAR BY NUM":
                error_line_information = "Do Modulus for" + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][4:]
                result = static_variable_modulation(toks[i+1], float(toks[i+3][4:]))
                if result == "Successfully modulated":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:4] == "MODULATE VAR BY EXPR":
                error_line_information = "Do Modulus for" + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][5:]
                result = static_variable_modulation(toks[i+1], float(evalExpression(str(toks[i+3][5:]))))
                if result == "Successfully modulated":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "FLOOR VAR BY VAR":
                error_line_information = "Do Flooring for" + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i+3][4:] in symbol_table:
                    result = static_variable_flooring(toks[i+1], float(getVARIABLE(toks[i+3])))
                    if result == "Successfully floored":
                        i = i + 4
                    else:
                        break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i + 3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "FLOOR VAR BY NUM":
                error_line_information = "Do Flooring for" + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][4:]
                result = static_variable_flooring(toks[i+1], float(toks[i+3][4:]))
                if result == "Successfully floored":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:4] == "FLOOR VAR BY EXPR":
                error_line_information = "Do Flooring for" + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + toks[i + 2] + " " + toks[i + 3][5:]
                result = static_variable_flooring(toks[i+1], float(evalExpression(str(toks[i+3][5:]))))
                if result == "Successfully floored":
                    i = i + 4
                else:
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_EQUAL_TO VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=" + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i+1][4:] and toks[i+3][4:] in symbol_table:
                    try:
                        if float(evalExpression(str(getVARIABLE(toks[i + 1])))) == float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                            del n_list[-1]
                            total_loops = total_loops - 1
                            i = i + 4
                        else:
                            if total_loops == len(n_list) and n_list != []:
                                i = n_list[-1]
                            else:
                                code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                                break
                    except NameError:
                        variable_1 = getVARIABLE(toks[i+1])
                        variable_1 = variable_1.upper()
                        variable_2 = getVARIABLE(toks[i + 3])
                        variable_2 = variable_2.upper()
                        if str(variable_1) == str(variable_2):
                            del n_list[-1]
                            total_loops = total_loops - 1
                            i = i + 4
                        else:
                            if total_loops == len(n_list) and n_list != []:
                                i = n_list[-1]
                            else:
                                code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_NOT_EQUAL_TO VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=/=" + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i + 1][4:] and toks[i + 3][4:] in symbol_table:
                    try:
                        if float(evalExpression(str(getVARIABLE(toks[i + 1])))) != float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                            del n_list[-1]
                            total_loops = total_loops - 1
                            i = i + 4
                        else:
                            if total_loops == len(n_list) and n_list != []:
                                i = n_list[-1]
                            else:
                                code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                                break
                    except NameError:
                        variable_1 = getVARIABLE(toks[i+1])
                        variable_1 = variable_1.upper()
                        variable_2 = getVARIABLE(toks[i + 3])
                        variable_2 = variable_2.upper()
                        if str(variable_1) != str(variable_2):
                            del n_list[-1]
                            total_loops = total_loops - 1
                            i = i + 4
                        else:
                            if total_loops == len(n_list) and n_list != []:
                                i = n_list[-1]
                            else:
                                code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                                break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_GREATER_THAN VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + ">" + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i + 1][4:] and toks[i + 3][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_LESS_THAN VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "<" + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i + 1][4:] and toks[i + 3][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_GREATER_THAN_OR_EQUAL_TO VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "> or =" + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i + 1][4:] and toks[i + 3][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_LESS_THAN_OR_EQUAL_TO VAR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "< or =" + " " + "Variable[" + toks[i + 3][4:] + "]"
                if toks[i + 1][4:] and toks[i + 3][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(evalExpression(str(getVARIABLE(toks[i + 3])))):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} or {toks[i+3][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_EQUAL_TO NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=" + " " + toks[i + 3][4:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) == float(toks[i + 3][4:]):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END,">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_NOT_EQUAL_TO NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=/=" + " " + toks[i + 3][4:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) != float(toks[i + 3][4:]):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_GREATER_THAN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + ">" + " " + toks[i + 3][4:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(toks[i + 3][4:]):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_LESS_THAN NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "<" + " " + toks[i + 3][4:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(toks[i + 3][4:]):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_GREATER_THAN_OR_EQUAL_TO NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "> or =" + " " + toks[i + 3][4:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(toks[i + 3][4:]):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:3] == "UNTIL VAR IS_LESS_THAN_OR_EQUAL_TO NUM":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "< or =" + " " + toks[i + 3][4:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(toks[i + 3][4:]):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:4] == "UNTIL VAR IS_EQUAL_TO EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=" + " " + toks[i + 3][5:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) == float(evalExpression(toks[i + 3][5:])):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END,">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:4] == "UNTIL VAR IS_NOT_EQUAL_TO EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=/=" + " " + toks[i + 3][5:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) != float(evalExpression(toks[i + 3][5:])):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END,">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:4] == "UNTIL VAR IS_GREATER_THAN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + ">" + " " + toks[i + 3][5:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) > float(evalExpression(toks[i + 3][5:])):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END,">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:4] == "UNTIL VAR IS_LESS_THAN EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "<" + " " + toks[i + 3][5:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) < float(evalExpression(toks[i + 3][5:])):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END,">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:4] == "UNTIL VAR IS_GREATER_THAN_OR_EQUAL_TO EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "> or =" + " " + toks[i + 3][5:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) >= float(evalExpression(toks[i + 3][5:])):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END,">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:4] == "UNTIL VAR IS_LESS_THAN_OR_EQUAL_TO EXPR":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "< or =" + " " + toks[i + 3][5:]
                if toks[i + 1][4:] in symbol_table:
                    if float(evalExpression(str(getVARIABLE(toks[i + 1])))) <= float(evalExpression(toks[i + 3][5:])):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END,">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:6] == "UNTIL VAR IS_EQUAL_TO STRING":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=" + " " + "\"" + toks[i + 3][7:] + "\""
                if toks[i + 1][4:] in symbol_table:
                    if str(getVARIABLE(toks[i + 1])) == str(toks[i + 3][7:]):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1][0:3] + " " + toks[i + 2] + " " + toks[i + 3][0:6] == "UNTIL VAR IS_NOT_EQUAL_TO STRING":
                error_line_information = toks[i] + " " + "Variable[" + toks[i + 1][4:] + "]" + " " + "=/=" + " " + "\"" + toks[i + 3][7:] + "\""
                if toks[i + 1][4:] in symbol_table:
                    if str(getVARIABLE(toks[i + 1])) != str(toks[i + 3][7:]):
                        del n_list[-1]
                        total_loops = total_loops - 1
                        i = i + 4
                    else:
                        if total_loops == len(n_list) and n_list != []:
                            i = n_list[-1]
                        else:
                            code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                            break
                else:
                    code_output.insert(END, f">>> Variable Error: {toks[i+1][4:]} is a variable that does not exist!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            elif toks[i] + " " + toks[i + 1] + " " + toks[i + 2] + " " + toks[i + 3] == "UNTIL THE LOOP BREAKS":
                error_line_information = error_array[-1] + " Until Infinity"
                if total_loops == len(n_list) and n_list != []:
                    i = n_list[-1]
                else:
                    code_output.insert(END, ">>> Loop Error: There is one or more Do This...Until loop(s) that you have not made properly!\n\n>>> THE PROGRAM HAS ENDED")
                    break
            else:
                code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
                code_output.insert(END, f">>> The Syntax Error comes after the line (or it is on the line): {error_line_information}\n\n")
                code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")
                break


    except ZeroDivisionError:
        code_output.insert(END, ">>> Division by Zero Error: In the Sofya Program there is a place where a number is being divided by zero!\n\n")
        code_output.insert(END, f">>> The Division by Zero Error is in the line: {error_line_information}\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")

    except TypeError:
        code_output.insert(END, ">>> Variable Storage Error: In the Sofya Program you have not stored things in a variable correctly!\n\n")
        code_output.insert(END, f">>> The Variable Storage Error is in the line: {error_line_information}\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")

    except ValueError:
        code_output.insert(END,">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
        code_output.insert(END,f">>> The Syntax Error is in the line: {error_line_information}\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")

    except NameError:
        code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
        code_output.insert(END, f">>> The Syntax Error is in the line: {error_line_information}\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")

    except SyntaxError:
        code_output.insert(END,">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
        code_output.insert(END, f">>> The Syntax Error is in the line: {error_line_information}\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")

    except AttributeError:
        code_output.insert(END, ">>> Syntax Error: In the Sofya Program, or in the input box, you have used something that does not follow the rules of Sofya!\n\n")
        code_output.insert(END, f">>> The Syntax Error comes after the line (or it is on the line): {error_line_information}\n\n")
        code_output.insert(END, ">>> THE PROGRAM HAS ENDED\n")


# '''

def run():
    code_output.delete("1.0", END)
    if file_path == "":
        messagebox.showinfo(title = "File Not Saved Error", message = "Please save your file before running it for the first time")
        return
    else:
        with open(file_path, "w") as file:
            code = editor.get("1.0", END)
            file.write(code)
            path = file_path

        file_data = read_file(path)
        toks_list = lexer(file_data)
        toks_list = parse_checker(toks_list)
        #print(toks_list)
        parse(toks_list)
        toks_list.clear()
        symbol_table.clear()


menu_bar = Menu(IDLE)

file_menu = Menu(menu_bar, tearoff = False)
file_menu.add_command(label = "Create New File", command = create_new_file)
file_menu.add_command(label = "Open File", command = open_file)
file_menu.add_command(label = "Save File", command = save_file)
file_menu.add_command(label = "Close File and Exit IDLE", command = exit_IDLE)
menu_bar.add_cascade(label = "File Options", menu = file_menu)

run_menu = Menu(menu_bar, tearoff = False)
run_menu.add_command(label = "Run Current File", command = run)
menu_bar.add_cascade(label = "Run Program", menu = run_menu)

IDLE.config(menu = menu_bar)

file_name_bar = Text(width = 152, height = 1, font=DesiredFont)
file_name_bar.insert("1.0", f"Name of Current File: {file_name_extracter(file_path)}")
file_name_bar.pack()
editor_header = Text(width = 152, height = 1, font=DesiredFont)
editor_header.insert("1.0", ">>> Program Editor <<<")
editor_header.pack()
editor = Text(width = 152, height = 20, font=DesiredFont, wrap="none")
editor.pack()
input_box_header = Text(width = 152, height = 1, font=DesiredFont)
input_box_header.insert("1.0", ">>> Input Box <<<")
input_box_header.pack()
input_box = Text(width = 152, height = 1, font=DesiredFont)
input_box.pack()
code_output_header = Text(width = 152, height = 1, font=DesiredFont)
code_output_header.insert("1.0", ">>> Program's Output <<<")
code_output_header.pack()
code_output = Text(width = 152, height = 11, font=DesiredFont, wrap="none")
code_output.pack()
IDLE.mainloop()