# Splunk: The Basics

> Categoria: Splunk / SOC
> Plataforma: TryHackMe
> Status: ✅ Estudado / evidenciado

## Objetivo
Entender componentes do Splunk, ingestão de dados e análise básica de logs em um ambiente SIEM.

## Conceitos
- Splunk e SIEM
- eventos e campos
- ingestão de logs
- busca e filtros
- dashboards e visibilidade
- normalização e contexto

## SPL inicial
```text
index=*
index=* sourcetype=access_combined
index=* | stats count by src_ip
index=* | timechart count by status
```

## Metodologia
Entender a fonte → restringir janela temporal → filtrar → agregar → investigar eventos específicos.

## O que eu aprendi
Splunk foi iniciado recentemente como parte dos estudos de Blue Team/SOC. Portanto, este registro é de **estudo**, não de conclusão oficial da room.

## Lições importantes
Buscar primeiro padrões e contexto, depois aprofundar em eventos individuais, ajuda a reduzir ruído.

## Referências
- https://tryhackme.com/room/splunk101
- https://docs.splunk.com/Documentation/Splunk
