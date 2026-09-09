# 📊 Splunk / SIEM

## Objetivo
Aprender a centralizar logs, pesquisar eventos, criar contexto e apoiar a triagem de alertas com SIEM.

## Conceitos
- eventos, campos e sourcetypes
- ingestão e normalização
- dashboards
- correlação
- alertas e tuning
- investigação baseada em timestamps e entidades

## SPL inicial
```text
index=* host=server01
index=* sourcetype=access_combined status>=400
index=* earliest=-24h latest=now | stats count by src_ip
```

Sempre limitar a busca ao contexto necessário para reduzir ruído e custo.

## Fluxo SOC
Alerta → validar → enriquecer → investigar → classificar → documentar → escalar/conter.

## TryHackMe relacionado
- Introduction to SIEM
- Splunk: The Basics
- Incident Handling with Splunk
- Investigating with Splunk

## Status
**Estudado / em andamento.** Splunk/SIEM já começou a ser estudado anteriormente.