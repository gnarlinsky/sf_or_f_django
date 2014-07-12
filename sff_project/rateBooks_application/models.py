from django.db import models

class Book(models.Model):
    # TODO: best practices, etc for arguments passed to each kind of Field

    # basic info
    title   = models.CharField(max_length=255)
    author  = models.CharField(max_length=255)

    # number of votes in each category
    votes_sf    = models.IntegerField()
    votes_f     = models.IntegerField()

    ###########################################################################
    # "I would opt for the 0..1 range simply because if you store e.g. 20% as
    # 0.2 and then you want 20% of some value, it is just a case of multiplying
    # the value by 0.2 (e.g. value*perc) rather than mucking about dividing by
    # 100 (value*(perc/100))."""
    ###########################################################################
    # Represent percentages as a number between 0 and 1
    #percent_sf  = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    #percent_f   = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    # TODO: later, play with:
    #   * (the Django equivalent of) a trigger in DB to update percent_f and
    #     percent_sf based on votes_f and votes_sf
    #   * (the Django equivalent of) a trigger to constrain the fields above to
    #     be between 0 and 1  -- and best practices for that. Validators?

    # TODO: or -- could calculate percentages on the fly. So then this is an
    # interesting best-practices question... 

    # TODO: https://djangosnippets.org/snippets/1914/ !!!  subclasses
    # IntegerField PercentField!!

    # TODO: link, description, image

    def __str__(self):
        """ Represent a Book as "<Title> by <Author>" """

        return ' '.join( [ self.title,
                           "by",
                           self.author ]
                        )

    def get_percentage_f_votes(self):
        """ Return percentage of fantasy votes as a float between 0 and 100,
            to 1 decimal places. """

        ratio = float(self.votes_f)/(self.votes_f + self.votes_sf)
        return round(ratio * 100, 1)

    def get_percentage_sf_votes(self):
        """ Return percentage of science fiction votes as a float between 0 and 100,
            to 1 decimal places. """

        ratio = float(self.votes_sf)/(self.votes_f + self.votes_sf)
        return round(ratio * 100, 1)
