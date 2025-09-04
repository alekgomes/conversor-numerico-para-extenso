# Conversor 

Certa vez eu vi, em um vídeo, um rapaz falando que o teste para conseguir um emprego foi escrever um conversor que recebesse um número na sua forma numérica e retornasse o número na forma extensa. Achei a proposta interessante e resolvi escrever minha solução para esse desafio.

**unittest** usado para testes

## Como usar

### CLI (Interface de linha de comando)

```bash
# Converter um número para texto
python main.py 32
# Saída: trinta e dois

./main.py 155
# Saída: cento e cinquenta e cinco

# Exibir ajuda
python main.py --help
```

### Executar testes

```bash
# Executar todos os testes via CLI
python main.py --test

# Executar testes diretamente
python test_conversor.py

# Executar testes individuais
python -m unittest test_conversor.test_unidades
python -m unittest test_conversor.test_dezenas
python -m unittest test_conversor.test_centenas
```

### Usar como módulo

```python
from conversor import Numero

# Criar instância e converter
num = Numero(42)
print(num.escrever())  # quarenta e dois
```

## Estrutura do projeto

- `main.py` - Interface CLI principal
- `conversor.py` - Lógica de conversão (classe Numero)
- `test_conversor.py` - Testes unitários
- `conversor-poo.py` - Versão original (ainda funcional)

## Limitações

- Suporta números de 0 a 999
- Saída em português brasileiro
