def CD(N, list_of_tracks): #backtracking
    best_list = {'cost': 0, 'tracks': None}
    def rec(curr, path_to_curr, sum_until_curr):
        if sum_until_curr>N:
            return
        if len(path_to_curr) == len(list_of_tracks):
            if sum_until_curr>best_list['cost']:
                best_list['cost'] = sum_until_curr
                best_list['tracks'] = path_to_curr
        if curr+sum_until_curr > N:
            if sum_until_curr>best_list['cost']:
                best_list['cost'] = sum_until_curr
                best_list['tracks'] = path_to_curr
        for i in range(curr,len(list_of_tracks)):
            rec(i+1,f'{path_to_curr}{i}',sum_until_curr+list_of_tracks[i])
    rec(0, '', 0)
    return (best_list['cost'], [list_of_tracks[int(i)] for i in best_list['tracks']])

print(CD(5,[1,3,4]))
print(CD(10,[9,8,4,2]))
print(CD(20,[10,5,7,4]))
print(CD(90,[10, 23, 1, 2, 3, 4, 5, 7]))
print(CD(45,[4, 10, 44, 43, 12, 9, 8, 2]))

