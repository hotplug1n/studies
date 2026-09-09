# Tcpdump: The Basics

> Categoria: Traffic Analysis
> Status: ✅ Concluída — evidência visual no perfil

## Objetivo
Capturar e filtrar tráfego pela linha de comando.

## Conceitos aprendidos
- captura em interface
- filtros BPF
- salvamento em arquivo
- leitura resumida de pacotes

## Ferramentas
`tcpdump` e `libpcap`.

## Comandos importantes
```bash
tcpdump -D
tcpdump -i eth0 -n
tcpdump -i eth0 -n port 53
tcpdump -i eth0 -w capture.pcap
```

## Metodologia
Escolher interface → definir filtro → capturar → salvar → analisar em Wireshark quando necessário.

## O que aprendi
A linha de comando é útil para coleta rápida antes de uma análise visual detalhada.

## Documentação de apoio
https://tryhackme.com/room/tcpdump · https://www.tcpdump.org/manpages/tcpdump.1.html

## Evidência
Room concluída no perfil apresentado.