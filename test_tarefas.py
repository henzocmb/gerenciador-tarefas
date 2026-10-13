import tarefas


def test_adicionar_e_concluir(tmp_path, monkeypatch):
    monkeypatch.setattr(tarefas, "ARQUIVO", tmp_path / "t.json")
    tarefas.adicionar("estudar SQL")
    tarefas.adicionar("enviar currículos")
    tarefas.concluir(1)
    dados = tarefas.carregar()
    assert len(dados) == 2
    assert dados[0]["concluida"] is True
    assert dados[1]["concluida"] is False


def test_remover(tmp_path, monkeypatch):
    monkeypatch.setattr(tarefas, "ARQUIVO", tmp_path / "t.json")
    tarefas.adicionar("tarefa teste")
    tarefas.remover(1)
    assert tarefas.carregar() == []
