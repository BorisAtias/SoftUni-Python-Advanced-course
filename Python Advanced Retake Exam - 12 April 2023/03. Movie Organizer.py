def movie_organizer(*movie_list):
    movie_collection = {}
    for movie in movie_list:
        movie_name, genre = movie
        if genre not in movie_collection:
            movie_collection[genre] = [movie_name]
        else:
            movie_collection[genre].append(movie_name)

    sorted_genres = sorted(movie_collection.keys(), key=lambda x: (-len(movie_collection[x]), x))

    output = ""
    for genre in sorted_genres:
        output += f"{genre} - {len(movie_collection[genre])}\n"
        for movie in sorted(movie_collection[genre]):
            output += f"* {movie}\n"

    return output

