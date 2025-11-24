# Logpass
## Como rodar o projeto
- pip install -r req.txt // instale as dependências
- alembic upgrade head // rode as migrations

## Arquitetura do sistema

![entidades](files/sistema_rel.png)

### Roles

    O sistema é orientado a roles (permissões), onde o usuário só tem acesso ao que é permitido para ele.

    São elas:
    - Suporte
        Permissão para usuários internos do LogPass. Clientes não tem acesso.
    - Admin
        Super usuário da empresa, pode criar outros usuários e acessar todas as funcionalidades.
    - Estoque
        Usuário responsável pelo estoque.
    - Financeiro
        Usuário responsável pelo financeiro.

### Empresa
    Os usuários são vinculados a uma empresa, dessa forma só possuem acesso a informações de sua própria compania.