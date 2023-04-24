class ProgrammingLanguage:
    def __init__(self, name, typing_style, reflection, year_created):
        self.name = name
        self.typing_style = typing_style
        self.reflection = reflection
        self.year_created = year_created

    def is_dynamic(self):
        if self.typing_style == "Dynamic":
            return self.typing_style

    def language_information(self):
        language_information = "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing_style,
                                                                                           self.reflection,
                                                                                           self.year_created)
        return language_information
