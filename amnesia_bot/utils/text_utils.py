def get_start_text():
    return (
        "🧿 *Добро пожаловать в Amnesia RPG*\n\n"
        "Ты очнулся в темной пещере без воспоминаний...\n"
        "Выбери расу и класс, чтобы начать приключение!"
    )

def get_race_desc(race):
    descriptions = {
        "elf": "...",  # полные описания из RACE_DESCRIPTIONS
        # другие расы
    }
    return descriptions.get(race, "")