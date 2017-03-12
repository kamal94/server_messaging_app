vari = "hi";
def f():
	print(vari);
def g():
	global vari
	print(vari);

print("running f", f());
print("running g", g());
