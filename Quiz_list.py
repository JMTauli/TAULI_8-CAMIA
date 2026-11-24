# ACTIVITY 1 - STUDENT QUIZ SCORE ANALYZER
# TAULI, JAIDEN
# 8 - CAMIA

scores = []

for i in range(1,6):
    quiz_score = int(input(f"Enter your on quiz {i}: "))
    scores.append(quiz_score)

print("========== QUIZ SCORE REPORT ==========")
print(f"QUIZ SCORES: {scores}")
print(f"TOTAL SCORES: {sum(scores)}")
print(f"HIGHEST SCORE: {max(scores)}")
print(f"LOWEST SCORE: {min(scores)}")
print(f"ASCENDING ORDER: {sorted(scores)}")
print(f"DESCENDING ORDER: {sorted(scores, reverse=True)}")
print(f"ORIGINAL SCORES: {scores}")