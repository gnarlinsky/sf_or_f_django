from django.db import models
from django.contrib.auth.models import User

class Vote(models.Model):
    # TODO: best practices, etc for arguments passed to each kind of Field
    SCIENCE_FICTION = 'SF'
    FANTASY = 'F'
    VOTE_CHOICES = (
        (SCIENCE_FICTION, 'Science Fiction'),
        (FANTASY, 'Fantasy'),
    )
    vote = models.CharField(max_length=2, choices=VOTE_CHOICES, null=False)
    book = models.ForeignKey('Book', null=False)
    user = models.ForeignKey(User, null=False)
    # TODO: user together with book should be unique

    @staticmethod
    def user_voted_for_book(user, book):
        if Vote.objects.filter(user=user, book=book):
            return True;
        else:
            return False

    @staticmethod
    def user_voted_f_for_book(user, book):
        vote = Vote.objects.filter(user=user, book=book).first()
        if vote != None and vote.vote == Vote.FANTASY:
           return True
        else:
            return False

    @staticmethod
    def user_voted_sf_for_book(user, book):
        vote = Vote.objects.filter(user=user, book=book).first()
        if vote != None and vote.vote == Vote.SCIENCE_FICTION:
           return True
        else:
            return False

class Book(models.Model):
    # TODO: best practices, etc for arguments passed to each kind of Field

    # basic info
    # (null=False sets field to NOT NULL; blank=False means this field
    #   is required in forms. So the combo of null=True, blank=False
    #   means that the field should be required in forms, but not if
    #   the object is created programmatically/in the db, etc.

    # TODO: it's not really the title that should be unique -- it should be the
    # title together with author that should be unique.
    title   = models.CharField(max_length=255, blank=False, null=False, unique=True)
    author  = models.CharField(max_length=255, blank=False, null=False)

    # number of votes in each category
    #votes_sf    = models.IntegerField(null=True, editable=False, default=0)
    #votes_f     = models.IntegerField(null=True, editable=False, default=0)

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

    def get_num_sf_votes(self):
        votes = Vote.objects.filter(book=self, vote=Vote.SCIENCE_FICTION)
        return len(votes)

    def get_num_f_votes(self):
        votes = Vote.objects.filter(book=self, vote=Vote.FANTASY)
        return len(votes)

    def get_percentage_f_votes(self):
        """ Return percentage of fantasy votes as a float between 0 and 100,
            to 1 decimal places. """

        votes_f = self.get_num_f_votes()
        votes_sf = self.get_num_sf_votes()

        # avoid dividing by zero
        if votes_f + votes_sf == 0:
            return 0
        else:
            ratio = float(votes_f)/(votes_f + votes_sf)
            return round(ratio * 100, 1)


    def get_percentage_sf_votes(self):
        """ Return percentage of science fiction votes as a float between 0 and 100,
            to 1 decimal places. """

        votes_f = self.get_num_f_votes()
        votes_sf = self.get_num_sf_votes()

        # avoid dividing by zero
        if votes_f + votes_sf == 0:
            return 0
        else:
            ratio = float(votes_sf)/(votes_f + votes_sf)
            return round(ratio * 100, 1)
