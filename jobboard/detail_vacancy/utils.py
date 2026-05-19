def render_stars_html(rating: float,max_stars: int = 5):
    full_stars = int(rating)
    half_star = rating - full_stars >= 0.5
    empty_stars = max_stars - full_stars - (1 if half_star else 0)

    html = "".join('<i class="bi bi-star-fill text-warning"></i>' for _ in range(full_stars))
    if half_star:
        html += '<i class="bi bi-star-half text-warning"></i>'
    html += "".join('<i class="bi bi-star text-warning"></i>' for _ in range(empty_stars))

    return html