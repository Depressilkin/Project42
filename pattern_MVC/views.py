from model import Title
class Menu:
    def __init__(self, journal):
        self.journal = journal

    def render_menu(self):
        while True:
            menu = input(f'Меню:\n1-вывод статей\n2-добавить статью\n3-удалить статью\n0-выход')
            if menu == '1':
                self.journal.render()
            elif menu == '2':
                name_title = input('Название статьи')
                outhor_title = input('Автор статьи')
                len_title = input('Количество символов статьи')
                published = input('Место публикации статьи')
                summary = input('Краткое описание статьи')
                new_title = Title(name_title, outhor_title, len_title, published, summary)
                self.journal.add_title(new_title)
                print('***\nСтатья добавлена!\n***')
            elif menu == '3':
                del_name_title = input('Введите название для удаления статьи')
                self.journal.del_title(del_name_title)
            elif menu =='0':
                break
