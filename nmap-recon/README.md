# 🔎 Nmap & Recon

## Objetivo
Desenvolver uma metodologia de reconhecimento que transforma um alvo autorizado em uma visão organizada de hosts, portas, serviços e versões.

## Fluxo
1. Descoberta de hosts.
2. Identificação de portas abertas.
3. Detecção de serviço e versão.
4. Enumeração específica do serviço.
5. Registro de evidências e hipóteses.

## Comandos-base
```bash
nmap -sn 192.168.1.0/24
nmap -sV -p 22,80,443 192.168.1.10
nmap -sC -sV 192.168.1.10
nmap -oA scans/target 192.168.1.10
```

`-sn` faz descoberta sem scan de portas; `-sV` tenta identificar versões; `-sC` executa o conjunto padrão de scripts NSE; `-oA` salva resultados em formatos úteis para documentação.

## Boas práticas
Evitar scans agressivos fora de um escopo autorizado. Registrar IP, horário, parâmetros usados, resultados e próximos passos.

## TryHackMe relacionado
- Nmap: The Basics
- Active Reconnaissance
- Nmap Live Host Discovery
- Nmap Basic Port Scans
- Nmap Advanced Port Scans
- Nmap Post Port Scans

## Status
**Estudado / em andamento.** Nmap já faz parte dos estudos práticos registrados; a conclusão das rooms específicas não foi presumida.