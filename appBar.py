import flet as ft


def main(page: ft.Page):
    #  criando o appBar
    page.appbar = ft.AppBar(
        title=ft.Text('App fit'),  # o titulo do app
        bgcolor=ft.colors.BLACK,  # a cor de fundo do appBar
        center_title=False,  # o alinhamento
        toolbar_height=100,  # a altura do aapBar
        color=ft.colors.AMBER,  # cor doa conponentes
        leading=ft.Icon(ft.icons.HOME),  # para colocar o icom ou a sua logo usa o ft,Image()
        leading_width=100,  # espasso dos elementos entre eles
        actions=[  # para adisionar funçoes
            ft.IconButton(icon=ft.icons.SUNNY),
            ft.IconButton(icon=ft.icons.NOTIFICATIONS),
            ft.CircleAvatar(content=ft.Text('PA')),  # para colocar o avatar do usuario
            ft.PopupMenuButton(  # para colocar os tres pontinho
                items=[
                    ft.PopupMenuItem(text='Meu dados'),
                    ft.PopupMenuItem(text='Cofigurações'),
                    ft.PopupMenuItem(text='Sair'),
                ]
            )
        ]
    )

    page.update()


if __name__ == '__main__':
    ft.app(main)