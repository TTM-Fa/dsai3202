from task import compute_power

results = []
for i in range(int(1e4)):
    results.append(compute_power.delay(i))
    

for result in results:
    results.get(timeout=10)
    
