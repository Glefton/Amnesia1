@router.callback_query(F.data.startswith("talk_"), GameStates.in_city)
async def talk_to_npc(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    race = data.get('race', 'human')
    npc_type = callback.data.split("_")[1]
    npc = NPC_DATA[race][npc_type]
    
    # Разные фразы для каждого NPC
    dialogues = {
        "merchant": [
            "У меня есть особые товары для особых клиентов...",
            "Хороший выбор, очень хороший...",
            "Этот товар только что прибыл из дальних земель!"
        ],
        "blacksmith": [
            "Только качественные материалы!",
            "Видел я оружие и получше твоего...",
            "Этому клинку уже сто лет, а он всё ещё острый!"
        ],
        "quest": [
            "Ты выглядишь подходящим кандидатом...",
            "Опасное это дело, не для слабаков!",
            "Последний, кто взял это задание, не вернулся..."
        ]
    }
    
    await callback.answer(
        npc['greeting'] + "\n\n" + random.choice(dialogues[npc_type]),
        show_alert=True
    )

@router.callback_query(F.data == "open_shop", GameStates.in_city)
async def open_shop(callback: CallbackQuery):
    await callback.answer("Магазин пока не реализован", show_alert=True)

@router.callback_query(F.data == "take_quest", GameStates.in_city)
async def take_quest(callback: CallbackQuery, state: FSMContext):
    await state.update_data(quest_active=True, mobs_killed=0)
    await callback.answer("Квест 'Убить 5 мобов' принят!", show_alert=True)