import flet as ft


def main(page: ft.Page):

    # criando fusão para abrir o bottomSheet
    def show_bs(e):
        bs.open = True  # para abrir o bottomsheet
        page.update()  # para colocar o bottomsheet na pagina

    def close_bs(e):
        bs.open = False  # para feichar o bottomsheet
        page.update()  # para colocar o bottomsheet na pagina

    # criando um bottomsheet
    bs = ft.BottomSheet(
        content=ft.Container(
            ft.Column(
                controls=[  # para add varios conponetes no bottonSheet
                    ft.Text('titulo', style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text('Conteúdo do bottomsheet', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.FilledButton('fechar', on_click=close_bs),
                ]
            ),
            padding=20,  # para deichar um espasamento
        ),
        dismissible=False,  # o false nao deicha fechar so fecha se tiver um botao já o true se click fora fecha
        enable_drag=True,  # para poder arrasto o bottomsheet para cima ou para baixo
        is_scroll_controlled=False,  # para abilitar barra de rolagem
        maintain_bottom_view_insets_padding=True,  # para deixar um espasamento de baixo dele
        show_drag_handle=True,  # para coloar o sinal " - " na parte superio do bottomSheet
    )

    page.overlay.append(bs)  # para adiscionar o bottomsheet na pagena

    btn = ft.ElevatedButton('abrir', on_click=show_bs)

    page.add(btn)


if __name__ == '__main__':
    ft.app(main)
