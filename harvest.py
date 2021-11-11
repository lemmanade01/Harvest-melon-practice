############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def __repr__(self):
        return f"<code = {self.code}>, <first_harvest = {self.first_harvest}>, <color = {self.color}>, <is_seedless = {self.is_seedless}>, <is_bestseller = {self.is_bestseller}>, <name = {self.name}>"
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairing = pairing

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.new_code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []


    musk = MelonType("musk", 1998, "green", False, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", True, False, "Casaba")
    cas.add_pairing("strawberries", "mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", True, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yellow", True, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    melon_types = make_melon_types()
    for i in melon_types:
        melon_pairing = melon_types[i].pairing
        print(f"{melon_types[i][5]} with") 
        print(f"- {melon_pairing}")

        # melon_types[0].pairing



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
