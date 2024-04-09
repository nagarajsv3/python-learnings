print("World {} {}".format("is","beautiful"))
print("world {0} {1} .{2} {3}".format("is","beautiful","go","live"))
print("{name} {i} {b}.{g} {l}".format(name="world", i="is", g="go", l="live", b="beautiful"))

#Float Formatting
rval=0.125364792
print("r value is {r:1.2f}".format(r=rval))

rval = 100.29083121212
print("r val is {r:1.2f}".format(r=rval))

#Formatted String Literals
hero="Krishna"
villain="Shakuni"
print(f"Mahabharata was driven by {hero} and {villain}")

nation="India"
year="2011"
print(f"Team {nation} won world cup in {year}")