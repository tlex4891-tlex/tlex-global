# Timeline — Claude Code Template

Template repozitář pro nové projekty s automatickou synchronizací globálních instrukcí pro Claude Code.

## Použití

1. Při vytváření nového repozitáře na GitHubu vyber tento repozitář jako **template**
2. Nový repozitář bude obsahovat SessionStart hook, který při každé session automaticky načte tvůj globální `CLAUDE.md`

## Co obsahuje

| Soubor | Účel |
|--------|------|
| `.claude/settings.json` | Definice SessionStart hooku |
| `.claude/hooks/session-start.sh` | Skript pro stažení `CLAUDE.md` z [`claude-global-config`](https://github.com/tlex4891-tlex/claude-global-config) |
| `CLAUDE.md` | Lokální placeholder — při startu session se přepíše aktuální verzí z `claude-global-config` |

## Jak to funguje

```
Nový repozitář (z template)
  └── .claude/
       ├── settings.json          ← spustí hook při SessionStart
       └── hooks/session-start.sh ← stáhne CLAUDE.md z claude-global-config
                                        ↓
                                  ~/.claude/CLAUDE.md  ← globální instrukce pro Claude
```

## Úprava globálních instrukcí

Edituj `CLAUDE.md` v repozitáři [claude-global-config](https://github.com/tlex4891-tlex/claude-global-config) — změny se automaticky projeví při každé nové session ve všech repozitářích vytvořených z tohoto template.

## Nastavení template

Aby tento repozitář fungoval jako template, je potřeba v **Settings** zaškrtnout **Template repository**.
