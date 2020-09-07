# defining the main decode module.
def decode_module():
    # read the rules carefully and follow them to get a stable result.
    print("""
    
    enter the generated code to be decoded here;
    note that the decoded information is only in lowercase.
    
    """)
    # here the code is taken from the user.
    input_sentence = input("enter the code to be decoded: ")
    output_code = ""
    error_statement = ""
    # now, carefully modify the following code in accordance with the codekey
    # or the whole thing might get messed up.
    for letter in input_sentence:
        if letter == "1":
            output_code = output_code + "a"
        elif letter == "2":
            output_code = output_code + "b"
        elif letter == "3":
            output_code = output_code + "c"
        elif letter == "4":
            output_code = output_code + "d"
        elif letter == "5":
            output_code = output_code + "e"
        elif letter == "6":
            output_code = output_code + "f"
        elif letter == "7":
            output_code = output_code + "g"
        elif letter == "8":
            output_code = output_code + "h"
        elif letter == "9":
            output_code = output_code + "i"
        elif letter == "!":
            output_code = output_code + "j"
        elif letter == "@":
            output_code = output_code + "k"
        elif letter == "#":
            output_code = output_code + "l"
        elif letter == "$":
            output_code = output_code + "m"
        elif letter == "%":
            output_code = output_code + "n"
        elif letter == "^":
            output_code = output_code + "o"
        elif letter == "&":
            output_code = output_code + "p"
        elif letter == "*":
            output_code = output_code + "q"
        elif letter == "(":
            output_code = output_code + "r"
        elif letter == ")":
            output_code = output_code + "s"
        elif letter == "_":
            output_code = output_code + "t"
        elif letter == "+":
            output_code = output_code + "u"
        elif letter == "-":
            output_code = output_code + "v"
        elif letter == "=":
            output_code = output_code + "w"
        elif letter == "<":
            output_code = output_code + "x"
        elif letter == ">":
            output_code = output_code + "y"
        elif letter == "?":
            output_code = output_code + "z"
        elif letter == "|":
            output_code = output_code + " "
        elif letter == "`":
            output_code = output_code + ","
        elif letter == "~":
            output_code = output_code + "."
        else:
            if error_statement == "":
                error_statement = "invalid code, decode is deemed unstable."
                print(error_statement)
                output_code = ""
    if output_code != "":
        print("the code has been decoded to: " + output_code)
        # the code is as easy as cutting butter.
