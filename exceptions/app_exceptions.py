class WrongLengthError(Exception):
    def __init__(self):
        self.message = {"Erro": "Tamanho padrão de 11 dígitos numéricos."}
        super().__init__(self.message)


class NotStringError(Exception):
    def __init__(self):
        self.message = {"Erro": "Ao menos um dos campos não é do tipo string."}
        super().__init__(self.message)


class AbsentError(Exception):
    def __init__(self):
        self.message = {"Erro": "Uma, ou mais, das chaves requeridas está ausente"}
        super().__init__(self.message)


class RepeatedKeyError(Exception):
    def __init__(self):
        self.message = {"Erro": "CPF já no banco de dados!"}
        super().__init__(self.message)
