# TicTacPy

**Aplicação do Jogo do Galo desenvolvida em Python**

## 1. Descrição do Projeto

O TicTacPy consiste no desenvolvimento de uma aplicação baseada no tradicional Jogo do Galo, utilizando a linguagem de programação Python.

A aplicação permitirá ao utilizador disputar partidas contra um adversário controlado pelo computador, num tabuleiro de dimensões 3 × 3, com possibilidade de selecionar diferentes níveis de dificuldade e consultar informações relativas ao seu desempenho.

O desenvolvimento do projeto tem como principais objetivos a aplicação de conceitos de programação modular, estruturas de dados, algoritmos de decisão, validação de dados e persistência de informação.

O projeto é desenvolvido no âmbito da unidade curricular de **Fundamentos de Programação**, correspondente ao ano letivo 2026/2027.

## 2. Objetivos

Os principais objetivos do projeto são:

- Implementar as regras e a lógica de funcionamento do Jogo do Galo.
- Desenvolver um sistema de interação entre o utilizador e o computador.
- Implementar diferentes níveis de dificuldade.
- Desenvolver uma estratégia de decisão baseada no algoritmo Minimax.
- Implementar mecanismos de validação e tratamento de entradas inválidas.
- Registar e consultar o histórico de partidas.
- Implementar um sistema de persistência de dados.
- Desenvolver uma aplicação modular, organizada e de fácil manutenção.

## 3. Funcionalidades

As funcionalidades previstas para a aplicação encontram-se organizadas de acordo com a respetiva prioridade de desenvolvimento.

### 3.1. Funcionalidades essenciais

- Inicialização e reinicialização de partidas.
- Representação de um tabuleiro 3 × 3.
- Validação das jogadas efetuadas pelo utilizador.
- Execução automática das jogadas do computador.
- Deteção das condições de vitória, derrota e empate.
- Apresentação dos resultados de cada partida.

### 3.2. Funcionalidades planeadas

- Seleção de níveis de dificuldade.
- Implementação do algoritmo Minimax.
- Registo e consulta do histórico de partidas.
- Apresentação de estatísticas de desempenho.
- Configuração das opções da aplicação.
- Persistência de preferências e resultados entre execuções.

### 3.3. Funcionalidades opcionais

- Geração de comentários sobre as jogadas efetuadas, através de mecanismos de análise baseados em regras.

**Nota:** As funcionalidades apresentadas constituem os objetivos de desenvolvimento e não representam necessariamente funcionalidades já implementadas.

## 4. Inteligência do Jogo

O adversário controlado pelo computador deverá utilizar diferentes estratégias de decisão, correspondentes aos níveis de dificuldade disponíveis.

A implementação encontra-se planeada da seguinte forma:

| Nível | Estratégia prevista |
|---|---|
| Fácil | Seleção aleatória de posições disponíveis. |
| Intermédio | Estratégia de decisão baseada em regras. |
| Difícil | Algoritmo Minimax. |

O algoritmo Minimax será utilizado para analisar as possíveis sequências de jogadas e selecionar decisões que maximizem a possibilidade de vitória do computador, considerando também as respostas do adversário.

## 5. Arquitetura do Projeto

A aplicação será desenvolvida segundo uma arquitetura modular, separando a lógica do jogo, a interface, os mecanismos de decisão e a gestão de dados.

### 5.1. Estrutura prevista

```text
TicTacPy/
│
├── main.py
├── interface.py
├── jogo.py
├── ia.py
├── dados.py
│
├── data/
│   └── historico.json
│
├── tests/
│
├── README.md
└── .gitignore
```

### 5.2. Descrição dos módulos

| Módulo | Responsabilidade |
|---|---|
| `main.py` | Inicialização da aplicação e gestão do ciclo principal. |
| `interface.py` | Gestão dos menus, apresentação do tabuleiro e comunicação com o utilizador. |
| `jogo.py` | Implementação das regras, gestão do estado do tabuleiro e validação das jogadas. |
| `ia.py` | Implementação das estratégias de decisão do computador. |
| `dados.py` | Gestão da leitura e escrita de dados, histórico e configurações. |

A estrutura apresentada corresponde à arquitetura preliminar e poderá ser ajustada durante o desenvolvimento.

## 6. Tecnologias e Ferramentas

| Tecnologia | Aplicação |
|---|---|
| Python | Desenvolvimento da aplicação. |
| JSON | Persistência de dados. |
| Git | Controlo de versões. |
| GitHub | Gestão do repositório e acompanhamento do desenvolvimento. |

A utilização de SQLite poderá ser considerada numa fase posterior, como alternativa ou complemento ao sistema inicial de persistência baseado em JSON.

## 7. Planeamento do Desenvolvimento

O desenvolvimento encontra-se organizado em quatro sprints.

| Sprint | Período previsto | Objetivos |
|---|---|---|
| Sprint 1 | Até 13/11/2026 | Análise de requisitos, arquitetura e planeamento. |
| Sprint 2 | 26–27/11/2026 | Desenvolvimento do primeiro protótipo funcional. |
| Sprint 3 | 07–11/12/2026 | Implementação das dificuldades, interface e testes. |
| Sprint 4 | Até 08/01/2027 | Finalização, documentação e preparação da apresentação. |

### 7.1. Identificação das versões

O desenvolvimento será acompanhado através de versões identificadas:

- `v0.1` — Proposta e planeamento.
- `v0.2` — Primeiro protótipo funcional.
- `v0.3` — Implementação de melhorias e validação.
- `v1.0` — Versão final da aplicação.

## 8. Requisitos Técnicos

O desenvolvimento deverá respeitar os seguintes requisitos:

- Utilização da linguagem Python.
- Implementação de programação modular.
- Desenvolvimento de, pelo menos, cinco funções próprias.
- Implementação de, pelo menos, dois módulos próprios.
- Utilização de estruturas de dados adequadas.
- Validação de dados e tratamento de exceções.
- Implementação de mecanismos de persistência em ficheiro.
- Disponibilização de documentação técnica e manual de utilização.
- Utilização do GitHub durante o processo de desenvolvimento.

## 9. Instalação e Execução

As instruções de instalação, configuração e execução serão disponibilizadas após a implementação do primeiro protótipo funcional.

## 10. Estado do Desenvolvimento

O projeto encontra-se organizado de acordo com o planeamento definido para a unidade curricular de Fundamentos de Programação.

As funcionalidades, módulos e componentes descritos neste documento representam a especificação prevista para o desenvolvimento da aplicação.

O estado de implementação será atualizado ao longo das diferentes etapas do projeto.

## 11. Contexto Académico

| Informação | Descrição |
|---|---|
| Projeto | TicTacPy |
| Unidade curricular | Fundamentos de Programação |
| Curso | Engenharia Informática e Telecomunicações |
| Ano letivo | 2026/2027 |
| Instituição | ESTGL |
| Repositório | [ATUAPRIMA123/TicTacPy](https://github.com/ATUAPRIMA123/TicTacPy) |

---

**TicTacPy — Projeto académico de desenvolvimento de software em Python.**
