# 🛡️ Mini SOC Lab

Laboratório defensivo em Python para praticar o fluxo básico de um analista SOC: **coleta → detecção → triagem → investigação → recomendação**.

## 🎯 Objetivo

Analisar um arquivo de eventos de autenticação e identificar sinais simples de atividade suspeita, sem depender de um SIEM externo.

O projeto simula cenários comuns em logs:

- múltiplas falhas de autenticação em sequência;
- sucesso de login após várias falhas;
- tentativa de acesso a conta administrativa;
- concentração anormal de eventos por origem.

## 🧠 O que este projeto demonstra

- parsing de logs;
- criação de regras de detecção;
- correlação simples de eventos;
- classificação de severidade;
- geração de alertas reproduzíveis;
- fundamentos de investigação de incidentes;
- automação com Python.

## 🗂️ Estrutura

```text
mini-soc-lab/
├── README.md
├── detector.py
├── requirements.txt
└── data/
    └── auth.log
```

## ▶️ Executando

Requer Python 3.10+.

```bash
python3 detector.py data/auth.log
```

O detector imprime os alertas encontrados e um resumo da investigação.

## 🔎 Regras de detecção

### AUTH-001 — Brute Force

Dispara quando uma mesma origem registra **5 ou mais falhas** para a mesma conta dentro da janela configurada.

### AUTH-002 — Suspicious Success

Dispara quando ocorre um login bem-sucedido logo após uma sequência de falhas para a mesma conta e origem.

### AUTH-003 — Admin Targeting

Marca tentativas de autenticação contra contas administrativas como evento de maior prioridade para triagem.

## 📊 Exemplo de saída

```text
[HIGH] AUTH-001 192.0.2.50 -> admin | 7 failed attempts
[CRITICAL] AUTH-002 192.0.2.50 -> admin | successful login after failures
[HIGH] AUTH-003 192.0.2.50 -> admin | administrative account targeted
```

Os endereços usados nos dados de exemplo pertencem a faixas reservadas para documentação e laboratório.

## 🧪 Próximos passos

- adicionar parsing de logs Windows/Sysmon;
- exportar alertas em JSON;
- criar regras compatíveis com Splunk/Sigma;
- adicionar testes automatizados;
- construir um dashboard simples de incidentes.

## ⚠️ Escopo

Este projeto é exclusivamente defensivo e deve ser usado com dados próprios ou em ambientes autorizados.
