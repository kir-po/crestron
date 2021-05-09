from Screen import *
import sys
import argparse
import Functions


def main():
    # 1. Стартовый экран

    # 2. Экран подключения, настроек и переход к GUI режиму
    cons_mode_menu = ('Connect...', 'Settings...', 'GUI mode', 'Quit')
    cons_mode_screen = Screen('cons_mode', 'Console Mode', 'Your choose:', *cons_mode_menu)
    cons_mode_screen.actions = {1: 'connect', 2: 'settings', 3: (Functions.func_dict['gui_mode'], ()), 4: (Functions.func_dict['quit'], ())}

    # 3.1. Экран соединения с выбором активных портов
    active_ports = Functions.active_ports_scan()
    if len(active_ports) > 0:
        connect_screen_menu = active_ports
        connect_screen = Screen('connect', 'Connect Screen', 'Please, select port:', *connect_screen_menu, prevscr=cons_mode_screen)
        connect_screen.actions = {}
        for port in range(0, len(active_ports)):
            connect_screen.actions[port + 1] = (Functions.func_dict['listen_port'], (active_ports[port]))
    else:
        connect_screen_menu = active_ports
        connect_screen = Screen('connect', 'Connect Screen\n (No active ports. Please, connect device and restart program!)', 'Your choose:', *connect_screen_menu, prevscr=cons_mode_screen)

    # 3.2. Экран настроек: настройки порта, языка, режима (консольный, GUI)
    settings_menu = ('Port settings...', 'Language settings...', 'Mode settings...')
    settings_screen = Screen('settings', 'Settings', 'Your choose:', *settings_menu, prevscr=cons_mode_screen)
    settings_screen.actions = {1: 'port_settings', 2: 'select_language', 3: 'mode_settings'}

    # 3.2.1. Экран настроек порта (скорость, четность и т. д.)
    port_settings_menu = ('Speed', 'Parity')
    port_settings_screen = Screen('port_settings', 'Port settings screen', 'Your choose: ', *port_settings_menu, prevscr=settings_screen)

    # 3.2.2. Экран выбора языка программы
    select_language_menu = ('Russian', 'English')
    select_language_screen = Screen('select_language', 'Select language menu', 'Please, select language: ', *select_language_menu, prevscr=settings_screen)
    select_language_screen.actions = {1: 'settings', 2: 'settings'}

    # 3.2.3. Экран выбора режима работы программы
    mode_settings_menu = ('Console mode', 'GUI mode')
    mode_settings_screen = Screen('mode_settings', 'Mode settings', 'Please, select mode: ', *mode_settings_menu, prevscr=settings_screen)
    mode_settings_screen.actions = {1: 'cons_mode', 2: (Functions.func_dict['gui_mode'], ())}

    # Добавление экранов к экземпляру класса Screens для управления навигацией по экранам
    scrs = Screens()
    scrs.add(cons_mode_screen)
    scrs.add(connect_screen)
    scrs.add(settings_screen)
    scrs.add(port_settings_screen)
    scrs.add(select_language_screen)
    scrs.add(mode_settings_screen)

    # Показ стартового экрана
    scrs.show(cons_mode_screen.name)


def createArgParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ac', '--autoconnect', nargs='?')
    return parser


if __name__ == '__main__':
    parser = createArgParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.autoconnect:
        Functions.listen_port(namespace.autoconnect)
    else:
        main()
