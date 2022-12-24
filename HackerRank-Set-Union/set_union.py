# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int( input() )
eng_subs_roll_nums = set( input().split() )
m = int( input() )
french_subs_roll_nums = set( input().split() )

print( len(eng_subs_roll_nums.union(french_subs_roll_nums)))
