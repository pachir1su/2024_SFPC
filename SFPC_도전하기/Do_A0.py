# Do_A0
def solve():
    import math

    participants = [
        ("narang",   [92, 91, 90, 88, 94, 90, 88, 87]),
        ("arang",    [93, 95, 90, 88, 95, 89, 90, 89]),
        ("danghak",  [96, 91, 91, 91, 90, 93, 90, 91]),
        ("meodol",   [90, 90, 91, 97, 90, 91, 90, 91]),
        ("geumdong", [88, 82, 88, 88, 87, 88, 91, 85]),
    ]

    k = 2


    def custom_round_half_up(value, decimals=1):
        """ Banker's rounding을 피하고, 0.5 이상이면 올림하는 방식을 직접 구현 """
        factor = 10 ** decimals
        return math.floor(value * factor + 0.5) / factor

    final_scores = []
    for i, (name, scores) in enumerate(participants):
        sorted_scores = sorted(scores)

        valid = sorted_scores[k : len(scores) - k]
        
        avg = sum(valid) / len(valid)
        avg_rounded = custom_round_half_up(avg, 1) 
        
        final_scores.append((i, name, avg_rounded))

    sorted_by_score = sorted(final_scores, key=lambda x: x[2], reverse=True)
    
    rank_dict = {}
    current_rank = 1
    rank_dict[sorted_by_score[0][0]] = current_rank
    prev_score = sorted_by_score[0][2]
    ties_count = 1
    
    for pos in range(1, len(sorted_by_score)):
        idx, pname, score = sorted_by_score[pos]
        if abs(score - prev_score) < 1e-9:
            rank_dict[idx] = current_rank
            ties_count += 1
        else:
            current_rank += ties_count
            ties_count = 1
            rank_dict[idx] = current_rank
            prev_score = score

    for (i, name, score) in final_scores :
        print(f"{rank_dict[i]} {name} {score:.1f}")


if __name__ == "__main__" :
    solve()