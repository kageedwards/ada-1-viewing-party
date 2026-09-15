# ------------- WAVE 1 --------------------

def create_movie(title: str, genre: str, rating: float) -> dict[str] | None:
    if not title or not genre or not rating:
        return None

    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data: dict[str], movie: dict[str]) -> dict[str]:
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data: dict[str], movie: dict[str]) -> dict[str]:
    pass

def watch_movie(user_data: dict[str], title: str) -> dict[str]:
    pass


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

