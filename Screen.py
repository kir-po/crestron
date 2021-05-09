import types


class Screens:
    screens = []

    def __init__(self):
        pass

    def __getitem__(self, item):
        return self.screens[item]

    def _get_scr_by_name(self, scrname):
        for scr in self.screens:
            if scr.name == scrname:
                return scr

    def add(self, scr):
        self.screens.append(scr)

    def show(self, screenname):
        screen = self._get_scr_by_name(screenname)
        screen.showmenu()
        currentscreenname, action = screen.userinput()
        self.navigator(currentscreenname, action)

    def navigator(self, currentscreenname, action):
        currentscreen = self._get_scr_by_name(currentscreenname)
        if action == 'back':
            self.show(currentscreen.prevscr.name)
        else:
            if type(currentscreen.actions[int(action)]) == str:
                nextscreen = self._get_scr_by_name(currentscreen.actions[int(action)])
                nextscreen.prevscr = self._get_scr_by_name(currentscreenname)
                self.show(self._get_scr_by_name(currentscreen.actions[int(action)]).name)
            elif type((currentscreen.actions[int(action)])[0]) == types.FunctionType:
                currentscreen.actions[int(action)][0](*(currentscreen.actions[int(action)][1]))
            else:
                print(type(currentscreen.actions[int(action)]))


class Screen:
    actions = {}

    def __init__(self, name, title, inputstr, *menu_entries, prevscr=None):
        self.name = name
        self.title = title
        self.inputstr = inputstr
        if len(menu_entries) > 0:
            self.menu_entries = menu_entries
        else:
            self.menu_entries = ()
        self.prevscr = prevscr

    def userinput(self):
        uinp = input(self.inputstr + ' ')
        if int(uinp) in range(0, len(self.menu_entries) + 1):
            return (self.name, uinp)
        else:
            if self.prevscr != None:
                if int(uinp) == len(self.menu_entries) + 1:
                   return (self.name, 'back')
                else:
                    print('Необходимо ввести существующий номер!')
                    return self.userinput()
            else:
                print('Необходимо ввести существующий номер!')
                return self.userinput()

    def showmenu(self):
        print('___________________\n' + self.title + '\n')
        for entry in range(0, len(self.menu_entries)):
            print(str(entry + 1) + '.', self.menu_entries[entry])
        if self.prevscr != None:
            print(str(len(self.menu_entries) + 1) + '.', 'Back...')

def main():
    pass

if __name__ == '__main__':
    main()
