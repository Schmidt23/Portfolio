

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



I = Legion('I', "Dark Angels", "Lion El'Jonson", "Repent! For tomorrow you die!", "Loyal / Imperium ", "I.jpg")
II = Legion('II', "Unknown", "Unknown", "Unknown", "None", "II.jpg")
III =Legion('III', "Emperor's Children", "Fulgrim", "Children of the Emperor! Death to his foes!", "Traitor: Slaaneesh", "III.jpg")
IV = Legion('IV', 'Iron Warrios', 'Perturabo', 'Iron within, Iron without', 'Traitor: Chaos Undivided', 'IV.gif')
V = Legion('V', 'White Scars', 'Jaghatai Khan', 'For the Khan and the Emperor!', 'Loyal / Imperium ', 'V.jpg')
VI = Legion('VI', 'Space Wolves', 'Leman Russ', 'For Russ and the Allfather!', 'Loyal / Imperium', 'VI.png')
VII = Legion('VII', 'Iron Fists', 'Rogal Dorn', 'Primarch-Progenitor, to your glory and the glory of him on earth', 'Loyal / Imperium', 'VII.png')
VIII = Legion('VIII', 'Night Lords', 'Konrad Curze', 'Ave Dominus Nox! We have come for you!', 'Traitor: None', 'VIII.png')
IX = Legion('IX', 'Blood Angels', 'Sanguinius', 'By the Blood of Sanguinius', 'Loyal / Imperium ', 'IX.png')
X = Legion('X','Iron Hands', 'Ferrus Manus', 'The Flesh is weak!', 'Loyal / Imperium', 'X.png')
XI = Legion('XI', "Unknown", "Unknown", "Unknown", "None", "XI.jpg")
XII = Legion('XII', 'World Eaters', 'Angron', 'Blood for the Blood God! Skulls for the Skull Throne!', 'Traitor: Khorne', 'XII.png')
XIII = Legion('XIII', 'Ultramarines', 'Roboute Guilliman', 'Courage and Honour! we march for Macragge!', 'Loyal Imperium', 'XIII.jpg')
XIV = Legion('XIV', 'Death Guard', 'Mortarion', 'None', 'Traitor: Nurgle', 'XIV.png')
XV = Legion('XV', 'Thousand Sons', 'Magnus', 'All is dust!', 'Traitor: Tzeentch', 'XV.png')
XVI = Legion('XVI', 'Sons of Horus', 'Horus Lupercal', 'We are returned! Death to the False Emperor!', 'Traitor: Chaos Undivided', 'XVI.jpg')
XVII = Legion('XVII', 'Word Bearers', 'Lorgar Aurelian', 'An appropriate passage from their sacred texts and dolorous roars', 'Traitor: Chaos Undivided', 'XVII.jpg')
XVIII = Legion('XVIII', 'Salamanders', 'Vulkan', 'Into the fires of battle, unto the anvil of war!', 'Loyal / Imperium', 'XVIII.jpg')
XIX = Legion('XIX', 'Raven Guard', 'Corvus Corax', 'Victorus Aut Mortis!', 'Loyal / Imperium', 'XIX.png')
XX = Legion('XX', 'Alpha Legion', 'Alpharius/Omegon', 'Hydra Dominatus', 'Traitor: Chaos Undivided / Loyal', 'XX.jpg')


def return_legion(query):
    out = set()
    for legion in legions:
        #check for exaxt match
        if query.lower() in [v.lower() for v in legion.__dict__.values()]:
            #clear partial matches
            out = set()
            out.add(legion)
            return out
        #return partial matches
        else:
            for v in legion.__dict__.values():
                if query.lower() in v.lower():
                    out.add(legion)
    return out

#search = "iron"
#olegion = return_legion(search)
#for rlegion in olegion:
#    response = (f"Name: {rlegion.name}")
#    print(response)