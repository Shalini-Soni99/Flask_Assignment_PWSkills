from flask import Flask , render_template , request 

app = Flask('__name__')


def calcultor_test():
    ops = request.form('operation')
    num1 = request.form('num1')
    num2 = request.form('num2')
    if( ops == 'add'):
        r = num1 + num2
        return f"The addition of {num1} and {num2} is {r}"


    if( ops == 'sub'):
        r = num1-num2
        return f"The difference of {num1} and {num2} is {r}"
    
    if( ops == 'multilply')
        r = num1*num2
        return f"The product of {num1} and {num2} is {r}"
    
                   