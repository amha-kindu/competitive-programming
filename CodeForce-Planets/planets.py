from collections import Counter

n = int( input() )
for _ in range(n):
    _, machine_2_cost = tuple( input().split() )
    planets = input().split()
    machine_2_cost = int(machine_2_cost)

    planet_cnt = Counter(planets)
    cost = 0 

    while planet_cnt:
        orbit_id = next(iter(planet_cnt))
    
        if planet_cnt[orbit_id] > machine_2_cost:
            cost += machine_2_cost
        else:
            cost += planet_cnt[orbit_id]
        planet_cnt.pop(orbit_id)

    print(cost)

