import sys

program_name = sys.argv[0]

list_1 = []
for i in range(1, len(sys.argv)):
    arguments = sys.argv[i]
    list_1.append(arguments)

print("word count:", len(sys.argv) - 1)
print("Unsorted list")
print(*list_1, sep="\n")

list_1.sort()

print("sorted list")
print(*list_1, sep="\n")


