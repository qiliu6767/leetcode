class Solution(object):
    def processEmail(self, email):
        '''
        Process email: remove "." in local name
        and remove contents after "+" sign
        '''
        # Split email into local and domain name
        [local, domain] = email.split("@")
        
        if "+" in local:
            # Find the index of the first "+" sign
            first_ind = local.index("+")
            # Remove everything after the first "+" sign
            local = local[:first_ind]
        
        if "." in local:
            # Remove the "." sign in local
            local = "".join(local.split("."))
        
        # Combine the local and domain name
        res = local + "@" + domain
        
        return res
            
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = len(set([self.processEmail(email) for email in emails]))
        return res
        