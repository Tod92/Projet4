

class Reporting:
    """
    Vue pour export de rapports
    """
    def gen_report(self, text):
        with open('report.txt', 'w') as f:
            f.write(text)
