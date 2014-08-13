__author__ = 'Dmitry Cheyshvili'
import urllib2
import json


class VK:
    """
    This class provides access to VK API
    """
    def __init__(self, user_id, token):
        self.__user_id = user_id
        self.__token = token
        self.__url = u'https://api.vk.com/method/%s'

    def __get_data(self, method, params):
        res = urllib2.urlopen(self.__url % method, params).read()
        data = json.loads(res)
        if 'error' in data:
            print data
            return list()
        return data[u'response']

    def get_friends(self, user_id=None):
        if not user_id:
            user_id = self.__user_id
        return self.__get_data('friends.get', 'user_id=%s&fields=nickname' % user_id)

    def get_audios(self, user_id=None):
        """
        note: first item in list is integer (sum of all audio tracks for the user)
            if you want to get tracks only, use get_audios()[1:]
        """
        if not user_id:
            user_id = self.__user_id
        return self.__get_data('audio.get', 'owner_id=%s&access_token=%s' % (user_id, self.__token))

    def get_groups(self, user_id=None):
        if not user_id:
            user_id = self.__user_id
        return self.__get_data('groups.get', 'user_id=%s&access_token=%s' % (user_id, self.__token))

    def get_users_info(self, ids=None):
        if not ids:
            ids = self.__user_id
        return self.__get_data('users.get', 'user_ids=%s' % ids)

    def get_groups_by_ids(self, groups_id):
        return self.__get_data('groups.getById', 'group_ids=%s&fields=contacts,description,members_count' % groups_id)

    def get_account_permissions(self):
        return self.__get_data('account.getAppPermissions', 'user_ids=%s&access_token=' + self.__token)
