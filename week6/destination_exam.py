"""
QUESTION : You are given an array, paths, where each element paths[i] = [cityAᵢ, cityBᵢ] represents a direct route from cityAᵢ to cityBᵢ. Your task is to identify the final city on the route—the one that has no outgoing path to any other city. The structure of the routes is guaranteed to be a simple chain without loops, so there will be exactly one such destination.

Example 1:

Input: paths = [["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: You travel from “London” to “Sao Paulo” as follows: “London” -> “New York” -> “Lima” -> “Sao Paulo”. The city “Sao Paulo” has no outgoing route, so it’s the destination.
Example 2:

Input: paths = [["B","C"], ["D","B"], ["C","A"]]
Output: "A"
Explanation: Possible routes include “D” -> “B” -> “C” -> “A”, showing that “A” is the final city without any outgoing path.
Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAᵢ.length, cityBᵢ.length <= 10
cityAᵢ != cityBᵢ
All city names consist of letters (both uppercase and lowercase) and spaces. 
"""

# Solution one - O(n^2)
def dest_city(paths):
    for i in range(len(paths)):
        city_a = paths[i][0] # First city in the path London
        city_b = paths[i][1] # Second city in the path New York
        is_destination = True

        for j in range(len(paths)): 
            if i != j and paths[i][1] == paths[j][0]: # Path [i][1] = city_b is the same as path [j][0] = city_a
                                                        # If there is a path from city_b to another city, then city_b cannot be the destination
                                                        # here city_b will be last city in the path
                                                        # If there is a path from city_b to another city, then city_b cannot be the destination
                                                        # city_b is actually path[i][1] and city_a is path[i][0]
                                                        # there is loop therefore therefore last loop will check path[i][1] and going to another city if not break the loop and last city will be the destination
                break

        if is_destination:
            return city_b

    return None

print(dest_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))  # "Sao Paulo"
print(dest_city([["B", "C"], ["D", "B"], ["C", "A"]]))  # "A"
print(dest_city([["A", "Z"]]))

# Solution two - O(n)
def dest_city(paths):
    for path in paths:
        source = path[0] #