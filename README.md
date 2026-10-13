# Gerenciador de Tarefas (CLI)

Aplicação de linha de comando em Python para gerenciar uma lista de tarefas, com persistência em arquivo JSON.

## Funcionalidades
- Adicionar, listar, concluir e remover tarefas
- Filtro para mostrar apenas pendentes
- Dados salvos em `tarefas.json`
- Testes automatizados com `pytest`

## Como usar
Requer Python 3.8+.

```bash
python tarefas.py add "Estudar SQL"
python tarefas.py list
python tarefas.py list --pendentes
python tarefas.py done 1
python tarefas.py rm 1
```

## Testes
```bash
pip install pytest
pytest
```

## Conceitos praticados
`argparse`, manipulação de arquivos, JSON, funções, listas e dicionários, testes unitários.

## Próximos passos
- Adicionar data limite e prioridade
- Trocar o JSON por SQLite
