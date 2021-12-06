genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    albums_total = {}
    albums = {}

    for i in range(len(genres)):
        albums_total[genres[i]] = albums_total.get(genres[i], 0) + plays[i]
        albums[genres[i]] = albums.get(genres[i], []) + [(plays[i], i)]

    genreSort = sorted(albums_total.items(), key = lambda x: -x[1])

    for (genre, play) in genreSort:
        albums[genre] = sorted(albums[genre], key = lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in albums[genre][:2]]

    return answer

print(solution(genres, plays))