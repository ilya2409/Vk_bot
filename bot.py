import vk_api
from testsfile_2 import tests, check_results
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
from keyboards_2 import generate_oneline_keyboard, test_keyboard, keyboard_my, keyboard_with_tests, nani_keyboard, other_keyboard, pet_keyboard

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
                        
                elif "Привет" in text:
                    send_img(event.user_id, "Приветствую тебя мой ДЛУГ", "photo-19127548_457239038", nani_keyboard)
                        
                elif any([(i  in text) for i in ["Говор", "говор"]]):
                    write_msg(event.user_id, """Лично я за Minecraft
                                                    но мы можем перейти и на другюю тему
                                                    (если хочешь конечно, для этого напиши "other")""",nani_keyboard)
                        
                elif any([(i  in text) for i in ["груст", "Груст"]]):
                        send_img(event.user_id, "Негрусти :Ъ", "photo-191267548_457239047", nani_keyboard)
                        send_img(event.user_id, "Негрусти :Ъ", "photo-191267548_457239046", nani_keyboard)
                        send_img(event.user_id, "Негрусти :Ъ", "photo-191267548_457239045", nani_keyboard)
                        send_img(event.user_id, "Лови мой друг)))", "photo-191267548_457239048", nani_keyboard)
                        
                elif any([(i  in text) for i in ["Дел", "дел"]]):
                    write_msg(event.user_id, """У меня всё Окей, висну сдругими ботами
                                                Ну как дела у тоби в школе?
                                                Мне просто интересно, как любому другу""",nani_keyboard)
             
                        
                       
                        


                #elif any([(i  in text) for i in ["Кот"]]):
                    #write_msg(event.user_id, """Понятненько, они прикольненькие,
                                                #особенно когда мелкие""")
                        
                elif "Котейки" in text:
                    write_msg(event.user_id, """Понятненько, они прикольненькие,
                                                 особенно когда мелкие""")

                elif "Pets" in text:
                    write_msg(event.user_id, '⌨⌨⌨', pet_keyboard)
                    
                elif "other" in text:
                    write_msg(event.user_id, """И так, какая 
                                                тема у нас сегодня?""", other_keyboard)
                    
                elif "Музыка" in text:
                    write_msg(event.user_id, "http://www.loveradio.ru",  other_keyboard)
                    
                elif "YouTube" in text:
                    write_msg(event.user_id, "https://youtube.com/channel/UCiW6lzSuVk9AnWuCeXDTusA")
                    write_msg(event.user_id, "https://www.youtube.com",  other_keyboard)
                    
                elif "Мемчики" in text:
                    send_img(event.user_id, "...", "photo-191267548_457239043", other_keyboard)
                    write_msg(event.user_id, "https://www.youtube.com/user/AdamThomasMoran/videos")
                    
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
                    
                
                    if "ping" in text:
                        write_msg(event.user_id, "pong",nani_keyboard)

                    elif "Хочешь тест?" in text:
                        write_msg(event.user_id, "Выбери тест", keyboard_with_tests)
                        tested_users[event.user_id]=None
                        
                    else:
                        write_msg(event.user_id, "nani?",nani_keyboard)
'''
                elif "А_1)" in text:
                    write_msg(event.user_id, "Хорошо, -10 баллов")

                elif "Психотест" in text:
                    write_msg(event.user_id, """Хорошо,Изначальная сумма твоих балов 100:
№_1 Если тебе в парную работу педложат мечтательного и
своебразного человека или сконцентрированного на цели,
но он предпочитает работать без лишней помощи(КОГО выберишь ты?)
А_1) мечтательного и своебразного
Б_1) сконцентрированного, но он любит работать без лишней помощи""")

               #elif event.user_id in tested_users:
                   #pass
                else:
                    write_msg(event.user_id, "Я бы пообщался с тобой еще,но автор не ввел в меня еще команд,поэтому я знаю совсем немного:(", test_keyboard)
                    
send_img(event.user_id, """VK_bot это маленький онлайн тестер,
           https://www.youtube.com/channel/UCJfbG7XfoVkZNakpY0mlXOg                                         он служит для поднятия может быть твого настроения""", "photo-191267548_457239035",nani_keyboard)

Психотест
'''
