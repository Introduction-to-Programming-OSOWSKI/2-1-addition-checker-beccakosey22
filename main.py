#Create a function addCheck() That returns true/false if the sum given variables x and y correctly add up to z.
def addCheck(x, y, z):
    if x + y == z:
        return True
    else:
        return False
print(addCheck(6, 4, 10))