import flet as ft
from pages.show_home import show_home
from pages.show_about import show_about
from pages.account import account

def main(page: ft.Page):
    page.title = "PowerDzhur"
    page.theme_mode = 'dark'

    # Створюємо панель навігації з кнопками
    nav = ft.Row(
        [
            ft.ElevatedButton("Головна", on_click=lambda e: show_home(page,content)),
            ft.ElevatedButton("Про нас", on_click=lambda e: show_about(page,content)),
            ft.ElevatedButton("Ввійти в аккаунт", on_click=lambda e: account(page,content)),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    content = ft.Column(expand=True, scroll="auto")

    page.add(nav)
    page.add(content)

    # Показуємо домашню сторінку спочатку
    show_home(page,content)


ft.app(
    target=main,
    view=ft.WEB_BROWSER,
    port=8550,
    host="0.0.0.0",
)