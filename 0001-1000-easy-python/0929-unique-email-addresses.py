# https://leetcode.com/problems/unique-email-addresses
class Solution(object):
    # def numUniqueEmails(self, emails: List[str]) -> int:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        _set = set()
        for email in emails:
            _email = email.split("@")
            _set.add(_email[0].split("+")[0].replace(".", "") + "@" + _email[1])
        return len(_set)

