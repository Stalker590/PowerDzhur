import flet as ft
from .register import register as reg


def account(page: ft.Page,content: ft.Column):
    content.controls.clear()
    content.controls.append(
        ft.Column(

            [
                ft.Text("Аккаунт", size=36, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Row(  # ось цей ряд — щоб центровано
                    controls=[
                        ft.Icon(ft.Icons.ACCOUNT_CIRCLE, size=100)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("Авторизуватись", width=150),
                        ft.ElevatedButton("Зареєструватись", width=150, on_click=lambda e: reg(page, content)),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            expand=True
        )
    )
    page.update()