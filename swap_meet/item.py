class Item:
    """
    A class to hold item object data.

    ...
    Attributes
    ----------
    category: str
        category of an item
    condition: float
        describes condition of item from a range of 0-5
    age: float
        describes how old an object is by year

    Methods
    -------
    condition_description
        Returns str description of condition.
    """

    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """
        Returns
        -------
        Str description of condition.
        """
        if self.condition == 5.0:
           return "Brand new condition"
        elif self.condition > 4.0:
           return "Like new condition"
        elif 3.0 < self.condition <= 4.0:
           return "Very good condition"
        elif  2.0 < self.condition <= 3.0:
           return "Good condition without noticeable wear and tear"
        elif  1.0 < self.condition <= 2.0:
           return "Acceptable condition but noticeable wear and tear"
        else:
           return "Fashionably antique"
