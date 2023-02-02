

class Reporting:
    """
    Vue pour export de rapports
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def gen_report(self, text):
        with open(self.file_path, 'w') as f:
            f.write(text)
