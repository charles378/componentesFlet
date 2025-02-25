import flet as ft


def main(page: ft.Page):
    tag = ft.Tabs(
        tabs=[
            ft.Tab(
                text='A100',
                content=ft.Container(
                    width=500,
                    height=500,
                    content=ft.ElevatedButton(text='oo'),
                    bgcolor=ft.colors.AMBER
                )   
            ),
            ft.Tab(
                text='A300'
            )
        ], scrollable=True
    )

    page.add( tag,   )

if __name__ == '__main__':
    ft.app(main)