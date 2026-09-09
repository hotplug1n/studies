# Wireshark: The Basics

> Categoria: Traffic Analysis
> Status: ✅ Concluída — evidência visual no perfil

## Objetivo
Aprender a abrir, navegar e filtrar PCAPs.

## Conceitos aprendidos
- packet dissection
- navegação e filtros
- identificação de conversas e protocolos

## Ferramentas
Wireshark e PCAP/PCAPNG.

## Filtros importantes
```text
ip.addr == X.X.X.X
tcp.port == 80
http
dns
tcp.stream eq 0
```

## Metodologia
Visão geral → filtro → pacote → stream → contexto → evidência.

## O que aprendi
A análise fica muito mais eficiente quando começo amplo e só depois aplico filtros específicos.

## Documentação de apoio
https://tryhackme.com/room/wiresharkthebasics · https://www.wireshark.org/docs/

## Evidência
Room concluída no perfil apresentado.