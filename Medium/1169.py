class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        parsed_transactions = []
        for transaction in transactions:
            parts = transaction.split(",")
            name = parts[0]
            time = int(parts[1])
            amount = int(parts[2])
            city = parts[3]
            parsed_transactions.append((name, time, amount, city, transaction))

        # Group transactions by name
        from collections import defaultdict

        name_groups = defaultdict(list)
        for parsed in parsed_transactions:
            name = parsed[0]
            name_groups[name].append(parsed)

        invalid = []
        # Check each transaction for validity
        for parsed in parsed_transactions:
            name, time, amount, city, original = parsed
            # Condition 1: amount exceeds $1000
            if amount > 1000:
                invalid.append(original)
                continue  # No need to check other condition

            # Condition 2: same name, different city within 60 minutes
            # Check all transactions in the same name group
            found_conflict = False
            for other in name_groups[name]:
                other_time = other[1]
                other_city = other[3]
                if other_city != city and abs(time - other_time) <= 60:
                    found_conflict = True
                    break  # Found a conflict, no need to check further
            if found_conflict:
                invalid.append(original)

        return invalid
