# Sprint 01 - Backlog do MVP

## Meta do Sprint

Entregar a base do MVP local do AI Music Teacher Agent: entrada estruturada, orquestracao de agentes, resposta consolidada e documentacao minima para execucao e validacao.

## Historias Priorizadas

### US-01 - Entrada estruturada do aluno

Como estudante de violao ou cavaquinho, quero informar instrumento, nivel, musica, artista, objetivo e tempo disponivel para receber uma orientacao adaptada.

**Criterios de aceitacao**

- Aceita input via CLI ou formulario simples.
- Valida campos obrigatorios.
- Restringe `instrumento` a `violao` ou `cavaquinho`.
- Restringe `nivel` a `iniciante`, `intermediario` ou `avancado`.
- Retorna erro claro quando o input e invalido.

### US-02 - Orquestracao inicial de agentes

Como usuario, quero que o sistema coordene agentes especializados para gerar uma resposta mais completa que uma resposta unica generica.

**Criterios de aceitacao**

- Existe um Planner Agent que recebe o input validado.
- Planner chama Search, Music Theory, Technique Coach e Study Plan.
- Cada agente retorna dados estruturados.
- Planner consolida todos os resultados em um objeto final.

### US-03 - Fontes relevantes

Como estudante, quero receber links de referencia para continuar estudando a musica e o objetivo escolhido.

**Criterios de aceitacao**

- Resposta contem lista de fontes com `tipo`, `titulo`, `url` e `relevancia`.
- MVP pode usar provider mockado ou configuravel.
- Nao copia cifras ou materiais proprietarios integralmente.

### US-04 - Analise musical pratica

Como estudante, quero uma explicacao simples da musica para entender o que praticar primeiro.

**Criterios de aceitacao**

- Resposta contem resumo musical.
- Resposta contem tom estimado ou indicacao de incerteza.
- Resposta contem desafios tecnicos e musicais.
- Linguagem e adaptada ao nivel informado.

### US-05 - Exercicios tecnicos adaptados

Como estudante, quero exercicios compativeis com meu instrumento, nivel e objetivo.

**Criterios de aceitacao**

- Resposta contem pelo menos 3 exercicios.
- Exercicios indicam duracao sugerida ou foco.
- Exercicios mudam conforme instrumento e nivel.

### US-06 - Plano de estudo por tempo disponivel

Como estudante, quero um plano de estudo dividido em blocos para conseguir praticar hoje.

**Criterios de aceitacao**

- Plano respeita `tempo_disponivel`.
- Plano contem blocos de aquecimento, tecnica, aplicacao e desafio.
- Soma dos blocos equivale ao tempo total informado.

### US-07 - Persistencia local do resultado

Como usuario local, quero salvar a resposta para acompanhar meu estudo.

**Criterios de aceitacao**

- Resultado pode ser salvo em JSON local.
- Arquivo contem input original e resposta consolidada.
- Caminho de saida e documentado.

### US-08 - Testes automatizados do MVP

Como equipe, quero testes para validar os contratos principais antes do checkpoint de QA.

**Criterios de aceitacao**

- Testes unitarios cobrem validacao de input.
- Testes unitarios cobrem distribuicao do plano por tempo.
- Teste de integracao cobre fluxo Planner -> agentes -> resposta final.
- Comando de teste e documentado.

## Fora de Escopo do Sprint

- Transcricao de audio.
- MIDI.
- Feedback automatico por gravacao.
- Login, contas ou cloud.
- Busca web obrigatoria em tempo real.
- Streamlit, caso CLI seja suficiente para fechar o MVP inicial.

## Definition of Done

- Codigo executa localmente.
- Saida contem fontes, analise, exercicios e plano.
- Documentacao atualizada em Markdown.
- Testes automatizados principais passam.
- QA valida fluxo feliz e erros de input.
- PM aprova checkpoint antes de implementacao e antes do fechamento pos-QA.

## Plano de Execucao Proposto

```mermaid
flowchart LR
    A[Design aprovado pelo PM] --> B[Contratos e modelos]
    B --> C[Agentes deterministas MVP]
    C --> D[CLI]
    D --> E[Persistencia JSON]
    E --> F[Testes unitarios]
    F --> G[Teste de integracao]
    G --> H[QA]
    H --> I[Checkpoint PM]
```
