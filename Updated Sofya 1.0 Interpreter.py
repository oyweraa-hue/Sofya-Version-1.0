# Sofya was first created by Timothy Oywera on December 2023
try:
    from sys import *

    tokens = []
    symbol_table = {}
    run_file = input("Which file do you want to run? ")


    def evalExpression(expression):
        return eval(expression)


    def doASSIGN(varname, varvalue):
        symbol_table[varname[4:]] = varvalue


    def getVARIABLE(varname):
        varname = varname[4:]
        if varname in symbol_table:
            return symbol_table[varname]
        else:
            return f">>> Variable Error: {varname} is an undefined Variable"
            exit()


    def getINPUT(string, varname):
        symbol_table[varname] = input(string + " ")


    def open_file(filename):
        data = open(filename, "r").read()
        return data


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
        number = ""
        number_recall = 0

        filecontents = list(filecontents)
        for character in filecontents:
            token = token + character
            token = token.upper()
            #print(token)
            if token == "START" and state == 0:
                tokens.append("WRITE")
                tokens.append("STRING:" + ">>> THE PROGRAM HAS STARTED...")
                tokens.append("WRITE")
                tokens.append("STRING:" + " ")
                tokens.append("START")
                token = ""
            elif token == " ":
                if varstarted == 1:
                    tokens.append("VAR:" + var)
                    varstarted = 0
                    var = ""
                    token = ""
                elif state == 0:
                    token = ""
                elif state == 1:
                    token = " "
            elif token == "\n":
                if expr != "" and isexpr == 1:
                    tokens.append("EXPR:" + expr)
                    isexpr = 0
                    expr = ""
                elif expr != "" and isexpr == 0:
                    tokens.append("NUM:" + expr)
                    expr = ""
                token = ""
            elif token == "IS" and state == 0:
                tokens.append("EQUALS")
                token = ""
            elif token == "VARIABLE " and state == 0:
                if varstarted == 0:
                    varstarted = 1
                token = ""
            elif varstarted == 1:
                var = var + token
                token = ""
            elif token == "WRITE" and state == 0:
                tokens.append("WRITE")
                token = ""
            elif token == "SAY" and state == 0:
                tokens.append("SAY")
                token = ""
            elif token == "ALSO SAY" and state == 0:
                tokens.append("&")
                token = ""
            elif token == "BETWEEN" and state == 0:
                tokens.append("BETWEEN")
                token = ""
            elif token == "FROM" and state == 0:
                tokens.append("FROM")
                token = ""
            elif token == "TO" and state == 0:
                tokens.append("TO")
                token = ""
            elif token == "AND" and state == 0:
                tokens.append("AND")
                token = ""
            elif token == "=" and state == 0:
                tokens.append("IS_EQUAL_TO")
                token = ""
            elif token == ">" and state == 0:
                tokens.append("IS_GREATER_THAN")
                token = ""
            elif token == "<" and state == 0:
                tokens.append("IS_LESS_THAN")
                token = ""
            elif token == "_>_" and state == 0:
                tokens.append("IS_GREATER_THAN_OR_EQUAL_TO")
                token = ""
            elif token == "_<_" and state == 0:
                tokens.append("IS_LESS_THAN_OR_EQUAL_TO")
                token = ""
            elif token == "!=" and state == 0:
                tokens.append("IS_NOT_EQUAL_TO")
                token = ""
            elif token == "ENDIF" and state == 0:
                tokens.append("ENDIF")
                token = ""
            elif token == "IF" and state == 0:
                tokens.append("IF")
                token = ""
            elif token == "OTHERWISE" and state == 0:
                token = "" #Here, the word "otherwise" has been ignored to make the program less complicated
            elif token == "BREAK THE LOOP" and state == 0:
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
            elif token == "ASKCOMPUTERUSER" and state == 0:
                tokens.append("INPUT")
                token = ""
            elif token == "STORE THE ANSWER IN" and state == 0:
                tokens.append("STOREIN")
                token = ""
            elif token == "DO THIS" and state == 0:
                tokens.append("REPEAT")
                token = ""
            elif token == "UNTIL" and state == 0:
                tokens.append("UNTIL")
                token = ""
            elif token == "{" and state == 0:
                tokens.append("{")
                token = ""
            elif token == "}" and state == 0:
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
                tokens.append("VAR:" + var)
                var = ""
                var_recall = 0
                token = ""
            elif token == "VARIABLE[" and state == 0:
                if var_recall == 0:
                    var_recall = 1
                token = ""
            elif var_recall == 1:
                var = var + token
                token = ""
            elif token == "]" and state == 0 and number_recall == 1:
                tokens.append("NUM:" + number)
                number = ""
                number_recall = 0
                token = ""
            elif token == "NUMBER[" and state == 0:
                if number_recall == 0:
                    number_recall = 1
                token = ""
            elif number_recall == 1:
                number = number + token
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
                elif state == 0:
                    tokens.append("CONSTANT:" + str(3.14159265358979323846))
                token = ""
            elif token == "CONSTANT[C]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(299792458))
                token = ""
            elif token == "CONSTANT[H]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(evalExpression(str(6.62607015*10**-34))))
                token = ""
            elif token == "CONSTANT[EO]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(evalExpression(str(8.854187812813*10**-12))))
                token = ""
            elif token == "CONSTANT[G]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(evalExpression(str(6.6743015*10**-11))))
                token = ""
            elif token == "CONSTANT[KE]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(evalExpression(str(8.987551792314*10**9))))
                token = ""
            elif token == "CONSTANT[G_E]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(9.80665))
                token = ""
            elif token == "CONSTANT[ATM]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(101325))
                token = ""
            elif token == "CONSTANT[M_E]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(evalExpression(str(9.109383701528*10**-31))))
                token = ""
            elif token == "CONSTANT[M_P]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(evalExpression(str(1.6726219236951*10**-27))))
                token = ""
            elif token == "CONSTANT[M_N]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(evalExpression(str(1.6749274980495*10**-27))))
                token = ""
            elif token == "CONSTANT[M_P:M_E]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(1836.1526734311))
                token = ""
            elif token == "CONSTANT[N_A]" or token == "CONSTANT[L]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(evalExpression(str(6.02214076*10**23))))
                token = ""
            elif token == "CONSTANT[R]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(8.31446261815324))
                token = ""
            elif token == "CONSTANT[F]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(96485.3321233100184))
                token = ""
            elif token == "CONSTANT[R_E]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(evalExpression(str(2.817940326213*10**-15))))
                token = ""
            elif token == "CONSTANT[PHI]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(1.61803398874989484820))
                token = ""
            elif token == "CONSTANT[E]" and varstarted == 0 and var_recall == 0 and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
                    tokens.append("CONSTANT:" + str(2.71828182845904523536))
                token = ""
            elif token == "+" or token == "-" or token == "/" or token == "*" or token == "(" or token == ")" and state == 0:
                if state == 1:
                    string = string + token
                elif state == 0:
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
                    tokens.append("STRING:" + string)
                    string = ""
                    state = 0
                    token = ""
            elif state == 1:
                    string = string + token
                    token = ""
            elif token == "STOP" and state == 0:
                tokens.append("WRITE")
                tokens.append("STRING:" + " ")
                tokens.append("WRITE")
                tokens.append("STRING:" + ">>> THE PROGRAM HAS ENDED")
                tokens.append("STOP")
                token = ""

        #print(tokens)
        return tokens

    #'''''
    def parse(toks):
        i = 0
        total_conditions = 0
        false_conditions = 0
        while i < len(toks):
            #print(toks[i])
            if toks[i] == "ENDIF":
                i = i+1
                total_conditions = 0
                false_conditions = 0
            elif toks[i] == "START" or toks[i] == "STOP":
                i = i+1
            elif toks[i] == "{" or toks[i] == "}":
                i = i+1
            elif toks[i] == "REPEAT":
                n = i+1
                i = i+1
            elif toks[i] == "BREAK_THE_LOOP":
                while i < len(toks) and toks[i] != "UNTIL":
                    i = i+1
                    if toks[i] == "UNTIL":
                        i = i+4
                        break
            elif toks[i] + " " + toks[i+1][0:6] == "WRITE STRING" or toks[i] + " " + toks[i+1][0:3] == "WRITE NUM" or toks[i] + " " + toks[i+1][0:4] == "WRITE EXPR" or toks[i] + " " + toks[i+1][0:3] == "WRITE VAR" or toks[i] + " " + toks[i+1][0:8] == "WRITE CONSTANT":
                if toks[i+1][0:6] == "STRING":
                    print(toks[i+1][7:])
                elif toks[i+1][0:3] == "NUM":
                    print(toks[i+1][4:])
                elif toks[i+1][0:4] == "EXPR":
                    print(evalExpression(toks[i+1][5:]))
                elif toks[i+1][0:3] == "VAR":
                    print(getVARIABLE(toks[i+1]))
                elif toks[i+1][0:8] == "CONSTANT":
                    print(toks[i+1][9:])
                i = i+2
            elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " + toks[i+3][0:3] == "SAY STRING & VAR" or toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:6] == "SAY VAR & STRING" or toks[i] + " " + toks[i+1][0:8] + " " + toks[i+2] + " " + toks[i+3][0:6] == "SAY CONSTANT & STRING" or toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " + toks[i+3][0:8] == "SAY STRING & CONSTANT":
                if toks[i+1][0:6] == "STRING" and toks[i+3][0:8] != "CONSTANT":
                    print(toks[i+1][7:] + " " + str(getVARIABLE(toks[i+3])))
                elif toks[i+1][0:8] == "CONSTANT":
                    print(toks[i+1][9:] + " " + toks[i+3][7:])
                elif toks[i+1][0:6] == "STRING" and toks[i+3][0:8] == "CONSTANT":
                    print(toks[i+1][7:] + " " + toks[i+3][9:])
                elif toks[i+1][0:3] == "VAR":
                    print(str(getVARIABLE(toks[i+1])) + " " + toks[i+3][7:])
                i = i+4
            elif toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:6] == "VAR EQUALS STRING" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS NUM" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:4] == "VAR EQUALS EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] == "VAR EQUALS VAR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] + " " + toks[i+3][0:4] == "VAR EQUALS VAR EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] + " " + toks[i+3][0:3] + " " + toks[i+4][0:4] == "VAR EQUALS VAR VAR EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:8] + " " + toks[i+3][0:4] == "VAR EQUALS CONSTANT EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:8] + " " + toks[i+3][0:3] + " " + toks[i+4][0:4] == "VAR EQUALS CONSTANT VAR EXPR" or toks[i][0:3] + " " + toks[i+1] + " " + toks[i+2][0:3] + " " + toks[i+3][0:8] + " " + toks[i+4][0:4] == "VAR EQUALS VAR CONSTANT EXPR":
                if toks[i+2][0:3] == "VAR" and toks[i+3][0:4] == "EXPR":
                    doASSIGN(toks[i], float(evalExpression("(" + (str(evalExpression(str(getVARIABLE(toks[i+2]))))) + ")" + toks[i+3][5:])))
                    i = i+4
                elif toks[i+2][0:8] == "CONSTANT" and toks[i+3][0:4] == "EXPR":
                    doASSIGN(toks[i], float(evalExpression(toks[i+2][9:] + toks[i+3][5:])))
                    i = i+4
                elif toks[i+2][0:3] == "VAR" and toks[i+3][0:3] == "VAR" and toks[i+4][0:4] == "EXPR":
                    doASSIGN(toks[i], float(evalExpression("(" + (str(evalExpression(str(getVARIABLE(toks[i+2]))))) + ")" + toks[i+4][5:] + str(evalExpression(str(getVARIABLE(toks[i+3])))))))
                    i = i+5
                elif toks[i+2][0:3] == "VAR" and toks[i+3][0:8] == "CONSTANT" and toks[i+4][0:4] == "EXPR":
                    doASSIGN(toks[i], float(evalExpression((str(evalExpression(str(getVARIABLE(toks[i+2])))) + toks[i+4][5:] + toks[i+3][9:]))))
                    i = i+5
                elif toks[i+2][0:8] == "CONSTANT" and toks[i+3][0:3] == "VAR" and toks[i+4][0:4] == "EXPR":
                    doASSIGN(toks[i], float(evalExpression((toks[i+2][9:] + toks[i+4][5:] + str(evalExpression(str(getVARIABLE(toks[i+3]))))))))
                    i = i+5
                elif toks[i+2][0:6] == "STRING":
                    doASSIGN(toks[i], toks[i+2][7:])
                    i = i+3
                elif toks[i+2][0:3] == "NUM":
                    doASSIGN(toks[i], float(toks[i+2][4:]))
                    i = i+3
                elif toks[i+2][0:4] == "EXPR":
                    doASSIGN(toks[i], float(evalExpression(toks[i+2][5:])))
                    i = i+3
                elif toks[i+2][0:3] == "VAR":
                    doASSIGN(toks[i], evalExpression(str(getVARIABLE(toks[i+2]))))
                    i = i+3
            elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " + toks[i+3][0:3] == "INPUT STRING STOREIN VAR":
                getINPUT(toks[i+1][7:], toks[i+3][4:])
                i = i+4
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "IF VAR IS_EQUAL_TO VAR THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) == float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+5
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "IF VAR IS_GREATER_THAN VAR THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) > float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+5
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "IF VAR IS_LESS_THAN VAR THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) < float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+5
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "IF VAR IS_GREATER_THAN_OR_EQUAL_TO VAR THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) >= float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+5
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "IF VAR IS_LESS_THAN_OR_EQUAL_TO VAR THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) <= float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+5
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] + " " + toks[i+4] == "IF VAR IS_NOT_EQUAL_TO VAR THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) != float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+5
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3] + " " + toks[i+4][0:3] + " " + toks[i+5] + " " + toks[i+6][0:3] + " " + toks[i+7] == "IF VAR EQUALS FROM NUM TO NUM THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) >= float(evalExpression(str(toks[i+4][4:]))) and float(evalExpression(str(getVARIABLE(toks[i+1])))) <= float(evalExpression(str(toks[i+6][4:]))):
                    i = i+8
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3] + " " + toks[i+4] + " " + toks[i+5][0:3] + " " + toks[i+6] + " " + toks[i+7][0:3] + " " + toks[i+8] == "IF VAR EQUALS FROM AFTER NUM TO NUM THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) > float(evalExpression(str(toks[i+5][4:]))) and float(evalExpression(str(getVARIABLE(toks[i+1])))) <= float(evalExpression(str(toks[i+7][4:]))):
                    i = i+9
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3] + " " + toks[i+4][0:3] + " " + toks[i+5] + " " + toks[i+6] + " " + toks[i+7][0:3] + " " + toks[i+8] == "IF VAR EQUALS FROM NUM TO BEFORE NUM THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) >= float(evalExpression(str(toks[i+4][4:]))) and float(evalExpression(str(getVARIABLE(toks[i+1])))) < float(evalExpression(str(toks[i+7][4:]))):
                    i = i+9
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3] + " " + toks[i+4][0:3] + " " + toks[i+5] + " " + toks[i+6][0:3] + " " + toks[i+7] == "IF VAR EQUALS BETWEEN NUM AND NUM THEN":
                total_conditions = total_conditions + 1
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) > float(evalExpression(str(toks[i+4][4:]))) and float(evalExpression(str(getVARIABLE(toks[i+1])))) < float(evalExpression(str(toks[i+6][4:]))):
                    i = i+8
                else:
                    false_conditions = false_conditions + 1
                    while i < len(toks) and (toks[i] != "ENDIF" or toks[i] != "IF"):
                        i = i+1
                        if toks[i] == "ENDIF":
                            i = i+1
                            total_conditions = 0
                            false_conditions = 0
                            break
                        elif toks[i] == "IF":
                            break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3] + " " + toks[i+4] + " " + toks[i+5] == "IF VAR EQUALS ANYTHING ELSE THEN" and total_conditions == false_conditions:
                i = i+6
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3] + " " + toks[i+4] + " " + toks[i+5] == "IF VAR EQUALS ANYTHING ELSE THEN" and total_conditions != false_conditions:
                while i < len(toks) and toks[i] != "ENDIF":
                    i = i+1
                    if toks[i] == "ENDIF":
                        i = i+1
                        total_conditions = 0
                        false_conditions = 0
                        break
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "UNTIL VAR IS_EQUAL_TO VAR":
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) == float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+4
                else:
                    i = n
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "UNTIL VAR IS_NOT_EQUAL_TO VAR":
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) != float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+4
                else:
                    i = n
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "UNTIL VAR IS_GREATER_THAN VAR":
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) > float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+4
                else:
                    i = n
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "UNTIL VAR IS_LESS_THAN VAR":
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) < float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+4
                else:
                    i = n
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "UNTIL VAR IS_GREATER_THAN_OR_EQUAL_TO VAR":
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) >= float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+4
                else:
                    i = n
            elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2] + " " + toks[i+3][0:3] == "UNTIL VAR IS_LESS_THAN_OR_EQUAL_TO VAR":
                if float(evalExpression(str(getVARIABLE(toks[i+1])))) <= float(evalExpression(str(getVARIABLE(toks[i+3])))):
                    i = i+4
                else:
                    i = n
            
    #'''''

    def run():
        data = open_file(run_file + ".txt")
        toks_list = lexer(data)
        parse(toks_list)

    run()

except FileNotFoundError:
    print(">>> File Not Found Error!: Sofya was not able to find the file you are trying to run because it might not exist or you might have typed the file name wrongly.")

except IndexError:
    print(">>> Syntax Error!: In the Sofya program, you have used something that does not follow the rules of Sofya.")
    print(">>> Program Run Error: Maybe your program does not have 'Start' or 'Stop'")

except ZeroDivisionError:
    print(">>> Division By Zero Error!: There is a place in the Sofya program where a number is divided by zero.")
