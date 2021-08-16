from PIL import Image, ImageTk
import tkinter as tk
import pygame

WIDTH, HEIGHT = 1900, 900

pygame.mixer.init()
pygame.mixer.music.load("play_intro.mp3")
pygame.mixer.music.play(loops=0)

''' Questions '''
current_question = 0

all_questions = [
    # [question, choice_a, choice_b, choice_c, choice_d, correct_answer],
    ["Защо даряват Иво и Инес?", "Защото са добри хора", "Защото са ИТ", "Защото обичат да помагат", "Нямат си друга работа", 2],
    ["Как се казва бебето на Пешо?", 'Пешо', 'Матей', 'Макавей', 'Мойсей', 2],
    ["Коe от следните места е любимото на Агнес да прекарва време с теб?", "Инсигния", "Стария апартамент", "В балетната зала", "На брода", 4],
    ["Какво са си мислили Рени и Дари за теб от профилната ти в кидс?", "Инструктур по гледане на кафе", "Естествено руса", "Малко кифла", "Собственичка на голф 4ка", 3],
    ["Как викаш на Дари като ви раздруса лигнята?", "Муци", "Пате", "Котьо", "Маце", 3],
    ["Кой те учи на бачата за първи път?", "Никола", "Венци", "Стоян", "Пешо", 1],
    ["Какъв доктор по специалност е Стоян?", "Пластичен хирург", "Коремен хирург", "Съдов хирург", "Кардиохирург", 3],
    ["В коя стая седнахте на един чин с Мария?", "401", "403", "301", "304", 1],
    ["Как си взехте изпита по Анатомия с Мария?", "На късмет", "С учене", "С пищови", "С наговаряне на курса", 4],
    ["В коя болница работи Стоян?", "Св. Георги", "Св. Мина", "МБАЛ Пловдив", "Св. Богородица", 1],
    ["С какво е пътувала Инес на първото си море?", "Автобус", "Кола", "Микробус", "Влак", 4],
    ["С какво се отоплява на Нова година?", "Климатик", "Раховец", "Камина", "Парно", 2],
    ["Коя е любимата игра на Иво?", "World of Warcraft", "Starcraft 2", "Dota 2", "League of Legends", 2],
    ["Кой е авторът на книгата, която най-много не е харесал Иво?", "Саймън Синек", "Ричърд Тейлър", "Рей Далио", "Даниел Канеман", 1],
    ["На кое тепе се качихте с Иво за първи път?", "Небет Тепе", "Сахат Тепе", "Бунарджик", "Джамбаз Тепе", 3]
]

''' Functions '''
def set_question(number):
    global correct_answer
    row = all_questions[number]
    question.set(row[0])
    choice_a.set(row[1])
    choice_b.set(row[2])
    choice_c.set(row[3])
    choice_d.set(row[4])
    correct_answer = row[5]


def selected(selected_number):
    global current_question
    if selected_number == correct_answer:
        if selected_number == 1:
            if current_question == 4:
                root.after(200, lambda: option_a_btn.configure(background="orange"))
                root.after(1200, lambda: option_a_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_a_btn.configure(background="blue"))
                root.after(1600, lambda: option_a_btn.configure(background="green"))
                root.after(1800, lambda: option_a_btn.configure(background="blue"))
                root.after(2000, lambda: option_a_btn.configure(background="green"))
                root.after(2200, lambda: option_a_btn.configure(background="blue"))
                root.after(2400, lambda: option_a_btn.configure(background="green"))
                root.after(9200, lambda: play_background('unpause'))
                root.after(9400, lambda: next_question())
            elif current_question == 9:
                root.after(200, lambda: option_a_btn.configure(background="orange"))
                root.after(1200, lambda: option_a_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_a_btn.configure(background="blue"))
                root.after(1600, lambda: option_a_btn.configure(background="green"))
                root.after(1800, lambda: option_a_btn.configure(background="blue"))
                root.after(2000, lambda: option_a_btn.configure(background="green"))
                root.after(2200, lambda: option_a_btn.configure(background="blue"))
                root.after(2400, lambda: option_a_btn.configure(background="green"))
                root.after(9200, lambda: play_background('unpause'))
                root.after(9400, lambda: next_question())
            elif current_question == 14:
                root.after(200, lambda: option_a_btn.configure(background="orange"))
                root.after(200, lambda: play_final_answer_mark())
                root.after(20200, lambda: option_a_btn.configure(background="green"))
                root.after(20200, lambda: play_correct())
                root.after(20400, lambda: option_a_btn.configure(background="blue"))
                root.after(20600, lambda: option_a_btn.configure(background="green"))
                root.after(20800, lambda: option_a_btn.configure(background="blue"))
                root.after(21000, lambda: option_a_btn.configure(background="green"))
                root.after(21200, lambda: option_a_btn.configure(background="blue"))
                root.after(21400, lambda: option_a_btn.configure(background="green"))
            else:
                root.after(200, lambda: option_a_btn.configure(background="orange"))
                root.after(1200, lambda: option_a_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_a_btn.configure(background="blue"))
                root.after(1600, lambda: option_a_btn.configure(background="green"))
                root.after(1800, lambda: option_a_btn.configure(background="blue"))
                root.after(2000, lambda: option_a_btn.configure(background="green"))
                root.after(2200, lambda: option_a_btn.configure(background="blue"))
                root.after(2400, lambda: option_a_btn.configure(background="green"))
                root.after(2400, lambda: play_background('unpause'))
                root.after(2600, lambda: next_question())
        elif selected_number == 2:
            if current_question == 4:
                root.after(200, lambda: option_b_btn.configure(background="orange"))
                root.after(1200, lambda: option_b_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_b_btn.configure(background="blue"))
                root.after(1600, lambda: option_b_btn.configure(background="green"))
                root.after(1800, lambda: option_b_btn.configure(background="blue"))
                root.after(2000, lambda: option_b_btn.configure(background="green"))
                root.after(2200, lambda: option_b_btn.configure(background="blue"))
                root.after(2400, lambda: option_b_btn.configure(background="green"))
                root.after(9200, lambda: play_background('unpause'))
                root.after(9400, lambda: next_question())
            elif current_question == 9:
                root.after(200, lambda: option_b_btn.configure(background="orange"))
                root.after(1200, lambda: option_b_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_b_btn.configure(background="blue"))
                root.after(1600, lambda: option_b_btn.configure(background="green"))
                root.after(1800, lambda: option_b_btn.configure(background="blue"))
                root.after(2000, lambda: option_b_btn.configure(background="green"))
                root.after(2200, lambda: option_b_btn.configure(background="blue"))
                root.after(2400, lambda: option_b_btn.configure(background="green"))
                root.after(9200, lambda: play_background('unpause'))
                root.after(9400, lambda: next_question())
            elif current_question == 14:
                root.after(200, lambda: option_b_btn.configure(background="orange"))
                root.after(1200, lambda: option_b_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_b_btn.configure(background="blue"))
                root.after(1600, lambda: option_b_btn.configure(background="green"))
                root.after(1800, lambda: option_b_btn.configure(background="blue"))
                root.after(2000, lambda: option_b_btn.configure(background="green"))
                root.after(2200, lambda: option_b_btn.configure(background="blue"))
                root.after(2400, lambda: option_b_btn.configure(background="green"))
            else:
                root.after(200, lambda: option_b_btn.configure(background="orange"))
                root.after(1200, lambda: option_b_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_b_btn.configure(background="blue"))
                root.after(1600, lambda: option_b_btn.configure(background="green"))
                root.after(1800, lambda: option_b_btn.configure(background="blue"))
                root.after(2000, lambda: option_b_btn.configure(background="green"))
                root.after(2200, lambda: option_b_btn.configure(background="blue"))
                root.after(2400, lambda: option_b_btn.configure(background="green"))
                root.after(2400, lambda: play_background('unpause'))
                root.after(2600, lambda: next_question())
        elif selected_number == 3:
            if current_question == 4:
                root.after(200, lambda: option_c_btn.configure(background="orange"))
                root.after(1200, lambda: option_c_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_c_btn.configure(background="blue"))
                root.after(1600, lambda: option_c_btn.configure(background="green"))
                root.after(1800, lambda: option_c_btn.configure(background="blue"))
                root.after(2000, lambda: option_c_btn.configure(background="green"))
                root.after(2200, lambda: option_c_btn.configure(background="blue"))
                root.after(2400, lambda: option_c_btn.configure(background="green"))
                root.after(9200, lambda: play_background('unpause'))
                root.after(9400, lambda: next_question())
            elif current_question == 9:
                root.after(200, lambda: option_c_btn.configure(background="orange"))
                root.after(1200, lambda: option_c_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_c_btn.configure(background="blue"))
                root.after(1600, lambda: option_c_btn.configure(background="green"))
                root.after(1800, lambda: option_c_btn.configure(background="blue"))
                root.after(2000, lambda: option_c_btn.configure(background="green"))
                root.after(2200, lambda: option_c_btn.configure(background="blue"))
                root.after(2400, lambda: option_c_btn.configure(background="green"))
                root.after(9200, lambda: play_background('unpause'))
                root.after(9400, lambda: next_question())
            elif current_question == 14:
                root.after(200, lambda: option_c_btn.configure(background="orange"))
                root.after(1200, lambda: option_c_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_c_btn.configure(background="blue"))
                root.after(1600, lambda: option_c_btn.configure(background="green"))
                root.after(1800, lambda: option_c_btn.configure(background="blue"))
                root.after(2000, lambda: option_c_btn.configure(background="green"))
                root.after(2200, lambda: option_c_btn.configure(background="blue"))
                root.after(2400, lambda: option_c_btn.configure(background="green"))
            else:
                root.after(200, lambda: option_c_btn.configure(background="orange"))
                root.after(1200, lambda: option_c_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_c_btn.configure(background="blue"))
                root.after(1600, lambda: option_c_btn.configure(background="green"))
                root.after(1800, lambda: option_c_btn.configure(background="blue"))
                root.after(2000, lambda: option_c_btn.configure(background="green"))
                root.after(2200, lambda: option_c_btn.configure(background="blue"))
                root.after(2400, lambda: option_c_btn.configure(background="green"))
                root.after(2400, lambda: play_background('unpause'))
                root.after(2600, lambda: next_question())
        elif selected_number == 4:
            if current_question == 4:
                root.after(200, lambda: option_d_btn.configure(background="orange"))
                root.after(1200, lambda: option_d_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_d_btn.configure(background="blue"))
                root.after(1600, lambda: option_d_btn.configure(background="green"))
                root.after(1800, lambda: option_d_btn.configure(background="blue"))
                root.after(2000, lambda: option_d_btn.configure(background="green"))
                root.after(2200, lambda: option_d_btn.configure(background="blue"))
                root.after(2400, lambda: option_d_btn.configure(background="green"))
                root.after(9200, lambda: play_background('unpause'))
                root.after(9400, lambda: next_question())
            elif current_question == 9:
                root.after(200, lambda: option_d_btn.configure(background="orange"))
                root.after(1200, lambda: option_d_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_d_btn.configure(background="blue"))
                root.after(1600, lambda: option_d_btn.configure(background="green"))
                root.after(1800, lambda: option_d_btn.configure(background="blue"))
                root.after(2000, lambda: option_d_btn.configure(background="green"))
                root.after(2200, lambda: option_d_btn.configure(background="blue"))
                root.after(2400, lambda: option_d_btn.configure(background="green"))
                root.after(9200, lambda: play_background('unpause'))
                root.after(9400, lambda: next_question())
            elif current_question == 14:
                root.after(200, lambda: option_d_btn.configure(background="orange"))
                root.after(1200, lambda: option_d_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_d_btn.configure(background="blue"))
                root.after(1600, lambda: option_d_btn.configure(background="green"))
                root.after(1800, lambda: option_d_btn.configure(background="blue"))
                root.after(2000, lambda: option_d_btn.configure(background="green"))
                root.after(2200, lambda: option_d_btn.configure(background="blue"))
                root.after(2400, lambda: option_d_btn.configure(background="green"))
            else:
                root.after(200, lambda: option_d_btn.configure(background="orange"))
                root.after(1200, lambda: option_d_btn.configure(background="green"))
                root.after(1200, lambda: play_background('pause'))
                root.after(1200, lambda: play_correct())
                root.after(1400, lambda: option_d_btn.configure(background="blue"))
                root.after(1600, lambda: option_d_btn.configure(background="green"))
                root.after(1800, lambda: option_d_btn.configure(background="blue"))
                root.after(2000, lambda: option_d_btn.configure(background="green"))
                root.after(2200, lambda: option_d_btn.configure(background="blue"))
                root.after(2400, lambda: option_d_btn.configure(background="green"))
                root.after(2400, lambda: play_background('unpause'))
                root.after(2600, lambda: next_question())
    else:
        print('Game Over')
        if selected_number == 1:
            root.after(200, lambda: option_a_btn.configure(background="orange"))
            root.after(1200, lambda: option_a_btn.configure(background="red"))
            root.after(1200, lambda: play_incorrect())
            root.after(1400, lambda: option_a_btn.configure(background="blue"))
            root.after(1600, lambda: option_a_btn.configure(background="red"))
            root.after(1800, lambda: option_a_btn.configure(background="blue"))
            root.after(2000, lambda: option_a_btn.configure(background="red"))
            root.after(2200, lambda: option_a_btn.configure(background="blue"))
            root.after(2400, lambda: option_a_btn.configure(background="red"))
            root.after(2600, lambda: root.quit())
        elif selected_number == 2:
            root.after(200, lambda: option_b_btn.configure(background="orange"))
            root.after(1200, lambda: option_b_btn.configure(background="red"))
            root.after(1200, lambda: play_incorrect())
            root.after(1400, lambda: option_b_btn.configure(background="blue"))
            root.after(1600, lambda: option_b_btn.configure(background="red"))
            root.after(1800, lambda: option_b_btn.configure(background="blue"))
            root.after(2000, lambda: option_b_btn.configure(background="red"))
            root.after(2200, lambda: option_b_btn.configure(background="blue"))
            root.after(2400, lambda: option_b_btn.configure(background="red"))
            root.after(2600, lambda: root.quit())
        elif selected_number == 3:
            root.after(200, lambda: option_c_btn.configure(background="orange"))
            root.after(1200, lambda: option_c_btn.configure(background="red"))
            root.after(1200, lambda: play_incorrect())
            root.after(1400, lambda: option_c_btn.configure(background="blue"))
            root.after(1600, lambda: option_c_btn.configure(background="red"))
            root.after(1800, lambda: option_c_btn.configure(background="blue"))
            root.after(2000, lambda: option_c_btn.configure(background="red"))
            root.after(2200, lambda: option_c_btn.configure(background="blue"))
            root.after(2400, lambda: option_c_btn.configure(background="red"))
            root.after(2600, lambda: root.quit())
        elif selected_number == 4:
            root.after(200, lambda: option_d_btn.configure(background="orange"))
            root.after(1200, lambda: option_d_btn.configure(background="red"))
            root.after(1200, lambda: play_incorrect())
            root.after(1400, lambda: option_d_btn.configure(background="blue"))
            root.after(1600, lambda: option_d_btn.configure(background="red"))
            root.after(1800, lambda: option_d_btn.configure(background="blue"))
            root.after(2000, lambda: option_d_btn.configure(background="red"))
            root.after(2200, lambda: option_d_btn.configure(background="blue"))
            root.after(2400, lambda: option_d_btn.configure(background="red"))
            root.after(2600, lambda: root.quit())


def next_question():
    global current_question
    current_question += 1
    if current_question >= len(all_questions):
        current_question = 0
    option_a_btn.configure(background="blue")
    option_b_btn.configure(background="blue")
    option_c_btn.configure(background="blue")
    option_d_btn.configure(background="blue")
    set_question(current_question)
    print(current_question)


def quit_game():
    root.destroy()


def play_correct():
    if current_question == 4:
        pygame.mixer.music.load("play_first_phase_win.mp3")
        pygame.mixer.music.play(loops=0)
    elif current_question == 9:
        pygame.mixer.music.load("play_second_phase_win.mp3")
        pygame.mixer.music.play(loops=0)
    elif current_question == 14:
        pygame.mixer.music.load("play_final_question_win.mp3")
        pygame.mixer.music.play(loops=0)

    else:
        pygame.mixer.music.load("play_correct.mp3")
        pygame.mixer.music.play(loops=0)


def play_incorrect():
    pygame.mixer.music.load("play_incorrect.mp3")
    pygame.mixer.music.play(loops=0)


def play_background(pause):
    if current_question <= 3:
        pygame.mixer.music.load("play_background_1.mp3")
        pygame.mixer.music.play(loops=100)
        if pause == 'pause':
            pygame.mixer.music.pause()
        elif pause == 'unpause':
            pygame.mixer.music.unpause()
        else:
            pass
    elif current_question >= 9:
        pygame.mixer.music.load("play_background_3.mp3")
        pygame.mixer.music.play(loops=100)
        if pause == 'pause':
            pygame.mixer.music.pause()
        elif pause == 'unpause':
            pygame.mixer.music.unpause()
        else:
            pass
    elif current_question >= 4:
        pygame.mixer.music.load("play_background_2.mp3")
        pygame.mixer.music.play(loops=100)
        if pause == 'pause':
            pygame.mixer.music.pause()
        elif pause == 'unpause':
            pygame.mixer.music.unpause()
        else:
            pass


def play_final_answer_mark():
    if current_question == 14:
        pygame.mixer.music.load("play_final_answer_mark.mp3")
        pygame.mixer.music.play(loops=0)


''' Frames '''
root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.state('zoomed')
root.bind('<Escape>', lambda event: root.state('normal'))
root.bind('<F11>', lambda event: root.state('zoomed'))

root.configure(background='black')
root.title("Who wants to be a bride-lionaire (0.1)")
root.after(15000, lambda: play_background('play'))  # waits for intro to finish
frame = tk.Frame(root, bg='black')
frame.grid(ipadx='900', ipady='500')

img = ImageTk.PhotoImage(Image.open('main.png').resize((WIDTH, HEIGHT), Image.ANTIALIAS))
lbl = tk.Label(root, image=img)
lbl.img = img
lbl.place(relx=0.5, rely=0.5, anchor='center')

main_frame = tk.Frame(root, width=WIDTH, height=HEIGHT)
main_frame.grid(row=0, column=0)

header_frame = tk.Frame(main_frame, bg='black', width=900, height=200, padx=175)  # padx=175 if 3 lifelines
header_frame.grid(row=0, column=0)

center_frame = tk.Frame(main_frame, bg='black', width=900, height=200, padx=2)
center_frame.grid(row=1, column=0)

footer_frame = tk.Frame(main_frame, bg='black', width=900, height=200, padx=52)
footer_frame.grid(row=2, column=0)

question = tk.StringVar()
choice_a = tk.StringVar()
choice_b = tk.StringVar()
choice_c = tk.StringVar()
choice_d = tk.StringVar()

''' Lifelines '''
def use_5050():
    canvas = tk.Canvas(header_frame, bg='black', width=343, height=266)
    canvas.grid(row=0, column=0)
    canvas.delete("all")
    new_image = tk.PhotoImage(file='lifeline_5050_x.png')
    canvas.create_image(170, 140, image=new_image)
    canvas.image = new_image

def use_ATA():
    canvas = tk.Canvas(header_frame, bg='black', width=343, height=266)
    canvas.grid(row=0, column=1)
    canvas.delete("all")
    new_image = tk.PhotoImage(file='lifeline_ATA_x.png')
    canvas.create_image(170, 140, image=new_image)
    canvas.image = new_image

def use_PAF():
    canvas = tk.Canvas(header_frame, bg='black', width=343, height=266)
    canvas.grid(row=0, column=2)
    canvas.delete("all")
    new_image = tk.PhotoImage(file='lifeline_PAF_x.png')
    canvas.create_image(170, 140, image=new_image)
    canvas.image = new_image


''' Widgets'''
lifeline_5050 = tk.PhotoImage(file='lifeline_5050.png')
logo_centre = tk.Button(header_frame, image=lifeline_5050, bg='black', width=343, height=266, command=use_5050)
logo_centre.grid(row=0, column=0)

lifeline_ATA = tk.PhotoImage(file='lifeline_ATA.png')
logo_centre = tk.Button(header_frame, image=lifeline_ATA, bg='black', width=343, height=266, command=use_ATA)
logo_centre.grid(row=0, column=1)

lifeline_PAF = tk.PhotoImage(file='lifeline_PAF.png')
logo_centre = tk.Button(header_frame, image=lifeline_PAF, bg='black', width=343, height=266, command=use_PAF)
logo_centre.grid(row=0, column=2)

# quit_image = ImageTk.PhotoImage(Image.open('quit.png').resize((343, 266), Image.ANTIALIAS))
# logo_centre = tk.Button(header_frame, image=quit_image, bg='black', width=343, height=266, command=quit_game)
# logo_centre.grid(row=0, column=3)

question_txt = tk.Entry(center_frame, font=('arial', 18, 'bold'), bg='blue', fg='white', bd=5, width=100, textvariable=question)
question_txt.grid(row=0, column=0, columnspan=4, padx=40, pady=20, ipady=50)

option_a = tk.Label(footer_frame, font=('arial', 14, 'bold'), text="A: ", bg='black', fg='white', bd=5)
option_a.grid(row=1, column=0, pady=4)
option_a_btn = tk.Button(footer_frame, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=50, height=2, textvariable=choice_a, command=lambda:selected(1))
option_a_btn.grid(row=1, column=1, pady=4)

option_b = tk.Label(footer_frame, font=('arial', 14, 'bold'), text="B: ", bg='black', fg='white', bd=5)
option_b.grid(row=1, column=2)
option_b_btn = tk.Button(footer_frame, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=50, height=2, textvariable=choice_b, command=lambda:selected(2))
option_b_btn.grid(row=1, column=3, pady=4)

option_c = tk.Label(footer_frame, font=('arial', 14, 'bold'), text="C: ", bg='black', fg='white', bd=5)
option_c.grid(row=2, column=0, pady=4)
option_c_btn = tk.Button(footer_frame, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=50, height=2, textvariable=choice_c, command=lambda:selected(3))
option_c_btn.grid(row=2, column=1, pady=4)

option_d = tk.Label(footer_frame, font=('arial', 14, 'bold'), text="D: ", bg='black', fg='white', bd=5)
option_d.grid(row=2, column=2, pady=4)
option_d_btn = tk.Button(footer_frame, font=('arial', 14, 'bold'), bg='blue', fg='white', bd=1, width=50, height=2, textvariable=choice_d, command=lambda:selected(4))
option_d_btn.grid(row=2, column=3, pady=4)

set_question(current_question)
root.mainloop()

'''
BACKLOG:
1. Add lose sounds for each phase - get sound from main audio file - small lose(1-5), big lose(6-14/15)
2. Change main image to be used as background and widgets to be 'transparent'
3. Add new frame to show progress
    - separate images for each question
        -- custom made starting from 0.10 lv - 0.50 lv; 1 lv - 5 lv; 10 lv - 25 lv; 50 lv or similar
    - change image on each correct answer
    - move lifelines?
4. Move to separate files
 - resources / functions
5. Add functions for lifelines
6. Cleaner code
'''