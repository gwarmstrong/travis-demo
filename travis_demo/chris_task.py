
def hello_world(name=""):

    if name:
        return('Hello ' + name[0].upper() + name[1:].lower() + '!')

    else:
        return('Hello world!')
