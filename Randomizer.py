import kivy, os, shutil, random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from tkinter import filedialog
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window

charnames = ["ames", "ari", "braxton", "burleday", "coach", "cop", "counselor", "crispin", "emily", "emt", "gamer_brother", "hunter", "jecka", "jeffery", "karen", "katz", "kelly", "kylar", "kyle", "lorre", "lynn", "mallcop", "megan", "mom", "nicole", "trody"]
misc = ["ball.png", "drawing_jecka.png", "text_stillthere.png", "ring_woodburn.png", "drawing_nicole.png", "yearbook.png", "sext.png", "car_lincoln.png", "car_civic.png", "car_corolla.png", "crt_myspace.png", "drawer.png", "car_mustang.png", "car_camry.png", "gunflash.png", "camera.png", "flash.png", "podium.png", "laptop.png", "aaa.png", "ball.png", "pizza.png", "brick.png", "blue.jpg", "red.jpg", "white.jpg", "blank.jpg"]
backgrounds = ['barcade ext.jpg', 'barcade int.jpg', 'bathroom.jpg', 'bedroom nicole.jpg', 'bookstore ext.jpg', 'bookstore.jpg', 'breakroom.jpg', 'Cafeteria int 2.jpg', 'Cafeteria int.jpg', 'classroom int 1.jpg', 'classroom int 2.jpg', 'classroom int 3.jpg', 'classroom int 4.jpg', 'classroom int 5.jpg', 'coffeeext.jpg', 'concert ext.png', 'concert.jpg', 'dark room.jpg', 'darkalley.png', 'diner ext.jpg', 'diner int.jpg', 'fye.jpg', 'gym 1.jpg', 'gym 2.jpg', 'gym 3.jpg', 'gym 4.jpg', 'hardwarestore.png', 'home jecka ext day.jpg', 'home jecka ext night.jpg', 'home kylar.jpg', 'home nicole ext day.jpg', 'home nicole ext night.jpg', 'home nicole int big.jpg', 'home nicole int.jpg', 'hood.png', 'hot topic.jpg', 'house ari night.png', 'house jecka night.png', 'house kylar night.jpg', 'jail int.jpg', 'library ext.png', 'library.png', 'locker room.jpg', 'mall int 2.jpg', 'mall int.jpg', 'office 1.jpg', 'office 2.jpg', 'parkinglot.png', 'photo classroom.jpg', 'porch_ari.png', 'porch_jecka.png', 'school courtyard.jpg', 'school ext 1.jpg', 'school ext 2.jpg', 'school ext 3.jpg', 'school ext 4.jpg', 'school ext 5.jpg', 'school ext 6.jpg', 'school front.jpg', 'school int 1.jpg', 'school int 2.jpg', 'theatre 1.jpg', 'theatre 2.jpg', 'theatre 2b.jpg', 'theatre backstage.jpg', 'wheat.jpg']
chartype = ""
bgtype = ""
global flipfilter
flipfilter = False
seed = ""

formattingsettings = {"":"None", "clothes":"Shuffle Clothes Only", "expressions":"Shuffle Expressions Only", "characters":"Shuffle Within Character", "sprites": "Shuffle Across Characters", "similar":"Shuffle Similar Backgrounds", "all":"Shuffle All Backgrounds", "og":"Class of '09 (Original)", "reup":"Class of '09: The Re-Up", "flip":"Class of '09: The Flipside"}

availablechar = ["clothes", "expressions", "characters", "sprites"]
availablebg = ["similar", "all"]
availablegames = ["og", "reup", "flip"]
games = []
paths = {"og":"", "reup":"", "flip":""}

class MainWindow(Screen):
    def checkbox_click(self, instance, value):
        global flipfilter, games, chartype, bgtype
        if instance == "flipfilter":
            
            flipfilter = value

        if value is True:
            if instance in availablegames:
                if paths[instance] == "":
                    paths[instance] = filedialog.askdirectory()
                games.append(instance)
            elif instance in availablebg:
                bgtype = instance
            elif instance in availablechar:
                chartype = instance
        else:
            if instance in availablegames:
                games.remove(instance)
        print(games, flipfilter, chartype, bgtype)

        format_games = []
        for g in games:
            format_games.append(formattingsettings[g])
        format_games = '\n'.join(format_games)


        gen_screen = self.manager.get_screen("generate")
        try:
            gen_screen.settingsdisplay = (
                f"Games Enabled:\n{format_games}"
                f"\n\nCharacter Sprite Randomization: {formattingsettings[chartype]}"
                f"\n\nBackground Randomization: {formattingsettings[bgtype]}"
                f"\n\nRemove Flipside's fetish content: {flipfilter}"
            )
        except:
            pass 
        

class GenerateWindow(Screen):

    settingsdisplay = StringProperty("")

    def generate(self):
        global seed
        seed = self.ids.seed.text
        print("Seed stored:", seed)

        # Get image files
        images = []
        for game in games:
            for i in os.listdir(paths[game] + "\\game\\images"):
                images.append(i)



    def on_pre_enter(self):
        global games, chartype, bgtype
        settingsdisplay = StringProperty(f"Games enabled: {games}\nCharacter Sprite Randomization: {chartype}\nBackground Randomization: {bgtype}")

class HelpWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("manager.kv")


class ClassOf09RandomizerApp(App):
    def build(self):
        return kv

Window.fullscreen = 'auto'

if __name__ == "__main__":
    ClassOf09RandomizerApp().run()