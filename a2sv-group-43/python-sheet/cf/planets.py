from collections import defaultdict


test_case_count = int(input())
for test_case in range(test_case_count):
    [planet_count, shot_cost]  = [int(i) for i in input().split(' ')]

    planet_orbits = [int(i) for i in input().split(' ')]

    planets_per_orbit = defaultdict(int)

    for planet in range(planet_count):
        orbit = planet_orbits[planet]
        planets_per_orbit[orbit] += 1

    
    cost = 0
    
    for orbit in planets_per_orbit:
        current_planet_count = planets_per_orbit[orbit]
        if (current_planet_count >= shot_cost):
            cost += shot_cost
        else:
            cost += current_planet_count
    
    print(cost)

    

