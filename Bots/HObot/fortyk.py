

legions = []

class Legion:


    def __init__(self, number, name, primarch, motto, affiliation, pic):
        self.number = number
        self.name = name
        self.primarch = primarch
        self.motto = motto
        self.affiliation = affiliation
        self.pic = pic
        legions.append(self)

    def info(self):
        return self.number, self.name, self.primarch, self.motto, self.affiliation, self.pic



I = Legion('I', "Dark Angels", "Lion El'Jonson", "Repent! For tomorrow you die!", "Loyal", "I.jpg")
II = Legion('II', "Unknown", "Unknown", "Unknown", "None", "II.jpg")
III =Legion('III', "Emperor's Children", "Fulgrim", "Children of the Emperor! Death to his foes!", "Slaaneesh", "III.jpg")
IV = Legion('IV', 'Iron Warrios', 'Perturabo', 'Iron within, Iron without', 'Chaos Undivided', 'IV.gif')
V = Legion('V', 'White Scars', 'Jaghatai Khan', 'For the Khan and the Emperor!', 'Loyal', 'V.jpg')
VI = Legion('VI', 'Space Wolves', 'Leman Russ', 'For Russ and the Allfather!', 'Loyal', 'VI.png')
VII = Legion('VII', 'Iron Fists', 'Rogal Dorn', 'Primarch-Progenitor, to your glory and the glory of him on earth', 'Loyal', 'VII.png')
VIII = Legion('VIII', 'Night Lords', 'Konrad Curze', 'Ave Dominus Nox! We have come for you!', 'None', 'VIII.png')
IX = Legion('IX', 'Blood Angels', 'Sanguinius', 'By the Blood of Sanguinius', 'Loyal', 'IX.png')
X = Legion('X','Iron Hands', 'Ferrus Manus', 'The Flesh is weak!', 'Loyal', 'X.png')
XI = Legion('XI', "Unknown", "Unknown", "Unknown", "None", "XI.jpg")
XII = Legion('XII', 'World Eaters', 'Angron', 'Blood for the Blood God! Skulls for the Skull Throne!', 'Khorne', 'XII.png')
XIII = Legion('XIII', 'Ultramarines', 'Roboute Guilliman', 'Courage and Honour! we march for Macragge!', 'Loyal', 'XII.jpg')
XIV = Legion('XIV', 'Death Guard', 'Mortarion', 'None', 'Nurgle', 'XIV.png')
XV = Legion('XV', 'Thousand Sons', 'Magnus', 'All is dust!', 'Tzeentch', 'XV.png')
XVI = Legion('XVI', 'Sons of Horus', 'Horus Lupercal', 'We are returned! Death to the False Emperor!', 'Chaos Undivided', 'XVI.jpg')
XVII = Legion('XVII', 'Word Bearers', 'Lorgar Aurelian', 'An appropriate passage from their sacred texts and dolorous roars', 'Chaos Undivided', 'XVII.jpg')
XVIII = Legion('XVIII', 'Salamanders', 'Vulkan', 'Into the fires of battle, unto the anvil of war!', 'Loyal', 'XVIII.jpg')
XIX = Legion('XIX', 'Raven Guard', 'Corvus Corax', 'Victorus Aut Mortis!', 'Loyal', 'XIX.png')
XX = Legion('XX', 'Alpha Legion', 'Alpharius/Omegon', 'Hydra Dominatus', 'Chaos Undivided/Loyal', 'XX.jpg')


def return_legion(query):
    for legion in legions:
        if query.lower() in [v.lower() for v in legion.__dict__.values()]:
            print(legion.name)
            return legion

#search = "angron"
#print (return_legion(search))