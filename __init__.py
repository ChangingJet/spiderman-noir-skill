from mycroft import MycroftSkill, intent_file_handler


class SpidermanNoir(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('noir.spiderman.intent')
    def handle_noir_spiderman(self, message):
        self.speak_dialog('noir.spiderman')


def create_skill():
    return SpidermanNoir()

