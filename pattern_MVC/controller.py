from model import Journal, Title
from views import Menu

journal = Journal('Мой журнал')
title1 = Title('Матч ЦСКА-Спартак', 'Иванов И.', 800, 'Матч Тв', 'Обзор матча ЦСКА- Спартак')
title2 = Title('Перенос GTA6', 'Петрова П.', 600, 'ИгроЖур', "Причины и последствия переноса игры")
journal.add_title(title1)
journal.add_title(title2)
menu_start = Menu(journal)
menu_start.render_menu()
print('Программа закрыта')
