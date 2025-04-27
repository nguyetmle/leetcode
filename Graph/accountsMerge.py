"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, 
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. 
Note that even if two accounts have the same name, they may belong to different people as people could have the same name. 
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, 
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.


Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                ["John","johnsmith@mail.com","john00@mail.com"],
                ["Mary","mary@mail.com"],
                ["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
        ["Mary","mary@mail.com"],
        ["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Level: Medium
Approach: Build graph then use DFS
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName = {}
        emailToEmails = {}

        # build graph of emails
        for acc in accounts:
            name = acc[0]
            emails = acc[1:]
            for email in emails:
                #populate emailToName dict
                emailToName[email] = name 

                #populate emailToEmails dict
                if email not in emailToEmails:
                    emailToEmails[email] = set()
                for neighbor in emails:
                    if neighbor != email:
                        emailToEmails[email].add(neighbor)
        print(emailToEmails)

        # perform dfs 
        visited = set()
        def dfs(email, mergeAcc):   #mergeAcc is a list of all emails belong to the same person
            if email in visited:
                return 
            visited.add(email)
            mergeAcc.append(email)

            #visit neighbors
            for neighbor in emailToEmails[email]:
                dfs(neighbor,mergeAcc)

        mergeAll = [] 
        for email in emailToEmails:
            if email not in visited:
                mergeAcc = []
                dfs(email,mergeAcc)
                mergeAll.append([emailToName[email]] + sorted(mergeAcc))

        return mergeAll


