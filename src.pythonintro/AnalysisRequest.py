class AnalysisRequest:
    def __init__(self, amount, buyer_name):
        self.amount = amount
        self.buyerName = buyer_name

    def get_amount(self):
        return self.amount

    def get_buyer_name(self):
        return self.buyerName
