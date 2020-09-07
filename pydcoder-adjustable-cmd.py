# imported the modules i made earlier.
import codekey
import decode
print()
print("CODER AND DECODER V1.0 modular | by __ilprofessore ")
# taking the decision of the user.
decision = input("enter 0 to code or 1 to decode: ")
if decision == "0":
    codekey.code_module()
    input("press any key to exit;")
elif decision == "1":
    decode.decode_module()
    input("press any key to exit;")
else:
    print("wrong input, try again.")
# simple code, so far.