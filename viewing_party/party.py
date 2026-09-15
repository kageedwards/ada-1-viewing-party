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
    pass

def get_most_watched_genre(user_data: dict[str, list]) -> str:
    pass

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

