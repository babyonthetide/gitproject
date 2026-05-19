def render_stars_html(rating: float,max_stars: int = 5):
    full_stars = int(rating)
    half_star = rating - full_stars >= 0.5
    empty_stars = max_stars - full_stars - (1 if half_star else 0)

    html = "".join('<i class="bi bi-star-fill text-warning"></i>' for _ in range(full_stars))
    if half_star:
        html += '<i class="bi bi-star-half text-warning"></i>'
    html += "".join('<i class="bi bi-star text-warning"></i>' for _ in range(empty_stars))

    return html

#Склоняем слова в опыте работы
def years_declension(experience_required: str, start: int, end: int = None) -> str:
    if experience_required == 'with_experience':
      if end == None:
        if start == 1 :
          suffix = "год"
        elif start in range(2,5):
          suffix = "года"
        else:
          suffix = "лет"
        return f"{start} {suffix}"
      elif end:
        if start and end in range(1,4):
          suffix = 'года'
        else:
          suffix = 'лет'
        return f"{start}-{end} {suffix}"
    else:
      return "without_experience"

#Разбитие текста на строки
def split_lines(text: str) -> list[str]:
  if not text:
    return []

  # Разделяем по символам переноса строки
  splited_text = text.splitlines()

  # Убираем пустые строки и пробелы по краям
  splited_text = [line.strip() for line in splited_text if line.strip()]

  return splited_text
