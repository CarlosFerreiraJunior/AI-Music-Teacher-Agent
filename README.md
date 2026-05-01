# AI Music Teacher Agent

MVP local de um professor de música agentivo para violão e cavaquinho, com foco em estudo prático de músicas brasileiras.

## Visão geral

Este projeto expõe uma CLI que gera um plano de estudo para um aluno, baseado em:
- instrumento (`violao`, `cavaquinho`)
- nível (`iniciante`, `intermediario`, `avancado`)
- música e artista
- objetivo de estudo
- tempo disponível

A saída é um JSON estruturado com análise, exercícios e plano de estudo.

## Requisitos

- Python 3.10+
- Nenhuma dependência externa declarada no `pyproject.toml`

## Como executar

### Rodando pela CLI

```bash
cd /home/fiap-carlos/AI-Music-Teacher-Agent
python -m music_teacher.cli \
  --instrumento violao \
  --nivel iniciante \
  --musica Carinhoso \
  --artista Pixinguinha \
  --objetivo "aprender base" \
  --tempo-disponivel 20
```

### Exemplo usando JSON de entrada

```bash
python -m music_teacher.cli --input-json examples/request.json --json --no-save
```

### Parâmetros válidos

- `--instrumento`: `violao`, `cavaquinho`
- `--nivel`: `iniciante`, `intermediario`, `avancado`
- `--objetivo`: `tirar intro`, `aprender base`, `entender harmonia`
- `--tempo-disponivel`: inteiro (minutos)

## Arquivos do projeto

- `music_teacher/` – código da aplicação
- `tests/` – testes unitários
- `examples/request.json` – exemplo de payload de entrada
- `outputs/` – saída padrão da CLI
- `.gitignore` – arquivos ignorados pelo Git
- `pyproject.toml` – configurações do projeto e script de entrada

## Testes

```bash
python -m unittest discover -s tests
```

## Preparando para subir no GitHub

1. Inicialize o repositório, caso ainda não exista:

```bash
git init
```

2. Adicione os arquivos e faça commit:

```bash
git add .
git commit -m "Initial commit"
```

3. Configure o remoto GitHub:

```bash
git remote add origin https://github.com/SEU_USUARIO/AI-Music-Teacher-Agent.git
```

4. Envie para o branch `main`:

```bash
git branch -M main
git push -u origin main
```

> O arquivo `.gitignore` já está configurado para ignorar `outputs/`, `.venv/`, `.vscode/`, `build/` e outros artefatos locais.
