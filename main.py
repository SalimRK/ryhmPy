import flet as ft


def main(page: ft.Page):
    page.title = "RhymPy"
    page.horizontal_alignment = page.vertical_alignment = "center"

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.PLAY_ARROW, bgcolor=ft.colors.RED_500)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    def animate(e):
        print(page.height)
        print(type(page.height))
        page.bottom_appbar.height = 100 if page.bottom_appbar.height == page.height else page.height
        c.content = c2 if c.content == c1 else c1
        c.update()
        page.bottom_appbar.update()

    c1 = ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_UP, icon_color=ft.colors.WHITE, on_click=animate),
            ft.Container(expand=True),
            ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
            ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
        ]
    )

    c2 = ft.Row(controls=[
        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_DOWN, icon_color=ft.colors.WHITE, on_click=animate),
    ])

    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=1000,
        reverse_duration=1000,
    )
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.RED_900,
        shape=ft.NotchShape.CIRCULAR,
        content=c,
    )

    page.add(ft.Text("Body!"))


if __name__ == '__main__':
    ft.app(main)
