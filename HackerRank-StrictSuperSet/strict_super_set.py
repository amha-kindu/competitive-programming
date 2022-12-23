# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set( input().split(' ') )
n = int( input() )

other_sets = []
for _ in range(n):
    std_input = input()
    other_sets.append( set(std_input.split(' ')) )

is_super_set = 'True'
for input_set in other_sets:
    if not set_A.issuperset(input_set):
        is_super_set = 'False'
        break
print(is_super_set)
