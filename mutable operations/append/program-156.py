# Write a program to append scores of n players into list
# calculate totalscore,maximum score,min score
scores=[]
n=int(input("How many players ?"))
for i in range(n):
    s=int(input(f'Enter Player{i+1} Score :'))
    scores.append(s)
print(f'Players Score {scores}')
total=sum(scores)
max_score=max(scores)
min_score=min(scores)
print(f'Maximum Score {max_score}')
print(f'Minimum Score {min_score}')
print(f'Total Score {total}')