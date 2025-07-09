> 📘 This README is available in: [🇺🇸 English](README.en.md) | [🇧🇷 Português](README.md)

# 📊 Otimização de Escalas com Gurobi

Este projeto aplica um modelo de **programação linear inteira** com uso do **Gurobi** para otimizar escalas de trabalho ao longo de um período de 24 horas, visando minimizar os custos salariais e atender diferentes cenários de demanda.

---

## 🎯 Objetivo

- Alocar funcionários em turnos de 6 horas ao longo de 24 períodos (horários) de forma ótima.
- Minimizar o custo total considerando multiplicadores salariais por hora.
- Garantir que todos os períodos sejam atendidos com o número mínimo de empregados exigidos.
- Testar o modelo em múltiplos cenários de demanda utilizando instâncias externas.

---

## 📁 Estrutura dos Arquivos

- `Trabalho Final.py` — script principal com definição do modelo e leitura dos dados.
- `Tab_Func.txt` — base de configuração contendo horários, exigência mínima e salários relativos.
- `inst_4a.txt` até `inst_6b.txt` — diferentes instâncias de demanda a serem testadas.

---

## ⚙️ Recursos Utilizados

- `gurobipy` — definição do modelo, variáveis, restrições e resolução.
- Manipulação de arquivos `.txt` para leitura dinâmica de parâmetros e instâncias.
- Lógica de looping para reconfigurar o modelo a cada cenário.

---

## 🧠 Variáveis do Modelo

- `x[i]` — número de funcionários que iniciam o turno na hora `i`
- `Q[i]` — número total de funcionários presentes na hora `i`

---

## 📌 Restrições

- Cada período deve ser atendido por funcionários que iniciaram nos últimos 6 horários.
- A presença total `Q[i]` deve respeitar o mínimo exigido definido em cada instância.
- As variáveis são inteiras e não-negativas.

---

## 💰 Função Objetivo

Minimizar:
```math
\sum_{i=0}^{23} Q[i] \times salário[i]
