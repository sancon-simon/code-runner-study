import os
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.metrics import dp
from kivy.storage.jsonstore import JsonStore

class ImageSelector:
    def __init__(self, app):
        self.app = app
        self.store = JsonStore('file_store.json')
        self.manager_open = False

    def file_manager_open(self):
        if self.store.exists('last_dir'):
            last_dir = self.store.get('last_dir')['path']
        else:
            last_dir = os.path.expanduser("~")

        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            preview=True,
            select_path=self.select_path,
            ext=['.png', '.jpg', '.jpeg']  # specify the file extensions you want to allow
        )
        self.file_manager.show(last_dir)

    def select_path(self, path):
        '''
        This function will be called when a file is selected.
        '''
        self.exit_manager()
        MDSnackbar(
            MDSnackbarText(
                text=path,
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.8,
        ).open()

        self.store.put('last_path', path=path)
        self.store.put('last_dir', path=os.path.dirname(path))
        self.load_last_path(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''
        self.manager_open = False
        self.file_manager.close()

    def load_last_path(self, path):
        '''
        This function will be called to load the last selected path.
        '''
        selected_image = self.app.manager.get_screen('main').ids.selected_image
        selected_image.source = path

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True
