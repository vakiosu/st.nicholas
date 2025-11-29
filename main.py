from customtkinter import*

screen=CTk()
screen.geometry('500x500')
screen.minsize(500,500)
screen.configure(fg_color='light pink')
screen.title('Письмо Святому Николаю!')

text_label=CTkLabel(
    screen,
    text='Привет, тут ты можешь написать письмо святому Николаю!<3',
    font=('Arial', 24),
    text_color='red'
)
text_label.pack(pady=20)

entry=CTkEntry(
    screen,
    width=400,
    height=40,
    font=('Arial', 16),
    placeholder_text="Введи свое желание здесь...",
    fg_color='white',
    text_color='black'
)
entry.pack(pady=20)

screen.mainloop()