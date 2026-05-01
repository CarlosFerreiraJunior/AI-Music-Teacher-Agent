# AI Music Teacher Agent

MVP local de um professor de musica agentico para violao e cavaquinho, com foco em estudo pratico de musicas brasileiras.

## Executar via CLI

```powershell
python -m music_teacher.cli `
  --instrumento violao `
  --nivel iniciante `
  --musica Carinhoso `
  --artista Pixinguinha `
  --objetivo "aprender base" `
  --tempo-disponivel 20
```

Para imprimir JSON sem salvar arquivo:

```powershell
python -m music_teacher.cli --input-json examples\request.json --json --no-save
```

## Contrato de Entrada

```json
{
  "instrumento": "violao",
  "nivel": "iniciante",
  "musica": "Carinhoso",
  "artista": "Pixinguinha",
  "objetivo": "aprender base",
  "tempo_disponivel": 20
}
```

## Testes

```powershell
python -m unittest discover -s tests
```

Se o `python` global do Windows apontar para o alias da Microsoft Store, use `uv`:

```powershell
$env:UV_CACHE_DIR='.uv-cache'; uv run python -m unittest discover -s tests
```

## Saidas Locais

Por padrao, a CLI salva cada resposta em `outputs/` como JSON contendo o input original e a resposta consolidada.
