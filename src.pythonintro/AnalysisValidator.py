class AnalysisValidator:
    def validate(self, request):
        buyer_name = request.get_buyer_name()
        return buyer_name

