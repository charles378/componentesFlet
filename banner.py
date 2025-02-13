import flet as ft


def main(page: ft.Page):
    # função para fechar o bane
    def close_banner(e):
        page.banner.open = False  # para fechar o banner
        page.update()  # para dar uploude do bane na pagena

    # criando uma fução para abri o baner
    def open_banner(e):
        page.banner = baner  # para atreboir a variavel no banner
        baner.open = True  # para abri o banner
        page.update()  # para dar uploude do bane na pagena

    # criando o baner
    baner = ft.Banner(
        actions=[
            ft.TextButton('cancelar', style=ft.ButtonStyle(color=ft.colors.RED), on_click=close_banner),
            ft.ElevatedButton('Tentar novamente', style=ft.ButtonStyle(bgcolor=ft.colors.GREEN, color=ft.colors.WHITE),
                              on_click=close_banner),
        ],
        content=ft.Text('Ops, parece que não conseguimos processar a sua solicitação no momento'),
        content_padding=ft.padding.all(5),  # largura do baner
        leading=ft.Icon(ft.icons.WARNING_AMBER),  # add um icone
        force_actions_below=True,  # para forçar a ação sempre ficar na parte inferior
        bgcolor=ft.colors.BLACK,  # autera a cor de fundo
    )

    botaoParaDisparaBaner = ft.ElevatedButton('Abrir o baner', on_click=open_banner)

    page.add(botaoParaDisparaBaner)


if __name__ == '__main__':
    ft.app(main)