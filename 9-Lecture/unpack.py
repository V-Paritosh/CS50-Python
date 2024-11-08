#Unpacking
def total(galleons, sickles, knuts):
  return (galleons *17 + sickles) * 29 + knuts

coins = [100, 50, 25]
coins2 = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(*coins), "Knuts")
print(total(galleons=100, sickles=50, knuts=25), "Knuts")
print(total(**coins2), "Knuts")

def f(*args, **kwargs):
  print("Positional:", args)
  print("Named:", kwargs)

#args
f(100, 20, 25)
#kwargs
f(galleons=100, sickles=20, knuts=25)

