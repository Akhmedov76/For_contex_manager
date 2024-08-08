import json


class OrderDuplicat:
    def __init__(self, file_name):
        self.file_name = file_name
        print("Filega kirdi")

    def __enter__(self):
        with open(self.file_name, 'r') as f:
            self.data = json.load(f)
            print("Enter")
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.file_name, 'w') as f:
            json.dump(self.data, f, indent=4)
            print("Exit")

    def deduplicate_orders(self):
        data = []
        seen = {}
        for dup in self.data:
            var = (dup['user'], dup['total_price'], json.dumps(dup['products']))
            if var not in seen:
                seen[var] = dup
                data.append(dup)

        self.data = data
        print("filega saqlash")


with OrderDuplicat('orders.json') as orders:
    orders.deduplicate_orders()
