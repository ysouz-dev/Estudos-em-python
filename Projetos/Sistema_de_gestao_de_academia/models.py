class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def apresentar(self):
        return f'Olá me chamo {self.nome} e tenho {self.idade} anos'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome_novo):
        self.validar_nome(nome_novo)
        self._nome = nome_novo

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade_nova):
        self.validar_idade(idade_nova)
        self._idade = idade_nova

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf_novo):
        self.validar_cpf(cpf_novo)
        self.__cpf = cpf_novo

    @staticmethod
    def validar_nome(nome):
        if not isinstance(nome, str):
            raise TypeError('O nome deve ser do tipo string.')
        if not nome.replace(' ', '').isalpha():
            raise ValueError('O nome só pode ser contido por caracteres alfabéticos.')

    @staticmethod
    def validar_idade(idade):
        if not isinstance(idade, int):
            raise TypeError('A idade deve ser um número inteiro.')
        if idade < 0:
            raise ValueError('A idade não pode ser um número negativo.')

    @staticmethod
    def validar_cpf(cpf):
        if not isinstance(cpf, str):
            raise TypeError('O cpf tem que ser do tipo string.')
        if len(str(cpf)) != 11:
            raise ValueError(f'Seu cpf contém {len(str(cpf))} dígitos. o correto é conter 11 dígitos.')


class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, plano):
        super().__init__(nome, idade, cpf)
        self.mensalidade = None
        self.plano = plano
        self.status = False
        self.nomeclasse = self.__class__.__name__

    def pagar_mensalidade(self):
        self.status = True
        print('\033[1;32mMensalidade paga com sucesso!\033[m')

    def cancelar_plano(self):
        self.status = False
        print('\033[1;31mPlano cancelado.\033[m')

    def apresentar(self):
        return f'Olá, sou o {self.nomeclasse.lower()} {self.nome} tenho {self.idade} anos e meu plano é o {self.plano.capitalize()}.'

    @property
    def mensalidade(self):
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, mensalidade_nova):
        self.__mensalidade = mensalidade_nova

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, plano_novo):
        self.validar_plano(plano_novo)
        if plano_novo.lower() in ['basico', 'básico']:
            self.mensalidade = 100
        elif plano_novo.lower() == 'plus':
            self.mensalidade = 130
        else:
            self.mensalidade = 150
        self.__plano = plano_novo

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_novo):
        self.__status = status_novo

    @staticmethod
    def validar_plano(plano):
        if not isinstance(plano, str):
            raise TypeError('O plano deve ser do tipo string.')
        if plano.lower() not in ['basico', 'básico', 'plus', 'premium']:
            raise ValueError('O plano só podem ser os seguintes (Básico, Plus, Premium).')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, cargo, salario):
        super().__init__(nome, idade, cpf)
        self.cargo = cargo
        self.salario = salario
        self.nomeclasse = self.__class__.__name__

    def aumentar_salario(self, percentual):
        self.validar_percentual(percentual)
        self.__salario += percentual / 100 * self.__salario
        print(f'\033[1;32mO {self.nomeclasse.lower()} {self.nome} teve um aumento de {percentual}%, meus parabéns!!\033[m')

    def bonus(self):
        return 0

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo_novo):
        self.validar_cargo(cargo_novo)
        self.__cargo = cargo_novo

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario_novo):
        self.validar_salario(salario_novo)
        self.__salario = salario_novo

    @staticmethod
    def validar_cargo(cargo):
        if not isinstance(cargo, str):
            raise TypeError('O cargo deve ser do tipo String.')
        if not cargo.replace(' ', '').isalpha():
            raise ValueError('O cargo só pode conter letras alfabéticas.')

    @staticmethod
    def validar_salario(salario):
        if not isinstance(salario, (int, float)):
            raise TypeError('O salário só pode ser contido por números.')
        if salario < 0:
            raise ValueError('O salário não pode ser um valor negativo.')

    @staticmethod
    def validar_percentual(percentual):
        if not isinstance(percentual, int):
            raise TypeError('O percentual deve ser um número inteiro')
        if percentual > 100 or percentual < 0:
            erro = 'O percentual não pode ser maior que 100%.' if percentual > 100 else 'O percentual não pode ser menor que 0.%'
            raise ValueError(erro)

class Instrutor(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, salario, especialidade):
        super().__init__(nome, idade, cpf, cargo, salario)
        self.especialidade = especialidade

    def bonus(self):
        return 10 / 100 * self.salario

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, especialidade_nova):
        self.validar_especialidade(especialidade_nova)
        self._especialidade = especialidade_nova

    @staticmethod
    def validar_especialidade(especialidade):
        if not isinstance(especialidade, str):
            raise TypeError('A especialidade deve ser do tipo string.')
        if not especialidade.replace(' ', '').isalpha():
            raise ValueError('A especialidade deve conter apenas caracteres alfabéticos.')

class Gerente(Funcionario):
    def __init__(self, nome, idade, cpf, cargo, salario):
        super().__init__(nome, idade, cpf, cargo, salario)

    def bonus(self):
        return 20 / 100 * self.salario

class Equipamento:
    def __init__(self, nome, categoria, codigo):
        self.nome = nome
        self.categoria = categoria
        self.codigo = codigo
        self.status = True

    def ocupar(self):
        if not self.status:
            print('\033[1;31mO equipamento {self.nome} já está ocupado.\033[m')
            return
        self.status = False
        print('\033[1;33mEquipamento {self.nome} ocupado!\033[m')

    def liberar(self):
        if self.status:
            print(f'\033[1;32mO equipamento {self.nome} ja está liberado.\033[m')
            return
        self.status = True
        print(f'\033[1;32m O equimanto {self.nome} foi liberado!\033[m')

    def enviar_para_manutencao(self):
        if self.status == None:
            print(f'\033[1;31mO equipamento {self.nome} ja está na manutenção.\033[m')
            return
        self.status = None
        print(f'\033[1;33mO equipamento {self.nome} foi enviado para a manutenção!\033[m')

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria_nova):
        self.validar_categoria(categoria_nova)
        self._categoria = categoria_nova

    @staticmethod
    def validar_categoria(categoria):
        if not isinstance(categoria, str):
            raise TypeError('A categoria tem que ser do tipo string.')
        if categoria.lower() not in ['cardio', 'forca', 'força', 'mobilidade']:
            raise ValueError('A categoria dos equipamentos só podem ser uma dessas (Cardio, Força, Mobilidade).')

class Academia:
    def __init__(self, nome_da_academia):
        self.nome = nome_da_academia
        self.lista_alunos = []
        self.lista_funcionarios = []
        self.lista_equipamentos = []

    def cadastrar_aluno(self):
        nome = self.validador_de_string('Nome do Aluno: ', 'nome de aluno')
        idade = self.validador_de_numero(int, f'Idade de {nome}: ', 'idade')
        cpf = self.validador_de_cpf()
        while True:
            plano = input('Plano desejado (Básico, Plus, Premium): ').strip().capitalize()
            if plano.lower() not in ['basico', 'básico', 'plus', 'premium']:
                print('\033[1;31mO plano só podem ser os seguintes (Básico, Plus, Premium).\033[m')
            else:
                break

        self.lista_alunos.append(Aluno(nome, idade, cpf, plano))
        print('\033[1;32mAluno cadastrado com sucesso!\033[m')

    def cadastrar_funcionario(self):
        nome = self.validador_de_string('Nome do funcionário: ', 'nome de funcionario')
        idade = self.validador_de_numero(int, 'Idade: ', 'idade')
        cpf = self.validador_de_cpf()
        cargo = self.validador_de_string('Cargo: ', 'cargo')
        salario = self.validador_de_numero(float, 'Salário: ', 'salário')
        self.lista_funcionarios.append(Funcionario(nome, idade, cpf, cargo, salario))
        print('\033[1;32mFuncionário cadastrado com sucesso!\033[m')

    def adicionar_equipamento(self):
        nome = input('Nome do equipamento: ')
        categoria = input('Categoria: ')
        Equipamento.validar_categoria(categoria)
        codigo = input('Código: ')
        self.lista_equipamentos.append(Equipamento(nome, categoria, codigo))
        print('\033[1;32mEquipamento adicionado com sucesso!\033[m')

    def listar_alunos(self):
        if not self.verificar_lista_tem_algo(self.lista_alunos):
            print('\033[1;31mA academia não possui nenhum aluno na lista para listar.\033[m')
            return

        print('---=---=---=---')
        print('Lista de Alunos')
        print('---=---=---=---')
        for posicao, aluno in enumerate(self.lista_alunos):
            print(f'{posicao+1} - Nome: {aluno.nome} | Idade: {aluno.idade} | CPF: {aluno.cpf} | Plano: {aluno.plano}')
            print()

        input('Pressione ENTER para continuar')

    def listar_funcionarios(self):
        if not self.verificar_lista_tem_algo(self.lista_funcionarios):
            print('\033[1;31mA academia não possui nenhum funcionário na lista para listar.\033[m')
            return

        print('---=---=---=---=---=---=---')
        print(' Lista de Funcionários')
        print('---=---=---=---=---=---=---')
        for posicao, funcionario in enumerate(self.lista_funcionarios):
            print(f'{posicao+1} - Nome: {funcionario.nome} | Idade: {funcionario.idade} | CPF: {funcionario.cpf} | Cargo: {funcionario.cargo} | Salário: R$ {funcionario.salario:.2f}')
            print()

        input('Pressione ENTER para continuar')

    def listar_equipamentos(self):
        if not self.verificar_lista_tem_algo(self.lista_equipamentos):
            print('\033[1;31mA academia não possui nenhum equipamento na lista para listar.\033[m')
            return

        print('---=---=---=---=---=---=---')
        print(' Lista de Equipamentos')
        print('---=---=---=---=---=---=---')
        for posicao, equipamento in enumerate(self.lista_equipamentos):
            print(f'{posicao+1} - Nome: {equipamento.nome} | Categoria: {equipamento.categoria} | Código: {equipamento.codigo}')
            print()

        input('Pressione ENTER para continuar')

    def buscar_aluno_por_cpf(self):
        if not self.verificar_lista_tem_algo(self.lista_alunos):
            print('\033[1;31mA academia não possui nenhum aluno na lista para buscar.\033[m')
            return

        cpf = self.validador_de_cpf()
        for aluno in self.lista_alunos:
            if cpf == aluno.cpf:
                print('\033[1;32mAluno encontrado!\033[m')
                print(f'Nome: {aluno.nome} | Idade: {aluno.idade} | CPF: {aluno.cpf} | Plano: {aluno.plano}')
                input('Pressione ENTER para continuar')
                return
        else:
            print('\033[1;31mNenhum aluno com esse cpf foi encontrado.\033[m')

    def buscar_funcionario_por_cpf(self):
        if not self.verificar_lista_tem_algo(self.lista_funcionarios):
            print('\033[1;31mA academia não possui nenhum funcionário na lista para buscar.\033[m')
            return

        cpf = self.validador_de_cpf()
        for funcionario in self.lista_funcionarios:
            if cpf == funcionario.cpf:
                print('\033[1;32mFuncionário encontrado!\033[m')
                print(f'Nome: {funcionario.nome} | Idade: {funcionario.idade} | CPF: {funcionario.cpf} | Cargo: {funcionario.cargo} | Salário: R$ {funcionario.salario:.2f}')
                input('Pressione ENTER para continuar')
                return
        else:
            print('\033[1;31mNenhum funcionário com esse cpf foi encontrado.\033[m')

    def buscar_equipamento_por_codigo(self):
        if not self.verificar_lista_tem_algo(self.lista_equipamentos):
            print('\033[1;31mA academia não possui nenhum equipamento na lista para buscar.\033[m')
            return

        codigo = input('Digite o codigo: ')
        for equipamento in self.lista_equipamentos:
            if codigo == equipamento.codigo:
                print('\033[1;32mEquipamento encontrado!\033[m')
                print(f'Nome: {equipamento.nome} | Categoria: {equipamento.categoria} | Código: {equipamento.codigo}')
                input('Pressione ENTER para continuar')
                return
        else:
            print('\033[1;31mNenhum equipamento com esse código foi encontrado.\033[m')

    @property
    def lista_alunos(self):
        return self.__lista_alunos

    @property
    def lista_funcionarios(self):
        return self.__lista_funcionarios

    @property
    def lista_equipamentos(self):
        return self.__lista_equipamentos

    @lista_alunos.setter
    def lista_alunos(self, nova_lista):
        if not isinstance(nova_lista, list):
            raise TypeError('A listagem de alunos precisa ser uma lista.')
        self.__lista_alunos = nova_lista

    @lista_funcionarios.setter
    def lista_funcionarios(self, nova_lista):
        if not isinstance(nova_lista, list):
            raise TypeError('A listagem de funcionários precisa ser uma lista.')
        self.__lista_funcionarios = nova_lista

    @lista_equipamentos.setter
    def lista_equipamentos(self, nova_lista):
        if not isinstance(nova_lista, list):
            raise TypeError('A listagem de equipamentos precisa ser uma lista.')
        self.__lista_equipamentos = nova_lista

    @classmethod
    def criar_padrao(cls):
        alunos = [Aluno('Marcos', 17, '12345678901', 'basico'),
                  Aluno('joão', 22, '12345678902', 'plus'),
                  Aluno('Davi', 23, '12345678903', 'premium')]

        equipamentos = [Equipamento('Leg press 45', 'Forca', '0f0'),
                        Equipamento('Remada cavalo', 'Forca', '0f1'),
                        Equipamento('Esteira', 'Cardio', '0c0')]

        funcionarios = [Gerente('Yago', 22, '12345678900', 'Gerente', 4000),
                        Instrutor('Matheus', 21, '12345678901', 'Instrutor', 2600, 'Musculação'),
                        Funcionario('Ze', 20, '12345678902', 'Atendente', 1800)]

        academia = cls('ACADEMIA PADRÃO')
        academia.__lista_alunos = alunos
        academia.__lista_funcionarios = funcionarios
        academia.__lista_equipamentos = equipamentos
        return academia

    @staticmethod
    def validador_de_string(message, objeto):
        while True:
            string = str(input(message)).strip()
            if string.replace(' ', '').isalpha():
                return string.title()
            else:
                print(f'\033[1;31mError: {string} não é um {objeto} válido, tente novamente.\033[m')

    @staticmethod
    def validador_de_numero(tipo, message, objeto):
        while True:
            try:
                num = tipo(input(message))
                return num
            except ValueError:
                print(f'\033[1;31mError: {objeto} precisa ser um número do tipo {tipo}.\033[m')

    @staticmethod
    def validador_de_cpf():
        while True:
            cadastro = input('CPF: ').strip()
            if len(cadastro) == 11 and cadastro.isnumeric():
                return cadastro
            else:
                erro = '\033[1;31mCpf inválido! seu cpf precisa conter 11 dígitos\033[m' if cadastro.isnumeric() else '\033[1;31mCpf inválido! seu cpf precisa conter apenas números.\033[m'
                print(erro)

    @staticmethod
    def verificar_lista_tem_algo(lista):
        return False if len(lista) == 0 else True
