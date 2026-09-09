# Linux Fundamentals Part 1

> Categoria: Linux
> Plataforma: TryHackMe
> Status: ✅ Estudado / evidenciado

## Objetivo
Construir familiaridade com a linha de comando, filesystem e operadores do shell.

## Conceitos aprendidos
- hierarquia de diretórios
- comandos básicos de navegação
- busca com `find` e `grep`
- permissões e arquivos
- pipes e redirecionamento

## Ferramentas
Bash e utilitários GNU.

## Comandos importantes
```bash
pwd
ls -la
cd /etc
find /var/log -type f 2>/dev/null
grep -R "error" /var/log 2>/dev/null | head
command1 | command2
command1 > output.txt
```

## Metodologia
Navegar → localizar arquivos → filtrar conteúdo → combinar comandos → documentar resultado.

## O que eu aprendi
Linux e comandos de shell já fazem parte dos estudos práticos anteriores. A conclusão oficial desta room não foi presumida.

## Lições importantes
Entender o shell aumenta eficiência tanto em administração quanto em investigação de segurança.

## Referências
- https://tryhackme.com/room/linuxfundamentalspart1
