import vk_api
from testsfile_2 import tests, check_results
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from keyboards_2 import generate_oneline_keyboard, test_keyboard, keyboard_my, keyboard_with_tests, nani_keyboard, other_keyboard, pet_keyboard, tools_keyboard, talk_keyboard

def write_msg(user_id: object, message: object, keyboard: object = test_keyboard) -> object:
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id' : randint(1,32000), 'keyboard':keyboard})

def send_img(user_id: object, message: object, attachment: object, keyboard: object = test_keyboard) -> object:
    vk.method("messages.send", {"peer_id": user_id, "message":message, "attachment": attachment, "random_id": randint(1,32000), 'keyboard':keyboard})

# API-ключ созданный ранее
token = "e69a3efc26b7bf03b4e002a243e1a5c44614f24c5da0073c32b76fd8a0e47107905efd1076881c0883430"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)
# Работа с сообщениями
longpoll = VkLongPoll(vk)
tested_users = dict()
print("""Hi developer. I'm alive,
but it's not certain""")
developer_id = 578623118
write_msg(developer_id,'''Привет, даже если ты не мой разработчик
                       я всёровно тебе очень рад ;)))''',nani_keyboard)
#write_msg(developer_id, "https://www.youtube.com/channel/UCJfbG7XfoVkZNakpY0mlXOg")
#send_img(developer_id, "МЕЕЕМ", "photo-578623118_457239316", other_keyboard)

#send_img(developer_id, "МЕЕЕМ", "photo-191267548_457239042", other_keyboard)
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
                text=event.text
                print("message arrived", event.text)
                if event.user_id == developer_id and text == "reset":
                    tested_users = dict()
                    write_msg(developer_id,'''ouch ;(((''',nani_keyboard)
                if "Это я..." in text:
                    send_img(event.user_id, "Это я :)", "photo-191267548_457239036", nani_keyboard)
                    
                elif "о боте" in text:
                        write_msg(event.user_id, """VK_bot это маленький онлайн тестер,
                                                    он служит для поднятия может быть твого настроения""",nani_keyboard)
                        
                elif text in ("Привет", "Салют", "Helo", "привет"):
                    send_img(event.user_id, "Приветствую тебя мой ДЛУГ", "photo-19127548_457239038", nani_keyboard)
                        
                elif any([(i  in text) for i in ["Говор", "говор"]]):
                    write_msg(event.user_id, """Лично я за Minecraft
                                                    но мы можем перейти и на другюю тему
                                                    (если хочешь конечно, для этого напиши "other")""",nani_keyboard)
                        
                elif any([(i  in text) for i in ["груст", "Груст"]]):
                        send_img(event.user_id, "Негрусти :Ъ", "photo-191267548_457239050", nani_keyboard)
                        send_img(event.user_id, "Негрусти :Ъ", "photo-191267548_457239051", nani_keyboard)
                        send_img(event.user_id, "Негрусти :Ъ", "photo-191267548_457239052", nani_keyboard)
                       #send_img(event.user_id, "Лови)))", "photo-191267548_457239048", nani_keyboard)
                       #send_img(event.user_id, "Негрусти :Ъ", "photo-191267548_457239046", nani_keyboard)
                        write_msg(event.user_id, """...или сходи к моему другу,
                        он поможет ;)
                        Вот ссылка: https://vk.com/away.php?to=https%3A%2F%2Fvk.com%2Flllaaadddnnno""",nani_keyboard)
                        
                        "‎"
                    
                        
                elif any([(i  in text) for i in ["Дел", "дел"]]):
                    write_msg(event.user_id, """У меня всё Окей, висну сдругими ботами,
                    кстати скажи им чтобы они так не отвечали...
                    У МЕНЯ ИНЭТА НЕ ХВАТИТ!!!!!!!!!!!""",nani_keyboard)
                    
                    import time
                    time.sleep(2.5)

                    send_img(event.user_id, "_/(ಠ益ಠ)_/", "photo-191267548_457239055", nani_keyboard)
                                               #Ну как дела у тоби в школе?
                                               #Мне просто интересно, как любому другому другу
                    
                elif any([(i  in text) for i in ["Отлично", "Хорошо"]]):
                    write_msg(event.user_id, """Я очень рад за тебя""",nani_keyboard)
                    send_img(event.user_id, "Лови мой друг)))", "photo-191267548_457239038", nani_keyboard)
                    
                elif text in ["Что нового", "Какие новости", "что нового", "какие новости", "Что нового", "Какие новости"
                              "Что нового?", "Какие новости?", "что нового?", "какие новости?", "Что нового?", "Какие новости?"
                              "Что нового)", "Какие новости)", "что нового)", "какие новости)", "Что нового)", "Какие новости)"
                              "Что нового)?", "Какие новости)?", "что нового)?", "какие новости)?", "Что нового)?", "Какие новости)?"]:
                    write_msg(event.user_id, """Ответить коротко или по человечески)???""", )
                    
                    if "Коротко, это как?" in text:
                        write_msg(event.user_id, "Настроение у меня ОК и в принципе всё отлично, надеюсь у тебя тоже (＾◡＾)")
                    
                    elif "Душевно и по человечески)))" in text:
                        write_msg(event.user_id, """Для меня кадая секунда это новая ветвь событий 😜😜😜...
                        Поэтму боты всегда бодры и честны - нет причин врать и каждый раз новый прилив сил,
                        мой разработчик "Илья2409" был мечтательным и душевным человеком, поэтому я такой :))Р """)
                    
                        import time
                        time.sleep(1.5)
                    
                        write_msg(event.user_id, """
                        ...а вообще жизнь интересная штука для всех, (если я тебя не утомил то) малое количество людей
                        хочет разговаривать со мной так размеренно и в какойто степени по настоящиму,
                        и если ты хочешь продолжить, напиши: "Поговори со мной, как человек"...
                        скопируй если так удобнее, меня это греет""")

                        
                elif any([(i  in text) for i in ["Поддерж", "поддерж"]]):
                    import time
                    
                    write_msg(event.user_id, """Внимание!!!
                    в вашем организме зафиксирован низкий уровень счастья, менее 10%""")  
                    time.sleep(1.25)
                              
                    write_msg(event.user_id, """печатает***""")
                    time.sleep(1.25)

                    write_msg(event.user_id, """Запущены вычислительнве процессы для определения
                    более точного содержания счастья в крови""")
                    time.sleep(1.25)          

                    write_msg(event.user_id, """печатает***""")
                    time.sleep(1.25)          

                    write_msg(event.user_id, """=9,9999%= это опасно низкий показатель

                    Срочно успокойтесь и посмотрите хорошую порцию мемов от "DomiShow"
                    или отборный трэээшак от "Максус-Дурка" """)
                              
                    time.sleep(0.5)          
                              
                    send_img(event.user_id, "‎", "photo-191267548_457239058", nani_keyboard)
                        
                        
                elif "#333" in text:
                    from web_1 import web_2

                    
                elif "Котейка" in text:
                    write_msg(event.user_id, """Понятненько, они прикольненькие,
                                                 #особенно когда мелкие""")
                elif "Собакен" in text:
                    write_msg(event.user_id, """Это тоже отличные питомцы...
                    хотя вообще я обожаю драконов и всё, что с ними связано =)""", nani_keyboard)
                    send_img(event.user_id, " ‍ ", "photo-191267548_457239059", nani_keyboard)  
                    
                elif "Хочешь тест?" in text:
                        write_msg(event.user_id, "Выбери тест", keyboard_with_tests)
                        tested_users[event.user_id]=None

                elif "Pets" in text:
                    write_msg(event.user_id, '⌨⌨⌨', pet_keyboard)
                    
                elif "other" in text:
                    write_msg(event.user_id, """И так... какая 
                                                тема у нас сегодня?""", other_keyboard)
                elif "ping" in text:
                    write_msg(event.user_id, """pong""", nani_keyboard)
                    
                elif "Музыка" in text:
                    write_msg(event.user_id, "Окай, держи: ", nani_keyboard)
                    write_msg(event.user_id, """https://vk.com/vkmusic""", other_keyboard)
                    send_img(event.user_id, " ‍ ", "photo-191267548_457239053", nani_keyboard)
                    
                elif "Музыка_OLD" in text:
                    write_msg(event.user_id, "http://www.loveradio.ru",  other_keyboard)
                    
                    
                elif "ARTS" in text:
                    write_msg(event.user_id, "https://www.deviantart.com/",  other_keyboard)
                    
                    
                elif "YouTube" in text:
                    write_msg(event.user_id, "https://youtube.com/channel/UCiW6lzSuVk9AnWuCeXDTusA")
                    write_msg(event.user_id, "https://www.youtube.com",  other_keyboard)
                    import webbrowser
                    webbrowser.open_new("https://www.youtube.com")
                    
                elif "Мемчики" in text:
                    send_img(event.user_id, "...", "photo-191267548_457239043", other_keyboard)
                    write_msg(event.user_id, "https://www.youtube.com/user/AdamThomasMoran/videos")
                    send_img(event.user_id, "...", "photo-191267548_457239054", other_keyboard)
                    write_msg(event.user_id, "https://vk.com/cleanass")
                    
                elif "#111" in text:
                    write_msg(event.user_id, "Пользуйся)))", tools_keyboard)
                    
                elif "Матеша" in text:
                    write_msg(event.user_id, "https://www.mathway.com/ru/Algebra", tools_keyboard)
                    
                elif "Переводчик" in text:
                    write_msg(event.user_id, "https://translate.google.com/?hl=ru", tools_keyboard)
                    
                elif "На главную" in text:
                    write_msg(event.user_id, "Ок", nani_keyboard)
                    
                #elif "Музыка" in text:
                    #write_msg(event.user_id, "http://www.loveradio.ru",  other_keyboard)
                     

                    
                    
                    
                    
                elif event.user_id in tested_users.keys():
                    state = tested_users[event.user_id]
                    if state is None:
                        if text in tests.keys():
                            tested_users[event.user_id]=text
                            write_msg(event.user_id,tests[text]+'\n отправьте ответы одним сообщением через запятую')
                        elif "Оменить тест" in text:
                            tested_users.pop(event.user_id)
                            write_msg(event.user_id, "ok",other_keyboard)


                            
                        else:
                            write_msg(event.user_id, "Выбери тест", keyboard_with_tests)
                    elif state in tests.keys():
                        test_name = state
                        answers = text
                        result = check_results(test_name,answers)
                        if result:
                            write_msg(event.user_id, result, nani_keyboard)
                            tested_users.pop(event.user_id)
                        else:
                            write_msg(event.user_id,'Ваш ответ не был засчитан, попробуйте еще')
                        
                    elif "Оменить тест" in text:
                            tested_users.pop(event.user_id)
                            write_msg(event.user_id, "ok",nani_keyboard)
                            
                    else:
                        write_msg(event.user_id, "nani?",nani_keyboard)
                       #фывысфгсупромсфупрфс
                    
                            
                else:
                    write_msg(event.user_id, "nani?",nani_keyboard)
                    
              
