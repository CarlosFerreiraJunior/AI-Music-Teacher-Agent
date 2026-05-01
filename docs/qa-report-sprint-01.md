# QA Report - Sprint 01

## Escopo

Validar o MVP local com foco em:

- validacao de input estruturado;
- orquestracao Planner -> agentes especializados;
- resposta final com fontes, analise, exercicios e plano;
- soma dos blocos do plano igual ao tempo disponivel;
- persistencia JSON local.

## Testes Automatizados Criados

| Arquivo | Cobertura |
| --- | --- |
| `tests/test_models.py` | Validacao e normalizacao do input |
| `tests/test_agents.py` | Plano de estudo e contrato de resposta do Planner |
| `tests/test_storage.py` | Persistencia local em JSON |

## Comandos de Verificacao

```powershell
python -m unittest discover -s tests
python -m music_teacher.cli --input-json examples\request.json --no-save
```

## Resultado da Execucao

Status: aprovado.

Ambiente usado:

```powershell
$env:UV_CACHE_DIR='.uv-cache'; uv run python --version
```

Resultado:

```text
Python 3.14.4
```

Suite automatizada:

```powershell
$env:UV_CACHE_DIR='.uv-cache'; uv run python -m unittest discover -s tests
```

Resultado:

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

Smoke test da CLI:

```powershell
$env:UV_CACHE_DIR='.uv-cache'; uv run python -m music_teacher.cli --input-json examples\request.json --no-save
```

Resultado: plano de estudo renderizado em Markdown com fontes, analise, exercicios e blocos de treino.

## Risco Residual

O comando `python` global do Windows ainda aponta para o alias da Microsoft Store. Para execucao confiavel neste ambiente, usar `uv run python ...` ou ajustar o PATH do Python instalado.

## Recomendacao de QA

MVP aprovado para checkpoint do PM. Antes de uso continuo, padronizar a execucao local via `uv` ou instalar Python 3.10+ no PATH.
