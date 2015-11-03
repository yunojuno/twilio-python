# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource
from twilio.rest.page import Page
from twilio.rest.pricing.v1.voice.country import CountryList
from twilio.rest.pricing.v1.voice.number import NumberList


class VoiceList(ListResource):

    def __init__(self, version):
        """
        Initialize the VoiceList
        
        :param Version version: Version that contains the resource
        
        :returns: VoiceList
        :rtype: VoiceList
        """
        super(VoiceList, self).__init__(version)
        
        # Path Solution
        self._solution = {}
        
        # Components
        self._numbers = None
        self._countries = None

    @property
    def numbers(self):
        """
        Access the numbers
        
        :returns: NumberList
        :rtype: NumberList
        """
        if self._numbers is None:
            self._numbers = NumberList(
                self._version,
            )
        return self._numbers

    @property
    def countries(self):
        """
        Access the countries
        
        :returns: CountryList
        :rtype: CountryList
        """
        if self._countries is None:
            self._countries = CountryList(
                self._version,
            )
        return self._countries

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.VoiceList>'


class VoicePage(Page):

    def __init__(self, version, response):
        """
        Initialize the VoicePage
        
        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        
        :returns: VoicePage
        :rtype: VoicePage
        """
        super(VoicePage, self).__init__(version, response)
        
        # Path Solution
        self._solution = {}

    def get_instance(self, payload):
        """
        Build an instance of VoiceInstance
        
        :param dict payload: Payload response from the API
        
        :returns: VoiceInstance
        :rtype: VoiceInstance
        """
        return VoiceInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.VoicePage>'


class VoiceInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the VoiceInstance
        
        :returns: VoiceInstance
        :rtype: VoiceInstance
        """
        super(VoiceInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'name': payload['name'],
            'url': payload['url'],
            'links': payload['links'],
        }
        
        # Context
        self._context = None
        self._solution = {}

    @property
    def name(self):
        """
        :returns: The name
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.VoiceInstance>'