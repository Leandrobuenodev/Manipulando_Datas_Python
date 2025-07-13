# 📅 Verificador de Vencimento em Python

Um projeto simples em Python que verifica se uma data de vencimento já passou em relação à data atual. Ideal para praticar manipulação de datas, validação de entrada e lógica condicional com `datetime`.

Aceita datas no formato DD-MM-AAAA ou DD/MM/AAAA. O código retorna `True` se a data informada já passou e `False` se ainda está válida.

Para usar: clone o repositório, mantenha os arquivos `func.py` e `main_func.py` no mesmo diretório e execute `main_func.py`. Você será solicitado a inserir uma data. O sistema validará o formato e comparará com a data atual.

O arquivo `func.py` contém:
- Função `today()` que retorna a data atual
- Função `verify_date(date)` que interpreta strings nos dois formatos permitidos
- Função `verify_due(date_ref)` que compara a data de vencimento com hoje

O arquivo `main_func.py` importa essas funções, recebe a entrada do usuário via `input()` e retorna mensagens indicando se o prazo está vencido ou ainda válido. Também trata erros de formatação com um bloco `try/except`.

Requisitos:
- Python 3.7+
- Nenhuma biblioteca externa

Como executar:
1. Rode `python main_func.py`
2. Digite a data no formato solicitado
3. Veja no terminal se o vencimento já passou

Exemplo de uso via terminal:
→ Entrada: 10/10/2010  
→ Saída: ⚠️  A data de vencimento já passou.

→ Entrada: 25-12-2099  
→ Saída: ✅ A data de vencimento ainda está em dia.

