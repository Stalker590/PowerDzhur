import flet as ft


def show_home(page: ft.Page, content: ft.Column):
    content.controls.clear()
    content.controls.append(
        ft.Column(
            [
                ft.Text("PowerBankDzhur", size=40, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                ft.Text("Якісні павербанки для ваших цілей", size=24, italic=True, color="gray",
                        text_align=ft.TextAlign.CENTER),
                ft.Divider(height=20, color="transparent"),

                # Перший рядок - Якість
                ft.Row(
                    [
                        ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN, size=40),
                        ft.Text("Висока якість продукції, перевірена часом", size=18),
                    ],

                    spacing=15,
                ),

                # Другий рядок - Швидка доставка
                ft.Row(
                    [
                        ft.Icon(ft.Icons.LOCAL_SHIPPING, color=ft.Colors.BLUE, size=40),
                        ft.Text("Швидка доставка по всій Україні", size=18),
                    ],

                    spacing=15,
                ),

                # Третій рядок - Вигідна ціна
                ft.Row(
                    [
                        ft.Icon(ft.Icons.EURO_SYMBOL, color=ft.Colors.ORANGE, size=40),
                        ft.Text("Вигідна ціна та гнучкі умови оплати", size=18),
                    ],

                    spacing=15,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=20,
        )
    )
    page.update()