# Name: Michael Shieh
# CSE 160
# Homework 4

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter

###
#  Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("E", "D")
print(practice_graph.neighbors("A"))

assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

# Test shape of practice graph
assert set(practice_graph.neighbors("A")) == set(["B", "C"])
assert set(practice_graph.neighbors("B")) == set(["A", "D", "C"])
assert set(practice_graph.neighbors("C")) == set(["A", "B", "D", "F"])
assert set(practice_graph.neighbors("D")) == set(["B", "C", "E", "F"])
assert set(practice_graph.neighbors("E")) == set(["D"])
assert set(practice_graph.neighbors("F")) == set(["C", "D"])


def draw_practice_graph(graph):
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(graph)
    plt.show()


# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
# draw_practice_graph(practice_graph)


###
#  Problem 1b
###

rj = nx.Graph()
rj.add_node("Juliet")
rj.add_edges_from(
    [("Juliet", "Nurse"), ("Juliet", "Tybalt"), ("Juliet", "Capulet"),
     ("Juliet", "Romeo"), ("Juliet", "Friar Laurence")])
rj.add_edges_from(
    [("Capulet", "Paris"), ("Capulet", "Tybalt"), ("Capulet", "Escalus")])
rj.add_edges_from(
    [("Romeo", "Friar Laurence"), ("Romeo", "Benvolio"),
     ("Romeo", "Montague"), ("Romeo", "Mercutio")])
rj.add_edges_from(
    [("Benvolio", "Montague"), ("Montague", "Escalus"), ("Escalus", "Paris"),
     ("Paris", "Mercutio"), ("Mercutio", "Escalus")])

assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

# Test shape of Romeo-and-Juliet graph
assert set(rj.neighbors("Nurse")) == set(["Juliet"])
assert set(rj.neighbors("Friar Laurence")) == set(["Juliet", "Romeo"])
assert set(rj.neighbors("Tybalt")) == set(["Juliet", "Capulet"])
assert set(rj.neighbors("Benvolio")) == set(["Romeo", "Montague"])
assert set(rj.neighbors("Paris")) == set(["Escalus", "Capulet", "Mercutio"])
assert set(rj.neighbors("Mercutio")) == set(["Paris", "Escalus", "Romeo"])
assert set(rj.neighbors("Montague")) == set(["Escalus", "Romeo", "Benvolio"])
assert set(rj.neighbors("Capulet")) == \
    set(["Juliet", "Tybalt", "Paris", "Escalus"])
assert set(rj.neighbors("Escalus")) == \
    set(["Paris", "Mercutio", "Montague", "Capulet"])
assert set(rj.neighbors("Juliet")) == \
    set(["Nurse", "Tybalt", "Capulet", "Friar Laurence", "Romeo"])
assert set(rj.neighbors("Romeo")) == \
    set(["Juliet", "Friar Laurence", "Benvolio", "Montague", "Mercutio"])


def draw_rj(graph):
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(graph)
    plt.savefig("romeo-and-juliet.pdf")
    # plt.show()


# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
draw_rj(rj)


###
#  Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


assert friends(rj, "Mercutio") == set(['Romeo', 'Escalus', 'Paris'])


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given
    graph. The result does not include the given user nor any of that user's
    friends.
    """
    user_friends = friends(graph, user)
    user_friends_of_friends = set()

    for person in user_friends:
        for friend in friends(graph, person):
            user_friends_of_friends.add(friend)

    user_friends_of_friends.discard(user)

    for person in user_friends:
        user_friends_of_friends.discard(person)

    return user_friends_of_friends


assert friends_of_friends(rj, "Mercutio") == \
    set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common.
    """
    mutual = set()
    for person in friends(graph, user1):
        if person in friends(graph, user2):
            mutual.add(person)

    return mutual


assert common_friends(practice_graph, "A", "B") == set(['C'])
assert common_friends(practice_graph, "A", "D") == set(['B', 'C'])
assert common_friends(practice_graph, "A", "E") == set([])
assert common_friends(practice_graph, "A", "F") == set(['C'])
assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping a person to the number of friends
    that person has in common with the given user. The map keys are the
    people who have at least one friend in common with the given user,
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "X"
    Here is what is relevant about my_graph:
        - "X" and "Y" have two friends in common
        - "X" and "Z" have one friend in common
        - "X" and "W" have one friend in common
        - "X" and "V" have no friends in common
        - "X" is friends with "W" (but not with "Y" or "Z")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "X")  =>   { 'Y':2, 'Z':1 }
    """
    map = {}
    for friend in friends_of_friends(graph, user):
        if len(common_friends(graph, user, friend)) >= 1:
            map[friend] = len(common_friends(graph, user, friend))

    return map


assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}
assert number_of_common_friends_map(rj, "Mercutio") == \
    {'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1,
     'Juliet': 1, 'Montague': 2}


def number_map_to_sorted_list(map_with_number_vals):
    """Given map_with_number_vals, a dictionary whose values are numbers,
    return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.
    """
    sorted_lst = sorted(sorted(
        map_with_number_vals.items(), key=itemgetter(0)), key=itemgetter(1),
        reverse=True)

    lst = [list(i)[0] for i in sorted_lst]

    return lst


assert number_map_to_sorted_list({"a": 5, "b": 2, "c": 7, "d": 5, "e": 5}) == \
    ['c', 'a', 'd', 'e', 'b']


def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """

    lst = number_map_to_sorted_list(number_of_common_friends_map(graph, user))
    return lst


assert recommend_by_number_of_common_friends(practice_graph, "A") == ['D', 'F']
assert recommend_by_number_of_common_friends(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
#  Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person to their
    influence score, with respect to the given user. The map only
    contains people who have at least one friend in common with the given
    user and are neither the user nor one of the users's friends.
    See the assignment writeup for the definition of influence scores.
    """
    potential_friends = friends_of_friends(graph, user)
    map = {}
    for name in potential_friends:
        mutual = common_friends(graph, user, name)
        influence = 0
        for person in mutual:
            influence = influence + 1/len(friends(graph, person))
        map[name] = influence

    return map


assert influence_map(rj, "Mercutio") == \
    {'Benvolio': 0.2, 'Capulet': 0.5833333333333333,
     'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45}


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    sorted_lst = sorted(sorted(
        influence_map(graph, user).items(), key=itemgetter(0)),
        key=itemgetter(1), reverse=True)

    lst = [list(i)[0] for i in sorted_lst]

    return lst


assert recommend_by_influence(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


def txt_to_line(line):
    row = []
    for element in line.split('\t'):
        row.append(element)

    return row


def make_facebook_graph(infile):
    input = open(infile)
    graph = nx.Graph()
    content = [txt_to_line(row) for row in input]

    for row in content:
        graph.add_edge(int(row[0]), int(row[1]))

    return graph


def run_recommondation(num, function, graph):
    # if num % 1000 == 0:
    lst = function(graph, num)
    if len(lst) > 10:
        lst = lst[0:10]

    return lst


###
#  Problem 4
###

print("Problem 4:")
print()

# (Your Problem 4 code goes here.)
same_list = []
not_same_list = []

for name in rj.nodes():
    tmp = recommend_by_influence(rj, name)
    tmp2 = recommend_by_number_of_common_friends(rj, name)
    if tmp == tmp2:
        same_list.append(name)
    else:
        not_same_list.append(name)

print("Unchanged Recommendation:", sorted(same_list))
print("Changed Recommendation:", sorted(not_same_list))

###
#  Problem 5
###

# (Your Problem 5 code goes here.)

infile = "facebook-links.txt"
facebook = make_facebook_graph(infile)

# assert len(facebook.nodes()) == 63731
# assert len(facebook.edges()) == 817090

# assert run_recommondation(
#    28000, recommend_by_number_of_common_friends, facebook) ==\
#    [23, 1445, 4610, 7996, 10397, 11213, 56, 85, 471, 522]
# assert run_recommondation(
#    29000, recommend_by_number_of_common_friends, facebook) ==\
#    [28606]
# assert run_recommondation(
#    30000, recommend_by_number_of_common_friends, facebook) ==\
#    [862, 869, 919, 941, 3154, 8180, 8269, 8614, 14473, 14495]

# assert run_recommondation(28000, recommend_by_influence, facebook) ==\
#    [7033, 17125, 15462, 33049, 51105, 16424, 23, 7996, 725, 1539]
# assert run_recommondation(29000, recommend_by_influence, facebook) ==\
#    [28606]
# assert run_recommondation(30000, recommend_by_influence, facebook) ==\
#    [862, 869, 919, 941, 3154, 8269, 14473, 14495, 17951, 19611]

dict_ncf = {}
dict_inf = {}

for num in facebook.nodes():
    if num % 1000 == 0:
        # print(num, "(by number_of_common_friends):", run_recommondation(
        #    num, recommend_by_number_of_common_friends, facebook))
        dict_ncf[num] = run_recommondation(
            num, recommend_by_number_of_common_friends, facebook)
        dict_inf[num] = run_recommondation(
            num, recommend_by_influence, facebook)

###
#  Problem 6
###
print()
print("Problem 6:")
print()

for key in sorted(dict_ncf.keys()):
    print(key, "(by number_of_common_friends):", dict_ncf[key])

###
#  Problem 7
###
print()
print("Problem 7:")
print()

# for num in facebook.nodes():
#    if num % 1000 == 0:
#        print(num, "(by influence):", run_recommondation(
#            num, recommend_by_influence, facebook))

for key in sorted(dict_inf.keys()):
    print(key, "(by influence):", dict_inf[key])

###
#  Problem 8
###
print()
print("Problem 8:")
print()

same_list = []
not_same_list = []

# for num in facebook.nodes():
for key in dict_inf.keys():
    # if num % 1000 == 0:
    #    tmp = recommend_by_influence(facebook, num)
    #    tmp2 = recommend_by_number_of_common_friends(facebook, num)
    if dict_inf[key] == dict_ncf[key]:
        same_list.append(key)
    else:
        not_same_list.append(key)

print("Same:", same_list)
print("Different:", not_same_list)

###
#  Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").
