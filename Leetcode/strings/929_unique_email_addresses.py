class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sett=set()
        for email in emails:
            local,domain=email.split('@')
            local=local.split('+')[0]
            local=local.replace(".","")
            email=local+"@"+domain
            sett.add(email)

        return len(sett)
