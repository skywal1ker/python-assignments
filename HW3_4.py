"""7. Consider the Python function range(a,b). Label these statements as True or False.
_ Value âaâ is included in the range.
_ Value âbâ is included in the range."""



inp_value_a = int(input("Enter the value a: ")) 
inp_value_b = int(input("Enter the value b: ")) 

if inp_value_a and inp_value_b in range(0, 1000):
    print(True)
else:
    print(False)

