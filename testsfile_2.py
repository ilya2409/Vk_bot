tests = {
    
    "Коты или псы?":
        ("""Мне просто интересно,
            какие питомцы тебе нравятся больще:
            КОШКИ ИЛИ СОБАКИ? (для ответа напиши "Pets" )"""),
    
    "Психотест":
        ("""Хорошо...

        №_1 Если тебе в парную работу педложат мечтательного и
            своебразного человека или сконцентрированного на цели,
            но он предпочитает работать без лишней помощи(КОГО выберишь ты?)
            А) что-то среднее
            Б) сконцентрированного, но он любит работать без лишней помощи
            В) мечтательного и своебразного

        №_2 Если наулице тебе попадётся ничейний кашелёк, что ты с
            ним сделаешь?
            А) Отдашь в бюро находок
            Б) Возьмёшь и посмотриш, что там внутри

        №_3 Если ты прогуливаясь по парку увидишь собаку которая
            бежит за ребёнком, коковы будут твои действия?
            А) Бросишь собаки кусок еды и тем самым спасёшь ребёнка
            Б) Бросишь в собаку камень
            В) Бросишь камень в ребёнка

        №_4 Если тебе понравился тест, то КАК БЫ ты отблагодорил автора?
            А) Сказал бы автору СПАСИБО
            А) Сказал бы автору СПАСИБО
            А) Сказал бы автору СПАСИБО""")
    ,

    "Вид твоего внутреннего волка":42,
    }
def check_results(test, answer):
    if test in tests:
        if test == "Коты или псы?":
            if any([(i  in answer) for i in ["кот", "Кот"]]):
                return('''Понятненько...
                           Кста они довольно милые, особенно когда мелкие''')
        if test == "Психотест":
            answer = answer.upper().split(',')
            if len(answer) == 4:
                for i in answer:
                    if i.upper() not in ('А','Б', 'В'):
                        return
                return "you are "+str(100 * (answer.count('А')+answer.count('A'))/ 4)+'% good'

print('PROGRAM_IS_ACTIVE')