"""Scheduler implements a course scheduling CSP.
    variables   A list of the courses to be scheduled
    domains     A dictionary in which the keys are the courses and the values are triples containing the possible
                professor/room/time combinations
    neighbors   All course pairs
    constraint_function: a function that returns false if the given variable values are conflicting
"""

from tools.aima.csp import CSP, min_conflicts


def create_timeroom_slots(times, rooms):
    timeroom_slots = []
    for time in times:
        for room in rooms:
            timeroom_slots.append((time, room))
    return timeroom_slots


def create_domains(courses, assignments, timeroom_slots):
    domains = {}
    for course in courses:
        dom = []
        prof = assignments[course]
        for slot in timeroom_slots:
            dom.append((prof, slot[0], slot[1]))
        domains[course] = dom
    return domains


def create_nonreflexive_neighbors(courses):
    neighbors = {}
    num_courses = len(courses)
    for i in range(num_courses):
        nbrs = []
        for j in range(i+1, num_courses):
            nbrs.append(courses[j])
        neighbors[courses[i]] = nbrs
    return neighbors


def schedule_constraint(course1, slot1, course2, slot2):
    #grab the details from each slot
    prof1 = slot1[0]
    time1 = slot1[1]
    room1 = slot1[2]
    prof2 = slot2[0]
    time2 = slot2[1]
    room2 = slot2[2]

    #make sure there aren't any time/room overlaps
    no_room_conflict = (time1 != time2) or (room1 != room2)

    #make sure there aren't any prof/time overlaps
    no_prof_conflict = (prof1 != prof2) or (time1 != time2)

    #only return true if there are no conflicts of either type
    return (no_room_conflict and no_prof_conflict)


#Set up some test data
courses = ['cs108', 'cs112', 'cs212', 'cs214', 'cs232', 'cs262', 'cs342']
faculty = ['adams', 'plantinga', 'bailey', 'schuurman']
assignments = {'cs108': 'schuurman', 'cs112': 'adams', 'cs212': 'plantinga', 'cs214': 'schuurman', 'cs232': 'adams', 'cs262': 'bailey', 'cs342': 'bailey'}
classtimes = ['mwf0900', 'mwf1030', 'mwf1130', 'mwf1230']
classrooms = ['nh253', 'sb382']
slots = create_timeroom_slots(classtimes, classrooms)
domains = create_domains(courses, assignments, slots)
neighbors = create_nonreflexive_neighbors(courses)

#Run it!
solution = min_conflicts(CSP(courses, domains, neighbors, schedule_constraint))

print('Variables: ' + str(courses))
print('Domains:')
for d in domains:
    print("\t{0}: {1}".format(d, domains[d]))
print('Neighbors (non-reflexive):')
for n in neighbors:
    print("\t{0}: {1}".format(n, neighbors[n]))
print('Solution:')
for s in solution:
    print("\t{0}: {1}".format(s, solution[s]))
# print(solution)
