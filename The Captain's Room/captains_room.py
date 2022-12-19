grp_size = int(input())

s = input()
room_entries = list(map(lambda x: int(x), s.split(' ')))
captains_room = 0
room_cnt = {}
for i in room_entries:
    room_cnt[i] = room_cnt.get(i, 0) + 1

for c in room_cnt:
    if room_cnt[c]==1:
        captains_room = c
print(captains_room)
