# Do_A1
def solve() :
    import sys
    import math

    input_data = sys.stdin.read().strip().split()
    if not input_data :
        return
    
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1 

    k = int(input_data[idx]); idx += 1

    participants = []
    for i in range(n) :
        name = input_data[idx]
        idx += 1
        scores = list(map(int, input_data[idx:idx+m]))
        idx += m
        participants.append((i, name, scores))

    def round_half_up(num, decimals=1):
        """
        소수점 아래 decimals자리에서 반올림 (무조건 0.5 이상이면 올림)
        """
        factor = 10 ** decimals
        return math.floor(num * factor + 0.5) / factor

    final_scores = []
    for (pid, name, scores) in participants :
        sorted_scores = sorted(scores)
        valid_scores = sorted_scores[k : m - k]
        avg_score = sum(valid_scores) / len(valid_scores)
        final_score = round_half_up(avg_score, 1)
        final_scores.append((pid, name, final_score))

    sorted_by_score = sorted(final_scores, key=lambda x: x[2], reverse=True)

    rank_dict = {}
    cur_rank = 1
    rank_dict[sorted_by_score[0][0]] = cur_rank
    prev_score = sorted_by_score[0][2]
    tie_count = 1

    for pos in range(1, len(sorted_by_score)) :
        pid, name, score = sorted_by_score[pos]
        if abs(score - prev_score) < 1e-9 :
            rank_dict[pid] = cur_rank
            tie_count += 1
        else:
            cur_rank += tie_count
            tie_count = 1
            rank_dict[pid] = cur_rank
            prev_score = score

    for (pid, name, score) in final_scores :
        print(rank_dict[pid], name, f"{score:.1f}")

if __name__ == "__main__" :
    solve()