for i in range(int(raw_input())):
    candidate_count, region_count = map(int, raw_input().split(' '))
    candidates = [0] * candidate_count
    for r in range(region_count):
        votes = map(int, raw_input().split(' '))
        for i in range(candidate_count):
            candidates[i] += votes[i]
    print(candidates.index(max(candidates)) + 1)