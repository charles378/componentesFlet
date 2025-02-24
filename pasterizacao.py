import flet as ft


def main(page: ft.Page):
    page.title = 'Pasterização'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.bgcolor = ft.colors.WHITE

    tela = ft.Column(
        scroll=ft.ScrollMode.HIDDEN,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        controls=[
            ft.Image(
                src=f'https://picsum.photos/500/600?{num}',
                fit=ft.ImageFit.FILL
            )for num in range(10)])
     

    tab = ft.Tabs(
        tabs=[
            ft.Tab(
                text='Inicio',
                content=tela
                
            ),
            ft.Tab(
                text='Pasterizadores',
                
            ),
            ft.Tab(
                text='Menbranas',
            ),
            ft.Tab(
                text='Saiba mais'
            )
        ],
        indicator_color=ft.colors.RED,
        label_color=ft.colors.GREEN,
        unselected_label_color=ft.colors.BLUE,
    )

    leauot = ft.Container(
        tab
    )
    page.add(leauot)


if __name__ == '__main__':
    ft.app(main)