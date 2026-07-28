def solution(genres, plays):
    answer = []
    
    g_hash = {}
    genre_plays = {}
    
    for i in range(len(genres)):
        # {"0": ["classic", 500] ..}
        g_hash[i] = (genres[i], plays[i])
    
        # {"classic": 1450, ...}
        if genres[i] in genre_plays:
            genre_plays[genres[i]] += plays[i]
        else: genre_plays[genres[i]] = plays[i]
    
    # 1. genre_plays 내림차순 기준 큰 것 타고 들어가서
    # 2. g_hash에서 해당 장르의 개별곡 -> 재생수 많은 것부터 수록
    
    # [["pop", 3100], ... ]
    sorted_plays = sorted(genre_plays.items(), key=lambda x: x[1], reverse=True)
    # [[3,["classic",800]], ... ]
    sorted_hash = sorted(g_hash.items(), key=lambda x: (x[1][0], -x[1][1]))
    
    # h[0] : 고유번호
    # h[1][0] : pop
    # h[1][1] : playtime
    
    for plays in sorted_plays:
        count = 0
        for h in sorted_hash:
            if plays[0] == h[1][0]:
                answer.append(int(h[0]))
                count += 1
            if count == 2:
                break
            
    return answer