# Atividade 1 — Projeto Overlap

## 1. Quais tabelas você definiu inicialmente?

Para a primeira versão do projeto, criei 4 tabelas principais:

* **`escuderia`:** Salva os dados do time do jogador (nome da equipe, orçamento e pontos no campeonato).
* **`pecas`:** Guarda as peças e componentes (pilotos, chassis, motores, chefes de equipe e mecânicos) com os atributos de cada um.
* **`circuitos`:** Armazena as pistas do calendário oficial da temporada com suas características.
* **`resultados_gp`:** Guarda a classificação final de cada GP, registrando a posição dos 20 carros do grid e quem pontuou.

---

## 2. Você utilizou migrations? Se sim, quantas migrations? Descreva em uma frase o que cada uma faz.

Sim, usei o próprio sistema de migrations do Django e até agora foram **2 migrations**:

* **Migration 1 (`0001_initial`):** Cria a estrutura inicial com as tabelas `Escuderia`, `Peca`, `Circuito` e `ResultadoGP` no banco.
* **Migration 2 (`0002_add_indexes`):** Adiciona alguns índices e ajusta as chaves estrangeiras para deixar as consultas das simulações mais rápidas.

---

## 3. Qual o caminho do arquivo que gera a seed do seu banco?

Criei um comando customizado no Django para popular os dados iniciais de pilotos, circuitos e equipes. O arquivo fica em:

`core/management/commands/seed_data.py`

---

## 4. Quais os endpoints que você irá implementar inicialmente? Cada endpoint deve ser um método e um path. Explique em um parágrafo por que você resolveu priorizar a implementação desses endpoints.

### Endpoints Iniciais:

* `POST /api/v1/escuderia/` — Cria a escuderia do jogador.
* `GET /api/v1/draft/sortear/` — Sorteia uma equipe histórica para o jogador escolher uma peça.
* `POST /api/v1/draft/escolher/` — Confirma a peça escolhida pelo jogador.
* `POST /api/v1/simulacao/gp/` — Roda a simulação da corrida para todos os 20 carros do grid.
* `GET /api/v1/campeonato/classificacao/` — Retorna a tabela atualizada dos Mundiais de Pilotos e Construtores.

### Justificativa:
Decidi priorizar esses endpoints porque eles formam o ciclo principal (*core loop*) do jogo. Para o projeto ter graça e funcionar de ponta a ponta, o jogador precisa criar o time, sortear/escolher as peças, simular a corrida e ver onde ficou na tabela de classificação. Focando nessas 5 rotas primeiro, consigo ter o jogo jogável do início ao fim da temporada antes de me preocupar com telas ou regras secundárias.

---

## 5. Você está usando algum framework para escrever os endpoints da sua API? Se sim, qual?

Sim, estou usando **Django** junto com o **Django REST Framework (DRF)** em Python. Escolhi o DRF porque ele facilita demais a criação dos serializers, já vem com roteamento pronto e me economiza tempo na parte de integração.
