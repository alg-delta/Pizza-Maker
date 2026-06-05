# функція для ініціалізації бази даних та додавання даних
def create_db():
    from app import app
    from models import db, Dough, Main, Dop

    with app.app_context():
        db.drop_all() # видаляє всі таблиці (для навчання)
        db.create_all()  # створює заново

    if not Dough.query.first():
        # ТИПИ тіста
        dough1 = Dough(name="Класичне Тісто", description="Звичайне тісто з дріжджами. Тонке та пухке.", price=4.0,
                                image="images/DOUGH1.png")
        dough2 = Dough(name="Бездрізджове Тісто", description="Тісто на кефірі, без дріжджів. Листкове та хрустке.", price=5.8,
                                image="images/DOUGH2.png")

        # Додаємо всі суші в чергу (session) БД
        db.session.add_all([dough1, dough2])



        # ГОЛОВНІ ІНГРЕДІЄНТИ
        if not Main.query.first():
            main1 = Main(name="Томатний", price=2.0, image="images/M1.png")
            main2 = Main(name="Білий", price=1.9, image="images/M2.png")
            main3 = Main(name="Барбек'ю", price=2.2, image="images/M3.png")
            main4 = Main(name="Песто", price=3.0, image="images/M4.png")
            main5 = Main(name="Альфредо", price=2.0, image="images/M5.png")
            main6 = Main(name="Сирний", price=2.9, image="images/M6.png")
            main7 = Main(name="Солодий Гострий", price=2.6, image="images/M7.png")
            main8 = Main(name="Без Соусу", price=0.0, image="images/nil.png")

        # Додаємо всі головні інгредієнти в чергу (session) БД
        db.session.add_all([main1, main2, main3, main4, main5, main6, main7, main8])



        # ДОПОВНЕННЯ
        if not Dop.query.first():
            dop1 = Dop(name="Моцарелла", price=1.2, image="images/D1.png")
            dop2 = Dop(name="Горгонзола", price=1.3, image="images/D2.png")
            dop3 = Dop(name="Пармезан", price=1.3, image="images/D3.png")
            dop4 = Dop(name="Чеддер", price=2.4, image="images/D4.png")
            dop5 = Dop(name="Бекон", price=1.0, image="images/D5.png")
            dop6 = Dop(name="Шинка", price=1.2, image="images/D6.png")
            dop7 = Dop(name="Курка", price=1.3, image="images/D7.png")
            dop8 = Dop(name="Пепероні", price=1.4, image="images/D8.png")
            dop9 = Dop(name="Перець", price=1.2, image="images/D9.png")
            dop10 = Dop(name="Базилік", price=0.9, image="images/D10.png")
            dop11 = Dop(name="Салат Айсберг", price=1.3, image="images/D11.png")
            dop12 = Dop(name="Ананас", price=2.4, image="images/D12.png")
            dop13 = Dop(name="Шампіньйони", price=1.3, image="images/D13.png")
            dop14 = Dop(name="Томат", price=0.8, image="images/D14.png")
            dop15 = Dop(name="Кукурудза", price=1.0, image="images/D15.png")
            dop16 = Dop(name="Оливки", price=1.2, image="images/D16.png")

        # Додаємо всі доповнення в чергу (session) БД
        db.session.add_all([dop1, dop2, dop3, dop4, dop5, dop6, dop7, dop8, dop9, dop10, dop11, dop12, dop13, dop14, dop15, dop16])


        # Зберігаємо всі зміни з черги (сесії) у БД
        db.session.commit()

    if __name__ == '__main__':
        create_db()
        print("Базу даних успішно ініціалізовано!")

