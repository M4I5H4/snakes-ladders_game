# def greet(name):
#     """
#     This function greets to
#     the person passed in as
#     a parameter
#     """
#     print("Hello, " + name + ". Good morning!")

# greet('Paul')

def createListContent():
    innerList = []
    innerContent = None
    i = 0
    j = 0

    while i < 10:
        innerList.append(innerContent)
        i += 1

    outerList = []
    while j < 10:
        outerList.append(innerList)
        j += 1
    
    return outerList

# print(createListContent())
    

