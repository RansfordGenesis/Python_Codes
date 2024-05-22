class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        new = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            new.add(f"{local}@{domain}")
        return len(new)
        
