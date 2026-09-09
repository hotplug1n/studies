# Splunk: The Basics

> Categoria: SIEM / Splunk
> Status: ✅ Concluída — evidência visual no perfil

## Objetivo
Conhecer componentes básicos do Splunk e analisar logs em um cenário de SIEM.

## Conceitos aprendidos
- eventos, índices e campos
- ingestão de dados
- busca e filtros
- visibilidade para detecção

## Ferramentas
Splunk Web e SPL.

## Comandos importantes
```text
index=* earliest=-24h
index=main | stats count by host
```

## Metodologia
Definir fonte → buscar eventos → filtrar → agrupar → contextualizar → registrar.

## O que aprendi
Consolidei a importância de saber perguntar aos logs, não apenas olhar dashboards.

## Documentação de apoio
https://tryhackme.com/room/splunk101 · https://docs.splunk.com/Documentation/Splunk

## Evidência
Room concluída no perfil apresentado.