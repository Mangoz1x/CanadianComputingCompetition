# Inputs
# 1. Number of participants
# N. Participant N score

num_participants = int(input())
scores = []

for x in range(num_participants):
    score = int(input())
    scores.append(score)

# Remove all duplicate scores and then sort them from greatest to least
sorted_scores = sorted(list(set(scores)), reverse=True)

bronze = sorted_scores[2]
num_bronze = 0

for score in scores:
    if (score == bronze):
        num_bronze += 1

print(f'{bronze} {num_bronze}')
