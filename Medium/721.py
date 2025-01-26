from collections import defaultdict


class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


def accountsMerge(accounts):
    uf = UnionFind()
    email_to_name = {}

    # Map emails to names and perform union operations
    for account in accounts:
        name = account[0]
        first_email = account[1]
        for email in account[1:]:
            uf.union(first_email, email)
            email_to_name[email] = name

    # Group emails by their root parent
    components = defaultdict(list)
    for email in email_to_name:
        root = uf.find(email)
        components[root].append(email)

    # Format the result
    result = []
    for root, emails in components.items():
        result.append([email_to_name[root]] + sorted(emails))

    return result
