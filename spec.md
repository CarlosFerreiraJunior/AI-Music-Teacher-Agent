# 🎸 AI Music Teacher Agent

## 1. Visão do Produto

Construir um sistema de agentes de IA que atua como um professor de música personalizado para violão (nylon) e cavaquinho, focado em estilos brasileiros como samba, pagode e bossa nova.

O sistema deve ser capaz de:
- entender o objetivo do usuário (ex: aprender uma música, tirar uma introdução)
- buscar conteúdos relevantes (cifras, vídeos, aulas)
- analisar musicalmente a música
- traduzir isso em exercícios práticos
- gerar um plano de estudo estruturado
- evoluir com o usuário ao longo do tempo

---

## 2. Problema

Usuários que estudam música:
- não sabem exatamente o que estudar
- praticam de forma desestruturada
- têm dificuldade em tirar músicas de ouvido
- não possuem feedback ou plano progressivo

---

## 3. Objetivo do MVP

Criar um sistema funcional que:
- receba uma música e um objetivo
- retorne um plano de estudo estruturado
- sugira materiais externos relevantes
- explique a música de forma prática

---

## 4. Escopo do MVP

### Entrada do usuário

```json
{
  "instrumento": "violao | cavaquinho",
  "nivel": "iniciante | intermediario | avancado",
  "musica": "nome da musica",
  "artista": "nome do artista",
  "objetivo": "tirar intro | aprender base | entender harmonia",
  "tempo_disponivel": 20
}
```

---

### Saída esperada

- lista de fontes relevantes (links)
- análise musical simplificada
- principais desafios técnicos
- exercícios recomendados
- plano de estudo dividido por tempo

---

## 5. Arquitetura de Agentes

### 5.1 Planner Agent (Orquestrador)

Responsabilidades:

- interpretar o input do usuário
- definir estratégia de ensino
- coordenar os outros agentes
- consolidar resposta final

---

### 5.2 Search Agent

Responsabilidades:

- buscar conteúdos relevantes (cifras, vídeos, aulas)
- priorizar qualidade e relevância
- retornar lista estruturada de fontes

Output esperado:

```json
[
  {
    "tipo": "video | cifra | aula",
    "titulo": "...",
    "url": "...",
    "relevancia": "alta | media | baixa"
  }
]
```

---

### 5.3 Music Theory Agent

Responsabilidades:

- identificar tom e campo harmônico
- analisar progressões
- explicar de forma prática (não acadêmica)
- destacar dificuldades

---

### 5.4 Technique Coach Agent

Responsabilidades:

- sugerir exercícios técnicos
- propor levadas e padrões rítmicos
- adaptar ao instrumento
- transformar teoria em prática

---

### 5.5 Study Plan Agent

Responsabilidades:

- montar plano baseado no tempo disponível
- dividir em:
  - aquecimento
  - técnica
  - aplicação
  - desafio

Output esperado:

```text
Treino de 20 minutos:

1. Aquecimento (5 min)
2. Técnica (7 min)
3. Aplicação (5 min)
4. Desafio (3 min)
```

---

## 6. Fluxo do Sistema

```text
User Input
  → Planner Agent
      → Search Agent
      → Music Theory Agent
      → Technique Coach Agent
      → Study Plan Agent
  → Planner consolida resposta final
```

---

## 7. Stack Tecnológica

- Linguagem: Python
- Orquestração de agentes: LangGraph ou CrewAI
- LLM: OpenAI API
- Armazenamento (MVP): JSON local
- Interface: CLI ou Streamlit

---

## 8. Roadmap Evolutivo

### Fase 2 — Memória e Evolução

- Memory Agent (histórico do usuário)
- Progress Agent (ajuste de dificuldade)
- Feedback Agent (coleta de aprendizado)

---

### Fase 3 — MIDI

- MIDI Agent
- leitura de arquivos MIDI
- geração de cifra simplificada

---

### Fase 4 — Transcrição de Áudio

- Transcription Agent
- uso de ferramentas externas (ex: Basic Pitch, Demucs)
- extração de notas, acordes e BPM

---

### Fase 5 — Inteligência Musical Avançada

- Style Agent (samba/pagode/bossa)
- Improvisation Agent

---

## 9. Restrições

- Não gerar partituras completas protegidas por copyright
- Não copiar cifras proprietárias integralmente
- Priorizar explicação e ensino sobre reprodução literal

---

## 10. Critérios de Sucesso

- usuário consegue usar 3x por semana
- plano de estudo é claro e executável
- recomendações fazem sentido musicalmente
- sistema evolui com o uso

---

## 11. Definição de Pronto (MVP)

- input estruturado funcionando
- agentes orquestrados
- saída completa com:
  - fontes
  - análise
  - exercícios
  - plano
- execução via CLI ou UI simples

---

## 11.1 Artefatos do Sprint 01

- Arquitetura inicial do MVP: `docs/architecture-mvp.md`
- Backlog do sprint com historias e criterios de aceitacao: `docs/sprint-01-backlog.md`
- Relatorio de QA do sprint: `docs/qa-report-sprint-01.md`
- Checkpoint obrigatorio: PM deve aprovar arquitetura e backlog antes do inicio da implementacao.

---

## 12. Futuro (visão longa)

Transformar o sistema em:

> um professor musical inteligente que aprende com o usuário e adapta o ensino continuamente
