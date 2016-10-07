"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Any melon order """

    def __init__(self, species, qty, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.tax = tax
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        base_price = 5
        
        if self.species == "Christmas":
            base_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty, tax=0.08):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, tax)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code, tax=0.17):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, tax)

        self.country_code = country_code

    def get_total(self):
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            return total + 3

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
