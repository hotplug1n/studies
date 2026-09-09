# 🌿 Git Security

## Objetivo
Entender Git e GitHub como fonte de evidências e também como superfície de risco.

## Tópicos
- commits, branches e histórico
- diferenças entre working tree, index e repository
- secrets acidentais
- `.git` exposto
- remoção de credenciais do histórico
- dependabot, secret scanning e proteção de branches

## Investigação
```bash
git log --oneline --all
git show <commit>
git diff <old>..<new>
git rev-list --all
```

Ao encontrar um segredo exposto, a prioridade é revogar/rotacionar a credencial; apagar o arquivo sozinho não invalida o segredo.

## Status
**Em andamento.**