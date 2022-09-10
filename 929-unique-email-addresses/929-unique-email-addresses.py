class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        output = set()
        count = 0
        for email in emails:
            local,domain = email.split("@")
            local = local.replace(".","").split("+")[0]
            email = local+"@"+domain
            if email not in output:
                output.add(email)
                count += 1
        return count
        