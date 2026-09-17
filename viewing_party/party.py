# ------------- WAVE 1 --------------------

def create_movie(title: str, genre: str, rating: float) -> dict[str, str | float] | None:
    if not title or not genre or not rating:
        return None

    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data: dict[str, list], movie: dict[str, str | float]) -> dict[str, list]:
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data: dict[str, list], movie: dict[str, str | float]) -> dict[str, list]:
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data: dict[str, list], title: str) -> dict[str, list]:
    if (
        not isinstance(user_data, dict)
        or not isinstance(user_data.get("watchlist"), list)
        or not isinstance(user_data.get("watched"), list)
        or not title
    ):
        return user_data

    for i in range(0, len(user_data["watchlist"])):
        movie = user_data["watchlist"][i]
        if not movie["title"]:
            continue

        if movie["title"] == title:
            user_data["watched"].append(user_data["watchlist"].pop(i))

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data: dict[str, list]) -> float:
    if not user_data["watched"]:
        return 0.0

    total_rating = 0

    for movie in user_data["watched"]:
        total_rating += movie["rating"]

    average = total_rating / len(user_data["watched"])

    return average

def get_most_watched_genre(user_data: dict[str, list]) -> str | None:
    if not user_data["watched"]:
        return None
    
    most_watched_genre = ""
    most_watched_count = 0
    genre_counts = {}
    for i in range(len(user_data["watched"])):
        genre = user_data["watched"][i].get("genre", "")
        genre_count = genre_counts.get(genre, 0)
        genre_counts[genre] = genre_count + 1

        if genre_counts[genre] > most_watched_count:
            most_watched_genre = genre
            most_watched_count = genre_counts[genre]

    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_watched_movies_set(friends_data: list[dict]) -> set[str]:
    friends_watched = set()

    for friend in friends_data:
        for movie in friend["watched"]:
            friends_watched.add(movie["title"])

    return friends_watched

def get_unique_watched(user_data: dict[str, list]) -> list[dict]:
    unique_movies = {}

    watched_movies = get_watched_movies_set(user_data["friends"])

    for movie in user_data["watched"]:
        if movie["title"] not in watched_movies:
            unique_movies[movie["title"]] = movie

    return list(unique_movies.values())

def get_friends_unique_watched(user_data: dict[str, list]) -> list[dict]:
    unique_movies = {}
    unique_movies_title_set = set()

    user_watched_movies = get_watched_movies_set([user_data])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (
                movie["title"] not in user_watched_movies
                and movie["title"] not in unique_movies_title_set
            ):
                unique_movies_title_set.add(movie["title"])
                unique_movies[movie["title"]] = movie

    return list(unique_movies.values())
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data: dict[str, list]) -> list[dict]:
    recommendations = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["host"] in user_data["subscriptions"]:
                if movie not in user_data["watched"]:
                    if movie not in recommendations:
                        recommendations.append(movie)

    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data: dict[str, list]) -> list:
    most_watched_genre = get_most_watched_genre(user_data)
    recommendations = []

    if most_watched_genre is None:
        return recommendations

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == most_watched_genre:
                if movie not in user_data["watched"]:
                    if movie not in recommendations:
                        recommendations.append(movie)

    return recommendations

def get_rec_from_favorites(user_data: dict[str, list]) -> list:
    recommendations = []

    for favorite in user_data["favorites"]:
        friend_watched_it = False

        for friend in user_data["friends"]:
            if favorite in friend["watched"]:
                friend_watched_it = True

        if friend_watched_it == False:
            recommendations.append(favorite)

    return recommendations

