from django.db import models

import uuid

#classificar sort, classify, rank, rate, categorize, class


class Document(models.Model):
    title = models.TextField( blank = False)
    document = models.TextField( blank = True)

    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    class Meta:
        get_latest_by = 'date_modified'

    def __str__(self):
        return self.title


class DocumentClassification(models.Model):
    classification = models.TextField( blank = False)
    document = models.ForeignKey(Document, null=True, blank=True,
                               on_delete=models.SET_NULL, related_name="document_classification")


    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    class Meta:
        get_latest_by = 'date_modified'

    def __str__(self):
        return self.title