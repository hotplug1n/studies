# Nmap: The Basics

> Categoria: Recon / Networking
> Status: ✅ Concluída — evidência visual no perfil

## Objetivo
Descobrir hosts, portas e versões de serviços em laboratórios.

## Conceitos aprendidos
- host discovery
- estados de portas
- version detection
- NSE e timing
- formatos de saída

## Ferramentas
Nmap e terminal.

## Comandos importantes
```bash
nmap -sn 192.168.1.0/24
nmap -sV -p 22,80,443 LAB_IP
nmap -sC -sV LAB_IP
nmap -oA scans/host LAB_IP
```

## Metodologia
Descobrir → enumerar → identificar serviço → aprofundar na superfície exposta → registrar.

## O que aprendi
Consolidei que uma porta aberta é apenas o começo; o valor está em identificar e contextualizar o serviço.

## Documentação de apoio
https://tryhackme.com/room/nmap · https://nmap.org/book/man.html

## Evidência
Room concluída no perfil apresentado.