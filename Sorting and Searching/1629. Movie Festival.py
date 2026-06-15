# 1629. Movie Festival

def maxMovieWatchingPossible(n: int, movieTimings: list) -> int:

    movieTimings.sort(key=lambda x:x[1])

    count = 0
    lastMovieEndTime = -1
    for movieTime in movieTimings:
        if movieTime[0] >= lastMovieEndTime:
            count += 1
            lastMovieEndTime = movieTime[1]

    return(count) 

def main():
    n = int(input())
    movieTimings = []
    for _ in range(n):
        movieStartTime, movieEndTime = map(int, input().split())
        movieTimings.append((
            movieStartTime,
            movieEndTime
        ))

    print(maxMovieWatchingPossible(n, movieTimings))

main()