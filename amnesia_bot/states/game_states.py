from aiogram.fsm.state import StatesGroup, State

class GameStates(StatesGroup):
    choosing_race = State()
    choosing_class = State()
    choosing_name = State()
    in_city = State()
    in_location = State()