import math
from appJar import gui

app = gui("Prime Finder (Max 15 Digits)", "615x394")
app.setBg("dimgrey")
app.setFont(22)
app.addLabel("title", "Prime Finder (Max 15 Digits)")
app.addNumericEntry("Number")
app.setFocus("Number")
app.addLabel("Result", "")
app.setLabelBg("Result", "dimgrey")
app.setIcon("C:\\Users\\brady\\Desktop\\Downloads\\icon.ico")
app.setEntryMaxLength("Number", 15)

def press(button):
    if button == "Search Database":
        Submi()
    if button == "Close":
        app.stop()
    if button == "Paste":
        clip = 0
        clip = app.topLevel.clipboard_get()
        if int(clip) < 1000000000000000:
            app.setEntry("Number", clip, callFunction=True)
            Submi()
        else:
            app.setLabel("Result", "Entry Too Large")
        
def close(button):
    n = app.getEntry("Number")
    l = ClosestPrimes(n)
    oot = ClosestPrime(l, n)  
    app.setLabel("Result", oot)
         
def Submi():
        nbr = app.getEntry("Number")
        finalResult = Prime(nbr)
        if finalResult:
            app.setLabel("Result", "Prime")
        else:
            app.setLabel("Result", "Not Prime")
        
app.setFocus("Number")
app.addButtons(["Search Database", "Paste", "Close"], press) 
app.setResizable(canResize=False)
app.addButtons(["Search Database for Closest Prime"], close)       

def Prime(x):
    z=x/2
    isPrime=not int(z)==z
    
    if not isPrime and x > 2:
        return(isPrime)
    
    y=3
    sqx=math.sqrt(x)
    isPrime=True
    while y<=sqx and isPrime:
        z=x/y
        isPrime=not int(z)==z
        y=y+2
    return(isPrime)

def ClosestPrimes(x):
	closestPrimeDown = 2
	i = x
	b = 2
	changed = False
	while i >= b and changed == False:
		if Prime(i):
			closestPrimeDown = i
			changed = True
		i = i-1
	closestPrimeUp = 1000000000100011
	k = x
	f = 999999999999999
	change = False
	while k <= f and change == False:
		if Prime(k):
			closestPrimeUp = k
			change = True
		k = k+1
	return([closestPrimeDown, closestPrimeUp])
	
def ClosestPrime(closestPrimes, x):
    r = x - closestPrimes[0]
    e = closestPrimes[1] - x
    print(int(r), int(e))
    if int(r) < int(e):
        return(int(closestPrimes[0]))
    else:
        return(int(closestPrimes[1]))

app.go()