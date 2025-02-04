class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails_set = set()
        for email in emails:
            sep = email.find("@")
            rest = email[sep:]
            local_name = email[:sep]

            plus = local_name.find("+")
            if plus != -1:
                local_name = local_name[:plus]

            local_name = local_name.replace(".", "")

            emails_set.add(local_name + email[sep:])

        # print(emails_set)
        return len(emails_set)
