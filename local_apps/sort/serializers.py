from rest_framework import serializers

from django.utils.timezone import now

from externals.third_apps.textblob import TextBlob

from externals.third_apps.textblob.sentiments import NaiveBayesAnalyzer

from externals.third_apps.nltk.tokenize import TabTokenizer



from . import models

from local_apps.sort.models import Document, DocumentClassification

class DocumentSerializer(serializers.ModelSerializer):

    #For classifications

    days_since_created = serializers.SerializerMethodField()

    sentiment = serializers.SerializerMethodField()

    noun_phrases = serializers.SerializerMethodField()

    tags = serializers.SerializerMethodField()

    class Meta:
        model = models.Document
        fields =  '__all__'
    
    #Classifications

    def get_days_since_created(self, obj):
        return (now() - obj.date_created).days
    

    def get_sentiment(self, obj):        
        return TextBlob(obj.document, analyzer=NaiveBayesAnalyzer()).sentiment  # Polarity score

    
    def get_noun_phrases(self, obj):        
        return TextBlob(obj.document).noun_phrases  # Noun phrase extraction

    def get_tags(self, obj):        
        return TextBlob(obj.document).tags  # Tags



class DocumentClassificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.DocumentClassification
        fields =  '__all__'

   