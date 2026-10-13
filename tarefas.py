"""Gerenciador de tarefas em linha de comando.

Guarda as tarefas em um arquivo JSON local.
Uso: python tarefas.py --help
"""
import argparse
import json
from datetime import datetime
from pathlib import Path

ARQUIVO = Path("tarefas.json")


def carregar():
    """Lê as tarefas do arquivo; retorna lista vazia se ele não existir."""
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text(encoding="utf-8"))
    return []


def salvar(tarefas):
    ARQUIVO.write_text(
        json.dumps(tarefas, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def adicionar(titulo):
    tarefas = carregar()
    novo_id = max((t["id"] for t in tarefas), default=0) + 1
    tarefas.append(
        {
            "id": novo_id,
            "titulo": titulo,
            "concluida": False,
            "criada_em": datetime.now().isoformat(timespec="seconds"),
        }
    )
    salvar(tarefas)
    print(f"Tarefa {novo_id} adicionada.")


def listar(somente_pendentes=False):
    tarefas = carregar()
    if somente_pendentes:
        tarefas = [t for t in tarefas if not t["concluida"]]
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for t in tarefas:
        marca = "x" if t["concluida"] else " "
        print(f"[{marca}] {t['id']:>3} - {t['titulo']}")


def concluir(id_tarefa):
    tarefas = carregar()
    for t in tarefas:
        if t["id"] == id_tarefa:
            t["concluida"] = True
            salvar(tarefas)
            print(f"Tarefa {id_tarefa} concluída.")
            return
    print(f"Tarefa {id_tarefa} não encontrada.")


def remover(id_tarefa):
    tarefas = carregar()
    restantes = [t for t in tarefas if t["id"] != id_tarefa]
    if len(restantes) == len(tarefas):
        print(f"Tarefa {id_tarefa} não encontrada.")
        return
    salvar(restantes)
    print(f"Tarefa {id_tarefa} removida.")


def main():
    parser = argparse.ArgumentParser(description="Gerenciador de tarefas")
    sub = parser.add_subparsers(dest="comando", required=True)

    p_add = sub.add_parser("add", help="adiciona uma tarefa")
    p_add.add_argument("titulo")

    p_list = sub.add_parser("list", help="lista tarefas")
    p_list.add_argument("--pendentes", action="store_true")

    p_done = sub.add_parser("done", help="marca como concluída")
    p_done.add_argument("id", type=int)

    p_rm = sub.add_parser("rm", help="remove uma tarefa")
    p_rm.add_argument("id", type=int)

    args = parser.parse_args()
    if args.comando == "add":
        adicionar(args.titulo)
    elif args.comando == "list":
        listar(args.pendentes)
    elif args.comando == "done":
        concluir(args.id)
    elif args.comando == "rm":
        remover(args.id)


if __name__ == "__main__":
    main()
