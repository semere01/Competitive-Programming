from typing import List


class Union:
    def __init__(self, emails):
        self.data = {}
        for email in emails:
            self.data[email] = email
    
    def rep(self, email):
        email_rep = self.data[email]
        while (email_rep != self.data[email_rep]):
            email_rep = self.data[email_rep]
        
        while (email != self.data[email]):
            next_email =self.data[email]
            self.data[email] = email_rep
            email = next_email
        
        return email_rep
    
    def union(self, email1, email2):
        email1_rep = self.rep(email1)
        email2_rep = self.rep(email2)
        if (email1_rep != email2_rep):
            self.data[email1_rep] = email2_rep
        




class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                emailToName[email] = name
        
        union = Union(emailToName.keys())

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                union.union(first_email, email)
        
        rep_emails = {}
        for email in emailToName.keys():
            rep_emails[union.rep(email)] = []

        for email in emailToName.keys():
            rep_emails[union.rep(email)].append(email)
        
        

        
        final_list = []
        for person in rep_emails.keys():
            current_list = []
            name = emailToName[person]
            sorted_emails = sorted(rep_emails[person])
            current_list.append(name)
            for email in sorted_emails:
                current_list.append(email)
            final_list.append(current_list)
        
        return final_list


        
        
        
        


        

        

