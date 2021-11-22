#!/usr/bin/python

def makePolyTable(one,two):
    page = '''
<!DOCTYPE html>
<html>
<table>
    _TABLE_
</table>
</html>
    '''
    lol = "<tr><th>x</th><th>y = x^3+3x^2+3x+1 </th></tr>\n\t"
    y = one
    while y <= two:
        lol += ("<tr><td>" + str(y) + "</td><td>" + str((y ** 3)+(3*y** 2)+(3*y)+1) + "</td></tr> \n\t")
        y += 1
    page = page.replace("_TABLE_",lol)
    return(page)
print(makePolyTable(5, 15))
