num = int(input())
vote = list(input())
print('A' if vote.count('A') > vote.count('B') else ('B' if vote.count('B') > vote.count('A') else 'Tie'))
