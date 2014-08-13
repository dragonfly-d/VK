__author__ = 'Dmitry Cheyshvily'
import urllib2
import json


class VK:
    """
    This class provides access to VK API
    """
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.url = u'https://api.vk.com/method/%s'

    def __get_data(self, method, params):
        res = urllib2.urlopen(self.url % method, params).read()
        data = json.loads(res)
        if 'error' in data:
            print data
            return list()
        return data[u'response']

    def get_friends(self):
        return self.__get_data('friends.get', 'user_id=%s&fields=nickname' % self.user_id)

    def get_audios(self):
        """
        note: first item in list is integer (sum of all audio tracks for the user)
        """
        return self.__get_data('audio.get', 'owner_id=%s&access_token=%s' % (self.user_id, self.token))

    def get_groups(self):
        return self.__get_data('groups.get', 'user_id=%s&access_token=%s' % (self.user_id, self.token))

    def get_users_info(self, ids):
        return self.__get_data('users.get', 'user_ids=%s' % ids)

    def get_groups_by_ids(self, groups_id):
        return self.__get_data('groups.getById', 'group_ids=%s&fields=contacts,description,members_count' % groups_id)

    def get_account_permissions(self):
        return self.__get_data('account.getAppPermissions', 'user_ids=%s&access_token=' + self.token)
