import flet as ft


def carosel (page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    #page.bgcolor = ft.colors.WHITE

    def move_D(e):
        ...

    def move_S():
        ...

    layout = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Image(
                            src=f'https://picsum.photos/250/300?{num}'
                        ) for num in range(10)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, icon_color=ft.colors.AMBER, on_click=move_D),
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, icon_color=ft.colors.AMBER_200, on_click=move_S)
                    ]
                )
            ]
        )
    )

    page.add(layout)

if __name__=='__main__':
    ft.app(carosel)