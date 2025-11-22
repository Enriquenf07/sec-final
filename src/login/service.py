class Service:
    def validate(self, form: dict) -> str: ...

def create_service() -> Service:
    class Impl(Service):
        pass

    def validate(form):
        print(form)
        return "inválido"

    obj = Impl()
    obj.validate = validate 
    return obj